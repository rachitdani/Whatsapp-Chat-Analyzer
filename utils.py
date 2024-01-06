from urlextract import URLExtract
extract = URLExtract()
import pandas as pd
from wordcloud import WordCloud
from collections import Counter

def fetch_stats(user,dataframe):

    if user != "Overall":
        dataframe = dataframe[dataframe['user'] == user]

    # number of messages
    num_messages = dataframe.shape[0]

    # number of words
    words = []
    for message in dataframe["messages"]:
        words.extend(message.split())

    # number of stickers
    num_stickers = dataframe['messages'].str.contains('sticker omitted', case=False).sum()

    # number of images
    num_images = dataframe['messages'].str.contains('image omitted', case=False).sum()

    # number of videos 
    num_videos = dataframe['messages'].str.contains('video omitted', case=False).sum()

    # number of gifs
    num_gifs = dataframe['messages'].str.contains('video omitted', case=False).sum()

    # number of deleted messages
    num_deleted_msg = dataframe['messages'].str.contains('This message was deleted.', case=False).sum()

    #number of links
    links = []
    for message in dataframe["messages"]:
        links.extend(extract.find_urls(message))

    return num_messages,len(words), num_stickers, num_images, num_videos, num_deleted_msg,len(links)


def most_busy_users(dataframe):
    x = dataframe['user'].value_counts().head(7)
    df1 = round((dataframe['user'].value_counts()/dataframe.shape[0])*100,2).reset_index().rename(columns={'count':'percent'})
    df2 = dataframe['user'].value_counts()
    df = pd.merge(df1, df2, on='user')
    return x,df


def create_wordcloud(selected_user,dataframe):
    f = open('stopwords.txt','r')
    stop_words = f.read()

    if selected_user != "Overall":
        dataframe = dataframe[dataframe['user'] == selected_user]
    
    # remove all rows which contained sticker/video/image/This "message was deleted. 
    ignore_text = ["image omitted", "This message was deleted." , "video omitted" , "sticker omitted","gif ommitted"]
    df_filtered = dataframe[~dataframe['messages'].apply(lambda x: any(substring in x for substring in ignore_text))]

    def remove_stop_words(message):
        y = []
        for word in message.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)
    
    wc = WordCloud(width=600,height =600,min_font_size=10,background_color="black")
    df_filtered["messages"] = df_filtered["messages"].apply(remove_stop_words)
    df_wc = wc.generate(df_filtered["messages"].str.cat(sep=" "))
    return df_wc


def most_common_words(selected_user,dataframe):

    f = open('stopwords.txt','r')
    stop_words = f.read()

    if selected_user != "Overall":
        dataframe = dataframe[dataframe['user'] == selected_user]

    # remove all rows which contained sticker/video/image/This "message was deleted. 
    ignore_text = ["image omitted", "This message was deleted." , "video omitted" , "sticker omitted","gif ommitted"]
    df_filtered = dataframe[~dataframe['messages'].apply(lambda x: any(substring in x for substring in ignore_text))]

    # remove stopwords
    words = []

    for message in df_filtered["messages"]:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)
    
    most_common_df = pd.DataFrame(Counter(words).most_common(25))

    return most_common_df

def monthly_timeline(selected_user,dataframe):
    if selected_user != "Overall":
        dataframe = dataframe[dataframe['user'] == selected_user]

    timeline = dataframe.groupby(['year','month']).count()['messages'].reset_index()

    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline["month"][i] + "-" + str(timeline["year"][i]))
    timeline["time"] = time

    return timeline
    
def daily_timeline(selected_user,dataframe):
    if selected_user != "Overall":
        dataframe = dataframe[dataframe['user'] == selected_user]

    timeline = dataframe.groupby("datee").count()["messages"].reset_index()
    return timeline

def week_activity(selected_user,dataframe):
    if selected_user != "Overall":
        dataframe = dataframe[dataframe['user'] == selected_user]

    day_timeline = dataframe["day_name"].value_counts().reset_index()

    return day_timeline

def month_activity(selected_user,dataframe):
    if selected_user != "Overall":
        dataframe = dataframe[dataframe['user'] == selected_user]

    month_time = dataframe["month"].value_counts().reset_index()

    return month_time

def activity_heatmap(selected_user,dataframe):

    if selected_user != "Overall":
        dataframe = dataframe[dataframe['user'] == selected_user]

    dataframe['period'] = pd.Categorical(dataframe['period'], categories=[f"{i:02d}-{(i + 1) % 24:02d}" for i in range(24)], ordered=True)
    pivot_activity = dataframe.pivot_table(index="day_name",columns="period",values = "messages",aggfunc='count').fillna(0)

    return pivot_activity




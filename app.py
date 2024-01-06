import streamlit as st
import preprocessor,utils
import matplotlib.pyplot as plt
import seaborn as sns

st.sidebar.title("Whatsapp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    #fetch unique users
    user_list = df["user"].unique().tolist()
    user_list.sort()
    user_list.insert(0,"Overall")

    selected_user = st.sidebar.selectbox("Show Analysis with respect to",user_list)

    if st.sidebar.button("Show Analysis"):

        # Stats Area
        num_messages, words, num_stickers, num_images, num_videos, num_deleted_msg,num_links = utils.fetch_stats(selected_user,df) 

        st.title("Top Statistics")

        col1, col2 = st.columns(2)

        col3,col4, col5, col6, col7 = st.columns(5)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(words)

        with col3:
            st.header("Total Links")
            st.title(num_links)        
        with col4:
            st.header("Total Stickers")
            st.title(num_stickers)
        with col5:
            st.header("Total Images")
            st.title(num_images)
        with col6:
            st.header("Total Videos")
            st.title(num_videos)
        with col7:
            st.header("Deleted Messages")
            st.title(num_deleted_msg)

        # Monthly Timeline
        st.title("Monthly Timeline")
        timeline = utils.monthly_timeline(selected_user, df)
        fig , ax = plt.subplots()

        ax.plot(timeline["time"],timeline["messages"],color = "red")
        plt.xticks(rotation="vertical")
        st.pyplot(fig)

        # Daily Timeline
        st.title("Daily Timeline")
        timeline = utils.daily_timeline(selected_user, df)
        fig , ax = plt.subplots()

        ax.plot(timeline["datee"],timeline["messages"],color = "green")
        plt.xticks(rotation="vertical")
        st.pyplot(fig)

        # Activity
        st.title('Activity Map')
        col8 , col9 = st.columns(2)

        with col8 :
            st.header("Daywise Activity")
            dayy = utils.week_activity(selected_user, df)
            fig,ax = plt.subplots()
            ax.bar(dayy["day_name"],dayy["count"])
            plt.xticks(rotation="vertical")
            st.pyplot(fig)

        with col9 :
            st.header("MonthWise Activity")
            month = utils.month_activity(selected_user, df)
            fig,ax = plt.subplots()
            ax.bar(month["month"],month["count"],color = "orange")
            plt.xticks(rotation="vertical")
            st.pyplot(fig)

        st.title("Weekly Timestamp Wise Activity Map")
        week_heatmap = utils.activity_heatmap(selected_user, df)
        fig,ax = plt.subplots()
        ax = sns.heatmap(week_heatmap,cmap="crest")
        st.pyplot(fig)

        # Finding the busiest users in the group(Group Level)
        if selected_user == "Overall":
            st.title("Participant Analyis")
            x,dff = utils.most_busy_users(df)
            fig, ax = plt.subplots()

            col8, col9 = st.columns(2)

            with col8:
                ax.bar(x.index,x.values)
                plt.xlabel('Users')
                plt.ylabel('Number of Messages')
                plt.xticks(rotation=45, ha='right')
                # Add count annotations on top of each bar
                for i, count in enumerate(x.values):
                    plt.text(i, count + 0.1, str(count), ha='center', va='bottom')

                st.pyplot(fig)
            
            with col9:
                st.dataframe(dff)

        # WordCloud
        st.title("Wordcloud")
        df_wc = utils.create_wordcloud(selected_user,df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        #Most Common Words
        st.title("Most Common Words")
        most_common_df = utils.most_common_words(selected_user, df)

        fig , ax = plt.subplots()

        bars = ax.barh(most_common_df[0],most_common_df[1])
        # Add count labels on top of each bar
        for bar in bars:
            plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f'{int(bar.get_width())}', va = "center",fontsize=8, color='black')
        plt.xlabel('Count')
        plt.ylabel('Messages')
        plt.xticks(rotation = 45)

        st.pyplot(fig)

        





        
        
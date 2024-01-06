import re
import pandas as pd

def preprocess(data):
    # Data cleaning and Extracting the required Information
    pattern = r"\[([^]]+)\] (.+?(?=\n|\Z))"
    matches = re.findall(pattern, data)
    messages_list = [list(match) for match in matches]

    # Converting list to dataframe
    df = pd.DataFrame(messages_list,columns=["date","user_message"])

    # Some Preprocessing
    df = df[df['date'].str.contains('AM|PM', case=False)]

    # Converting dataframe to datetime datatype
    df["date"] = pd.to_datetime(df["date"],format="%d/%m/%y, %I:%M:%S %p",errors="coerce")
    df.dropna(inplace=True)

    # Seperate users and messages
    users = []
    messages = []
    for message in df["user_message"]:
        info = re.split('([\w\W]+?):\s',message)
        try:
            if info[1:]:
                users.append(info[1])
                messages.append(info[2])
            else:
                users.append('group_notification')
                messages.append(info[0])
        except Exception as e:
            raise("Error Occured")
            
    df['user'] = users
    df['messages'] = messages
    df.drop(columns=['user_message'],inplace=True)

    # Extracting the individul components of the date
    df['day'] = df['date'].dt.day
    df['month'] = df['date'].dt.month_name()
    df['year'] = df['date'].dt.year
    df['hour'] = df['date'].dt.hour
    df['min'] = df['date'].dt.minute
    df['sec'] = df['date'].dt.second
    df['datee'] = df['date'].dt.date
    df["day_name"] = df["date"].dt.day_name()

    # for heatmap
    period = []
    for hour in df[['day_name','hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))    
        elif hour == 0:
            period.append(str('00') + "-" + str(hour+1))  
        else:
            period.append(str(hour) + "-" + str(hour+1))
    df["period"] = period

    return df

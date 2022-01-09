import pandas as pd
import datetime

local_df = pd.DataFrame(pd.read_csv('locale.csv'))



for i in range(0,1):
    city = local_df['city'][i]
    df1 = pd.DataFrame(pd.read_csv(str(city) + '.csv'))
    df1.insert(0, 'day', '')
    df1.insert(0, 'month', '')
    df1.insert(0, 'year', '')
    df1.insert(0, 'city', '')

    for i in range(len(df1)):
        data = datetime.datetime.strptime(str(df1['time'][i]), "%Y/%m/%d %H:%M")
        df1['month'][i] = data.month
        df1['year'][i] = data.year
        data = datetime.date(data.year, data.month, data.day)
        day = data - datetime.date(data.year - 1, 12, 31)
        df1['day'][i] = (int(day.days))
        df1['city'][i] = city
    df1.to_csv(str(city) +'1.csv',index=None)


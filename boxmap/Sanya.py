import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def draw(city, df,m1,m2):
    plt.title(str(city))
    a = sns.barplot(x="month", y="tp", data=df, hue='2011-2012/2019-2021',ci = 95,errwidth = 1.5, capsize = 0.2)
    # sns.violinplot(x="month", y="tp", data=df, hue='2011-2012/2019-2021')
    # sns.boxplot(x="month", y="tp", data=df, hue='2011-2012/2019-2021')
    plt.vlines(m1-0.5, 0, 0.3, color="green", linestyles='--')  # 竖线
    plt.vlines(m2+0.5, 0, 0.3, color="red", linestyles='--')  # 竖线

    # plt.grid(axis="y")
    legend1 = plt.legend(bbox_to_anchor=(0.9, 1.25),fontsize=24,loc='lower center',borderaxespad=0)
    legend1.texts[0].set_text("2011-2012")
    plt.xlabel('Month', )
    plt.ylabel('Precipitation(mm)',)
    plt.yticks()
    plt.xticks()
    plt.legend()

    # a.legend_.remove()
local_df = pd.DataFrame(pd.read_csv('locale.csv'))
city = local_df['city'][0]
month1 = local_df['month1'][0]
month2 = local_df['month2'][0]
df1 = pd.DataFrame(pd.read_csv(str(city) +'1.csv'))
df2 = df1.groupby(['year', 'month','day'], as_index=False)['tp'].sum()
df2.insert(0, '2011-2012/2019-2021', '')
for t in range(len(df2)):
    if df2['year'][t] <= 2012:
        df2['2011-2012/2019-2021'][t] = '2011-2012'
    else:
        df2['2011-2012/2019-2021'][t] = '2019-2021'

draw(city,df2,month1,month2)

# plt.figtext(0.5, 0.05, 'Month', fontsize=16)
# plt.figtext(0.05, 0.5, 'Precipitation(mm)', va='center', rotation='vertical',fontsize=16)
# plt.suptitle('Comparison: Daily Precipitation', fontsize=14)

plt.savefig('precipitation_sanya.tif',format='tif',dpi=600)
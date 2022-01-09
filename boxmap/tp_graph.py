import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def draw(city, df,m1,m2,i):
    plt.title(str(city),fontsize=10)
    a = sns.barplot(x="month", y="tp", data=df, hue='2011-2012/2019-2021',ci = 95,errwidth = 1.5, capsize = 0.2)
    # sns.violinplot(x="month", y="tp", data=df, hue='2011-2012/2019-2021')
    # sns.boxplot(x="month", y="tp", data=df, hue='2011-2012/2019-2021')
    plt.vlines(m1-0.5, 0, 0.3, color="green", linestyles='--')  # 竖线
    plt.vlines(m2+0.5, 0, 0.3, color="red", linestyles='--')  # 竖线

    # plt.grid(axis="y")
    legend1 = plt.legend(bbox_to_anchor=(0.9, 1.15),loc='lower center',borderaxespad=0,fontsize=7)
    legend1.texts[0].set_text("2011-2012")
    plt.xlabel(None)
    plt.ylabel(None)
    # plt.set_xlabel(fontsize=17)
    # plt.set_ylabel(fontsize=17)
    plt.yticks()
    plt.xticks()
    # plt.legend(fontsize=12)
    if i != 1:
        a.legend_.remove()


local_df = pd.DataFrame(pd.read_csv('locale.csv'))
fig, axes = plt.subplots(4, 2, sharex='all', sharey='row')
# plt.autoscale(enable=True, axis="both", tight=True)
fig.subplots_adjust(hspace=0.4, wspace=0.02)
plt.figtext(0.48, 0.03, 'Month')
plt.figtext(0.04, 0.5, 'Precipitation(mm)', va='center', rotation='vertical')
# plt.suptitle('Comparison: Daily Precipitation', fontsize=14)



for i in range(len(local_df)):
    city = local_df['city'][i]
    month1 = local_df['month1'][i]
    month2 = local_df['month2'][i]
    df1 = pd.DataFrame(pd.read_csv(str(city) +'1.csv'))
    df2 = df1.groupby(['year', 'month','day'], as_index=False)['tp'].sum()
    df2.insert(0, '2011-2012/2019-2021', '')
    for t in range(len(df2)):
        if df2['year'][t] <= 2012:
            df2['2011-2012/2019-2021'][t] = '2011-2012'
        else:
            df2['2011-2012/2019-2021'][t] = '2019-2021'
    df2.to_csv(str(city) +'2.csv')

    plt.subplot(4,2,i+1)
    draw(city,df2,month1,month2,i)


# plt.legend()
# plt.savefig('precipitation.tif',format='tif',dpi=600)
plt.show()
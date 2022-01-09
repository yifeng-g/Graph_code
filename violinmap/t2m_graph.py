import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

def draw(city, df, m1, m2,i):
    plt.title(str(city),fontsize=10)
    # a= sns.boxplot(x="month", y="t2m", data=df,hue='2011-2012/2019-2021')
    a = sns.violinplot(x="month", y="t2m", data=df,split=True,hue='2011-2012/2019-2021',ci=0)
    # sns.barplot(x="month", y="t2m", data=df, hue='2011-2012/2019-2021',ci=0)
    # plt.hlines(0, -3, 3, color="red")  # 横线
    plt.vlines(m1-0.5, -15, 45, color="green", linestyles='--')  # 竖线
    plt.vlines(m2+0.5, -15, 45, color="red", linestyles='--')  # 竖线
    # legend = plt.legend(bbox_to_anchor=(1, 1.25),fontsize=8,loc='upper right',borderaxespad=0)
    legend1 = plt.legend(bbox_to_anchor=(0.9, 1.15),loc='lower center',borderaxespad=0,fontsize=7)
    legend1.texts[0].set_text("2011-2012")
    plt.xlabel(None)
    plt.ylabel(None)
    plt.yticks()
    plt.xticks()
    plt.ylim(-15,45)
    # color = ['green', 'red']
    # labels = ['start time', 'end time']
    # patches = [mpatches.Patch(color=color[i], label="{:s}".format(labels[i])) for i in range(len(color))]
    # a.legend(handles=patches, bbox_to_anchor=(0.95,1.12), ncol=4)
    # plt.gca().add_artist(l1)
    # plt.legend(fontsize=12)

    if i != 1:
        a.legend_.remove()


    # my_y_ticks = np.arange(-15, 45, 10)
    # plt.yticks(my_y_ticks)



insert = pd.read_excel('insert.xlsx')
local_df = pd.DataFrame(pd.read_csv('locale.csv'))
fig, axes = plt.subplots(4, 2, sharex='all', sharey='row')
# plt.autoscale(enable=True, axis="both", tight=True)
fig.subplots_adjust(hspace=0.4, wspace=0.02)
plt.figtext(0.48, 0.05, 'Month', )
plt.figtext(0.04, 0.5, 'Temperature(℃)', va='center', rotation='vertical')
# plt.suptitle('Comparison: Hourly Temperature', fontsize=14)






for i in range(len(local_df)):
    city = local_df['city'][i]
    month1 = local_df['month1'][i]
    month2 = local_df['month2'][i]
    df1 = pd.DataFrame(pd.read_csv(str(city) +'2.csv'))
    # df1.insert(0, '2011-2012/2019-2021', '')
    # for t in range(len(df1)):
    #     if df1['year'][t] <= 2012:
    #         df1['2011-2012/2019-2021'][t] = '2011-2012'
    #     else:
    #         df1['2011-2012/2019-2021'][t] = '2019-2021'
    #     df1["t2m"][t] = df1["t2m"][t] - 273.15
    # df1.to_csv((str(city) +'2.csv'), index=None)

    plt.subplot(4,2,i+1)
    draw(city,df1,month1,month2,i)


# plt.legend()
# plt.show()
plt.savefig('temperature1.tif',format='tif',dpi=600)
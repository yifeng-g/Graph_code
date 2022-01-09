import matplotlib.pylab as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.colors as colors


rgb = [1,1,20],[3,4,94],[2,62,138],[0,119,182],[0,150,199],[0,150,199],[0,150,199],[0,150,199],[0,150,199], [0,180,216],[0,180,216],[0,180,216],[0,180,216],[0,180,216], [72,202,228] ,[72,202,228] ,[72,202,228] ,[72,202,228] ,[72,202,228] ,[72,202,228] ,[144,224,239],[144,224,239],[144,224,239],[144,224,239],[144,224,239],[144,224,239],[173,232,244],[173,232,244],[173,232,244],[173,232,244],[173,232,244],[173,232,244],[202,240,248],[202,240,248],[202,240,248],
rgb=np.array(rgb)/255.0

icmap=colors.ListedColormap(rgb,name='my_color')


df = pd.read_excel('PH_VARIANCE.xlsx',index_col='Unnamed: 0')
df1 = pd.read_excel('PH_VALUES.xlsx',index_col='Unnamed: 0')
df2 = pd.read_excel('PH_VARIANCE_diff.xlsx',index_col='Unnamed: 0')
df3 = pd.read_excel('PH_VALUES_diff.xlsx',index_col='Unnamed: 0')
sns.set_theme(style="dark",font='Times New Roman')


###figure1###
df1 = df1 *-1
df_min = df1.min().min()
df_max = df1.max().max()
df_range = df_max-df_min

# sns.heatmap(pd.DataFrame(df), linewidths=0.1, xticklabels=False, yticklabels=False, cmap='rainbow', cbar=None, annot=True,annot_kws={'size':10,'color':'yellow'}, fmt='.2g',alpha = 0,)
# sns.heatmap(pd.DataFrame(df2), linewidths=0.1, xticklabels=False, yticklabels=False, cmap='rainbow', cbar=None, annot=True,annot_kws={'size':10,'color':'red'}, fmt='.2g',alpha = 0)
# c = sns.heatmap(pd.DataFrame(df1), linewidths=0.1, xticklabels=True, yticklabels=True, cmap=icmap.reversed(),fmt='.2f',cbar_kws={'ticks':[df_min+(1/5)*df_range,df_min+(2/5)*df_range,df_min+(3/5)*df_range,df_min+(4/5)*df_range],'format':ticker.FixedFormatter(['Fair','Good','Better','Excellent']),})



#figure2###
df_min = df3.min().min()
df_max = df3.max().max()
negative = 0- df_min
range
# print(negative)
print(df_max)
print(df_min)
sns.heatmap(pd.DataFrame(df), linewidths=0.1, xticklabels=False, yticklabels=False, cmap='rainbow', cbar=None, annot=True,annot_kws={'size':10,'color':'white'}, fmt='.2g',alpha = 0,)

sns.heatmap(pd.DataFrame(df3), linewidths=0.1, xticklabels=True, yticklabels=True, cmap='Blues' ,fmt='.2f',vmin = -0.01,vmax=df_max,cbar_kws={'ticks':[-0.008,0,0.008,0.016,0.024,0.032],'format':ticker.FixedFormatter(['Negative improv.','No improv.','Little improv.','Medium improv.','Large improv.']),})


plt.savefig('ph.tif',format='tif',dpi=600)
# plt.show()


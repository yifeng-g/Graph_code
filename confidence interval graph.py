import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv("merge.csv")
plt.figure(figsize=(16, 8))

data_x = pd.DataFrame(data['soybeans_planted_areas'],dtype=float)
data_y = pd.DataFrame(data['soybeans_harvested_areas'],dtype=float)
sns.regplot(x='soybeans_planted_areas',y='soybeans_harvested_areas',data=data,scatter=False)

plt.savefig('3-3.png')
print

help(sns.regplot)
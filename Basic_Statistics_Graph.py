import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#导入 整理 检查数据
data = pd.read_csv("data.csv")
data_y= pd.DataFrame(data['x'],dtype=float)
data_x= pd.DataFrame(data['year'],dtype=int)
print(data['x'])
print(data['year'])

#设置图表大小
plt.figure(figsize=(10,6))
#设置图表名
plt.title('year and value1')
#fontsize设置字体大小，默认12，可以写字体大小或参数，可选参数 ['xx-small', 'x-small', 'small', 'medium', 'large','x-large', 'xx-large']
#fontweight设置字体粗细，可选参数 ['light', 'normal', 'medium', 'semibold', 'bold', 'heavy', 'black']
#fontstyle设置字体类型，可选参数[ 'normal' | 'italic' | 'oblique' ]，italic斜体，oblique倾斜
#verticalalignment设置水平对齐方式 ，可选参数 ： 'center' , 'top' , 'bottom' ,'baseline'
#horizontalalignment设置垂直对齐方式，可选参数：left,right,center
#rotation(旋转角度)可选参数为:vertical,horizontal 也可以为数字
#alpha透明度，参数值0至1之间
#loc设置位置，可选参数：left,right,center
#color

#设置轴标签
plt.xlabel('year')
plt.ylabel('x')
#作图
plt.scatter(data_x,data_y,c='k')#散点图
#plt.plot(data_x,data_y,c='b') #折线图 linewidth设置粗细，linestyle设置‘-’直线,‘--’虚线
#设置坐标轴粗细
ax=plt.gca();#获得坐标轴变量
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
#设置坐标轴区间
plt.xlim(2008,2019)
plt.ylim(0,3)
#omatplotlib.pyplot.axis([xmin, xmax, ymin, ymax])

#设置坐标轴刻度
plt.xticks(range(2008, 2019, 1))
plt.tick_params(axis='both',labelsize = 10)
#保存图片（在show之前）
plt.savefig('3.1.png')

plt.show()

# c青红（cyan）	r  红色（red）	m  品红（magente） g  绿色（green）
# y黄色（yellow）	k  黑色（black）	w  白色（white）   b 蓝色（blue）
help(plt.xlim)
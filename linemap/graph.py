import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def p1():
    def draw1(number,name,df):
        plt.title('population vs. year'+'('+str(name)+')')
        sns.despine()
        plt.grid(axis="y")
        sns.lineplot(x="year", y="popc"+str(number), data=df,label='popc')
        sns.lineplot(x="year", y="rurc"+str(number), data=df,label='rurc')
        sns.lineplot(x="year", y="urbc"+str(number), data=df,label='urbc')
        sns.distplot()
        plt.legend()
        y = [0,5,10,15,19,23,27,32,37,42,47,52,57,62,67,72,77]
        plt.xticks(y,rotation=60)

    df = pd.read_excel('popu_data.xlsx')
    plt.rcParams['figure.figsize'] = (30.0, 16.0)

    plt.subplot(3,3,1)
    draw1(0,'global',df)
    plt.subplot(3,3,4)
    draw1(1,'Africa',df)
    plt.subplot(3,3,5)
    draw1(2,'Asia',df)
    plt.subplot(3,3,6)
    draw1(3,'Australia',df)
    plt.subplot(3,3,7)
    draw1(4,'Europe',df)
    plt.subplot(3,3,8)
    draw1(5,'North America',df)
    plt.subplot(3,3,9)
    draw1(6,'South America',df)

    plt.tight_layout(pad=6)
    # plt.show()
    plt.savefig('population vs. year.png',bbox_inches='tight')

def p2():
    def draw1(number,name,df):
        plt.title('land vs. year'+'('+str(name)+')')
        sns.despine()
        plt.grid(axis="y")
        sns.lineplot(x="year", y="cropland"+str(number), data=df,label='cropland')
        sns.lineplot(x="year", y="tot_rainfed"+str(number), data=df,label='tot_rainfed')
        sns.lineplot(x="year", y="tot_irri"+str(number), data=df,label='tot_irri')
        sns.distplot()
        plt.legend()
        y = [0,5,10,15,19,23,27,32,37,42,47,52,57,62,67,72,77]
        plt.xticks(y,rotation=60)

    df = pd.read_excel('popu_data.xlsx')
    plt.rcParams['figure.figsize'] = (30.0, 16.0)

    plt.subplot(3,3,1)
    draw1(0,'global',df)
    plt.subplot(3,3,4)
    draw1(1,'Africa',df)
    plt.subplot(3,3,5)
    draw1(2,'Asia',df)
    plt.subplot(3,3,6)
    draw1(3,'Australia',df)
    plt.subplot(3,3,7)
    draw1(4,'Europe',df)
    plt.subplot(3,3,8)
    draw1(5,'North America',df)
    plt.subplot(3,3,9)
    draw1(6,'South America',df)

    plt.tight_layout(pad=6)
    # plt.show()
    plt.savefig('land vs. year.png',bbox_inches='tight')

def p3():
    def draw1(number,name,df):
        plt.title('population vs. year'+'('+str(name)+')')
        sns.despine()
        plt.grid(axis="y")
        sns.lineplot(x="year", y="popc"+str(number), data=df,label='popc')
        sns.lineplot(x="year", y="rurc"+str(number), data=df,label='rurc')
        sns.lineplot(x="year", y="urbc"+str(number), data=df,label='urbc')
        sns.distplot()
        plt.legend()
        y = range(0,len(df),5)
        plt.xticks(y,rotation=60)

    df = pd.read_excel('popu_data1.xlsx')
    plt.rcParams['figure.figsize'] = (30.0, 16.0)

    plt.subplot(3,3,1)
    draw1(0,'global',df)
    plt.subplot(3,3,4)
    draw1(1,'Africa',df)
    plt.subplot(3,3,5)
    draw1(2,'Asia',df)
    plt.subplot(3,3,6)
    draw1(3,'Australia',df)
    plt.subplot(3,3,7)
    draw1(4,'Europe',df)
    plt.subplot(3,3,8)
    draw1(5,'North America',df)
    plt.subplot(3,3,9)
    draw1(6,'South America',df)

    plt.tight_layout(pad=6)
    # plt.show()
    plt.savefig('population vs. year(after 1700AD).png',bbox_inches='tight')

def p4():
    def draw1(number,name,df):
        plt.title('population vs. year'+'('+str(name)+')')
        sns.despine()
        plt.grid(axis="y")
        sns.lineplot(x="year", y="cropland"+str(number), data=df,label='cropland')
        sns.lineplot(x="year", y="tot_rainfed"+str(number), data=df,label='tot_rainfed')
        sns.lineplot(x="year", y="tot_irri"+str(number), data=df,label='tot_irri')
        sns.distplot()
        plt.legend()
        y = range(0,len(df),5)
        plt.xticks(y,rotation=60)

    df = pd.read_excel('popu_data1.xlsx')
    df = df
    plt.rcParams['figure.figsize'] = (30.0, 16.0)

    plt.subplot(3,3,1)
    draw1(0,'global',df)
    plt.subplot(3,3,4)
    draw1(1,'Africa',df)
    plt.subplot(3,3,5)
    draw1(2,'Asia',df)
    plt.subplot(3,3,6)
    draw1(3,'Australia',df)
    plt.subplot(3,3,7)
    draw1(4,'Europe',df)
    plt.subplot(3,3,8)
    draw1(5,'North America',df)
    plt.subplot(3,3,9)
    draw1(6,'South America',df)

    plt.tight_layout(pad=6)
    # plt.show()
    plt.savefig('area vs. year(after 1700AD).png',bbox_inches='tight')

def p5():
    def draw1(number,name,df):
        plt.title('population/area vs. year'+'('+str(name)+')')
        sns.despine()
        plt.grid(axis="y")
        sns.lineplot(x="year", y="popc"+str(number), data=df,label='popc/area')
        sns.lineplot(x="year", y="rurc"+str(number), data=df,label='rurc/area')
        sns.lineplot(x="year", y="urbc"+str(number), data=df,label='urbc/area')
        plt.ylabel('pop/area')
        sns.distplot()
        plt.legend()
        y = [0,5,10,15,19,23,27,32,37,42,47,52,57,62,67,72,77]
        plt.xticks(y,rotation=60)

    df = pd.read_excel('popu_data2.xlsx')
    plt.rcParams['figure.figsize'] = (30.0, 16.0)

    plt.subplot(3,3,1)
    draw1(0,'global',df)
    plt.subplot(3,3,4)
    draw1(1,'Africa',df)
    plt.subplot(3,3,5)
    draw1(2,'Asia',df)
    plt.subplot(3,3,6)
    draw1(3,'Australia',df)
    plt.subplot(3,3,7)
    draw1(4,'Europe',df)
    plt.subplot(3,3,8)
    draw1(5,'North America',df)
    plt.subplot(3,3,9)
    draw1(6,'South America',df)

    plt.tight_layout(pad=6)
    # plt.show()
    plt.savefig('Population-area vs. year.png',bbox_inches='tight')

def p6():
    def draw1(number,name,df):
        plt.title('land/area vs. year'+'('+str(name)+')')
        sns.despine()
        plt.grid(axis="y")
        sns.lineplot(x="year", y="cropland"+str(number), data=df,label='cropland/area')
        sns.lineplot(x="year", y="tot_rainfed"+str(number), data=df,label='tot_rainfed/area')
        sns.lineplot(x="year", y="tot_irri"+str(number), data=df,label='tot_irri/area')
        plt.ylabel('land/area')
        sns.distplot()
        plt.legend()
        y = [0,5,10,15,19,23,27,32,37,42,47,52,57,62,67,72,77]
        plt.xticks(y,rotation=60)

    df = pd.read_excel('popu_data2.xlsx')
    plt.rcParams['figure.figsize'] = (30.0, 16.0)

    plt.subplot(3,3,1)
    draw1(0,'global',df)
    plt.subplot(3,3,4)
    draw1(1,'Africa',df)
    plt.subplot(3,3,5)
    draw1(2,'Asia',df)
    plt.subplot(3,3,6)
    draw1(3,'Australia',df)
    plt.subplot(3,3,7)
    draw1(4,'Europe',df)
    plt.subplot(3,3,8)
    draw1(5,'North America',df)
    plt.subplot(3,3,9)
    draw1(6,'South America',df)

    plt.tight_layout(pad=6)
    # plt.show()
    plt.savefig('land-area vs. year.png',bbox_inches='tight')

def p7():
    def draw1(number,name,df):
        plt.title('population/area vs. year(after 1700AD)'+'('+str(name)+')')
        sns.despine()
        plt.grid(axis="y")
        sns.lineplot(x="year", y="popc" + str(number), data=df, label='popc/area')
        sns.lineplot(x="year", y="rurc" + str(number), data=df, label='rurc/area')
        sns.lineplot(x="year", y="urbc" + str(number), data=df, label='urbc/area')
        plt.ylabel('pop/area')
        sns.distplot()
        plt.legend()
        y = range(0,len(df),5)
        plt.xticks(y,rotation=60)

    df = pd.read_excel('popu_data4.xlsx')
    plt.rcParams['figure.figsize'] = (30.0, 16.0)

    plt.subplot(3,3,1)
    draw1(0,'global',df)
    plt.subplot(3,3,4)
    draw1(1,'Africa',df)
    plt.subplot(3,3,5)
    draw1(2,'Asia',df)
    plt.subplot(3,3,6)
    draw1(3,'Australia',df)
    plt.subplot(3,3,7)
    draw1(4,'Europe',df)
    plt.subplot(3,3,8)
    draw1(5,'North America',df)
    plt.subplot(3,3,9)
    draw1(6,'South America',df)

    plt.tight_layout(pad=6)
    # plt.show()
    plt.savefig('population-area vs. year(after 1700AD).png',bbox_inches='tight')

def p8():
    def draw1(number,name,df):
        plt.title('land/area vs. year(after 1700AD)'+'('+str(name)+')')
        sns.despine()
        plt.grid(axis="y")
        sns.lineplot(x="year", y="cropland" + str(number), data=df, label='cropland/area')
        sns.lineplot(x="year", y="tot_rainfed" + str(number), data=df, label='tot_rainfed/area')
        sns.lineplot(x="year", y="tot_irri" + str(number), data=df, label='tot_irri/area')
        plt.ylabel('land/area')
        sns.distplot()
        plt.legend()
        y = range(0,len(df),5)
        plt.xticks(y,rotation=60)

    df = pd.read_excel('popu_data4.xlsx')
    df = df
    plt.rcParams['figure.figsize'] = (30.0, 16.0)

    plt.subplot(3,3,1)
    draw1(0,'global',df)
    plt.subplot(3,3,4)
    draw1(1,'Africa',df)
    plt.subplot(3,3,5)
    draw1(2,'Asia',df)
    plt.subplot(3,3,6)
    draw1(3,'Australia',df)
    plt.subplot(3,3,7)
    draw1(4,'Europe',df)
    plt.subplot(3,3,8)
    draw1(5,'North America',df)
    plt.subplot(3,3,9)
    draw1(6,'South America',df)

    plt.tight_layout(pad=6)
    # plt.show()
    plt.savefig('land-area vs. year(after 1700AD).png',bbox_inches='tight')

p8()



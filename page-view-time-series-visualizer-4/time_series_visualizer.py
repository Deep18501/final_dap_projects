import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df['date'] = pd.to_datetime(df['date'])
df.set_index('date',inplace=True)


# Clean data
# print(df.shape)
top=np.percentile(df['value'],97.5)
low=np.percentile(df['value'],2.5)
df = df[(df['value']<=top)&(df['value']>=low)]

# print(df)

def draw_line_plot():
    # Draw line plot
    fig,ax=plt.subplots(figsize=(32,10))
    sns.lineplot(data=df,x='date',y='value')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date',fontsize=22)
    plt.ylabel('Page Views',fontsize=22)
    # plt.show()
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['month']=df.index.month
    df_bar['year']=df.index.year
    # print(df_bar)
    # Draw bar plot
    fig,ax=plt.subplots(figsize=(10,8))
    sns.barplot(data=df_bar,x='year',y='value',hue='month',edgecolor='black')
    # plt.show()
    plt.title('Months')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    # ax.set_xticks(range(1, 13))
    plt.legend(labels=month_names,fontsize='large')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig,(ax1,ax2)=plt.subplots(1,2,figsize=(29,11))
    sns.boxplot(data=df_box,x=df_box['year'],y=df_box['value'],ax=ax1)
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(data=df_box,x=df_box['month'],y=df_box['value'],ax=ax2,order=month_names)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax1.set_ylabel('Page Views')
    ax2.set_ylabel('Page Views')
    ax2.set_xlabel('Month')
    ax1.set_xlabel('Year')
    
    
    
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

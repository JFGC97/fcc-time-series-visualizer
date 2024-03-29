import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df=pd.read_csv('fcc-forum-pageviews.csv',index_col='date')

# Clean data
df=df[(df['value']>=df['value'].quantile(0.025)) & (df['value']<= df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(20, 6))
    ax = plt.plot(df.index, df['value'])
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    fig.savefig('line_plot.png')
  
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
      df_bar=df.copy(deep=True)
      df_bar['Year']=pd.DatetimeIndex(df_bar.index).year
      df_bar['Month']=pd.DatetimeIndex(df_bar.index).month
      df_bar = df_bar.groupby(['Year','Month'])['value'].mean().reset_index().sort_values(by=['Year','Month'])
      df_bar = df_bar.set_index('Year')
      df_bar = df_bar.pivot_table(values = 'value', index=df_bar.index, columns='Month', aggfunc='first').reset_index()
      df_bar = df_bar.set_index('Year')
      df_bar.columns = ['January','February','March','April','May','June','July','August','September','October','November','December']
      df_bar=df_bar.fillna(0)
  
    # Draw bar plot
      fig, ax = plt.subplots()
      df_bar.plot.bar(rot=0,ax=ax)
      plt.xlabel('Year')
      plt.ylabel('Average Page Views')

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
    fig, (ax, ax1) = plt.subplots(1,2)
    fig.set_figheight(10)
    fig.set_figwidth(20)
  
    sns.boxplot(df_box,x='year',y='value', ax=ax)
    ax.set_title("Year-wise Box Plot (Trend)")
    ax.set_xlabel("Year")
    ax.set_ylabel("Page Views")
  
    Order_month=['jan','Fev','Mar','Apr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dec']
  
    sns.boxplot(ax=ax1, x="month", y= "value", data=df_box, order = Order_month) 
    ax1.set_title("Month-wise Box Plot (Seasonality)")
    ax1.set_xlabel("Month")
    ax1.set_ylabel("Page Views"
                   
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

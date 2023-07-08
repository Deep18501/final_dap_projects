import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')
    
    

    # Create scatter plot
    plt.scatter(x=df['Year'],y=df['CSIRO Adjusted Sea Level'])
    # Create first line of best fit
    x_values= pd.Series(range(df['Year'].min(), 2051))

  
    res=linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    plt.plot(x_values,(res.intercept+(res.slope*x_values)),color='r')
    # Create second line of best fit
    df_filtered = df[df['Year'] >= 2000]
    res2 = linregress(x=df_filtered['Year'], y=df_filtered['CSIRO Adjusted Sea Level'])
    x_values2 = pd.Series(range(df_filtered['Year'].min(), 2051))
    plt.plot(x_values2,(res2.intercept+(res2.slope*x_values2)),color='g')
    # plt.show()



    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')
# Add 'overweight' column
# print(len(df))
ov=(df['weight']/(df['height']**2))*10000
# print(ov)
overrt=np.zeros(len(df))
for i in range(len(overrt)) :
  if ov[i]>25 :
    overrt[i]=1
  else :
    overrt[i]=0

ovSeries=pd.Series(overrt)
df['overweight'] = ovSeries


# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.


def cal(x):
  if x<=1:
    return 0
  else :
    return 1


df['cholesterol']=df['cholesterol'].transform(lambda x : cal(x))
df['gluc']=df['gluc'].transform(lambda x : cal(x))
                    
# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
  
    
    melted_df=pd.melt(df,id_vars='cardio',value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'],var_name='variable')
    
    df_cat = melted_df
    # print(df_cat)


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    # df_cat = None
    

    # Draw the catplot with 'sns.catplot()'
    sns.set_theme(style="ticks")
    catplot=sns.catplot(
      data=df_cat,
      x='variable',
      y=None,
      hue='value',
      order=['active','alco','cholesterol','gluc','overweight','smoke'],
      col='cardio',
      kind='count',
      legend=True,
      legend_out=True
    )
    catplot.set_axis_labels('variable', 'total')
    catplot.fig.suptitle('Catplot')
    # plt.tight_layout(rect=[0, 0, 1, 0.95])
    # plt.show()
    # Get the figure for the output
    fig = catplot.fig
    # Do not modify the next two lines
    fig.savefig('catplot.png')    
    return fig

# Draw Heat Map

def draw_heat_map():
    # Clean the data
    
    df_clean=df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025))& (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025))& (df['weight'] <= df['weight'].quantile(0.975))]

# Reset the index of the cleaned data
  
    # sns.boxplot(df,y='sex')  
    # plt.show()
    # print(df.describe())
    
    df_heat = df_clean.reset_index(drop=True,inplace=True)


    # Calculate the correlation matrix
    corr = df_clean.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr,dtype=bool))
  
   


    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))

    # Draw the heatmap with 'sns.heatmap()'
    # cmap = sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(corr,mask=mask,annot=True,ax=ax,fmt='.1f',vmin=-0.16, vmax=0.32,cbar_kws={'ticks': [-0.08, 0.00, 0.08, 0.16, 0.24]})

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

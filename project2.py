import project1
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


#please use my latest version of project1, upload with project2
df2 = project1.df2('supply_tables_1997-2020.xlsx')
df1 = project1.df1('supply_tables_1997-2020.xlsx')

subjects = ['Tax on products','Subsidies','Total tax less subsidies on products']
subjects_2 = ['Machinery','Computer and electronic products','Electrical equipment, appliances, and components','Motor vehicles, bodies and trailers, and parts']

#use the list subjects above, and industry here is 'Total industry supply'
def problem_01(subjects,industry):
    fig, ax = plt.subplots()
    for subject in subjects:
        df_subject = df1[(df1['commodity'] == subject) & (df1['industry'] == industry)]
        ax.plot(df_subject['year'], df_subject['value'], label=subject)

    ax.set_xlabel('Year')
    ax.set_ylabel('Value')
    ax.set_title('Change in Value of Total tax and subsidies')

    ax.legend()

    plt.savefig('project2-1.png')
    plt.show()
    plt.close()
    
#dimension is a string in industry column, my choices are 'Pipeline transportation', 'Oil and gas extraction'
def problem_02(dimension1, dimension2):
    df_filtered = df1[df1['industry'].isin([dimension1, dimension2]) & (df1['commodity'] == 'Total product supply (purchaser prices)')]

    df_pivot = df_filtered.pivot(index='year', columns='industry', values='value')
    df_pivot[dimension1] = df_pivot[dimension1].astype(float)
    df_pivot[dimension2] = df_pivot[dimension2].astype(float)

    sns.lmplot(x=dimension1, y=dimension2, data=df_pivot)

    plt.title(f'Scatter plot of Value of {dimension1} vs {dimension2} with Regression Line')
    plt.savefig('project2-2.png')
    plt.show()
    plt.close() 
    
    
    
#use the list subjects_2 above, and commodity here is 'Imports', the explanation of MCIF
def problem_03(subjects_2, commodity):
    fig, ax = plt.subplots()
    for subject in subjects_2:
        df_subject = df1[(df1['industry'] == subject) & (df1['commodity'] == commodity)]
        ax.plot(df_subject['year'], df_subject['value'], label=subject)

    ax.set_xlabel('Year')
    ax.set_ylabel('Value')
    ax.set_title('Change in Value of MCIF of manufactory')

    ax.legend()

    plt.savefig('project2-3.png')
    plt.show()
    plt.close()
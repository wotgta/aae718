import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def readcsv(filename):
    df = pd.read_csv(filename)
    return df

def problem_01(filename):
    df1 = readcsv(filename)
    
    plt.scatter(df1['Height(Inches)'], df1['Weight(Pounds)'])
    plt.xlabel('Height')
    plt.ylabel('Weight')
    plt.title('Scatter plot of Weight vs Height')
    plt.savefig('hwk5-1-1.png')
    plt.show()
    plt.close()  
    
    #seaborn
    sns.scatterplot(x='Height(Inches)', y='Weight(Pounds)', data=df1)
    plt.title('Scatter plot of Weight vs Height')
    plt.savefig('hwk5-1-2.png')
    plt.show()
    plt.close() 
    
    
def problem_02(filename):
    df1 = readcsv(filename)
    
    fig, axs = plt.subplots(1, 2)
    axs[0].hist(df1['Height(Inches)'], bins=20, color='b', alpha=0.7)
    axs[0].set_title('Height')

    axs[1].hist(df1['Weight(Pounds)'], bins=20, color='b', alpha=0.7)
    axs[1].set_title('Weight')

    plt.savefig('hwk5-2-1.png')
    plt.show()
    plt.close() 
    
    #seaborn
    fig, axs = plt.subplots(1, 2)

    sns.histplot(df1['Height(Inches)'], bins=20, color='b', ax=axs[0])
    axs[0].set_title('Height')
    axs[0].set_ylabel('Count')

    sns.histplot(df1['Weight(Pounds)'], bins=20, color='b', ax=axs[1])
    axs[1].set_title('Weight')
    axs[1].set_ylabel('Count')

    plt.savefig('hwk5-2-2.png')
    plt.show()
    plt.close() 
    
    std_height = df1['Height(Inches)'].std()
    std_weight = df1['Weight(Pounds)'].std()
    std = {}
    std['Standard Deviation of Height'] = std_height
    std['Standard Deviation of Weight'] = std_weight
    return std
    
def problem_03(filename):
    df1 = readcsv(filename)
    
    sns.lmplot(x='Height(Inches)', y='Weight(Pounds)',data=df1, line_kws={'color': 'blue'}, scatter_kws={'color': 'blue'})

    plt.title('Scatter plot of Weight vs Height with regression line and confidence interval')


    plt.savefig('hwk5-3.png')
    plt.show()
    plt.close() 
    
def problem_04(filename):
    df2 = readcsv(filename)
    
    plt.figure(figsize=(10, 5))
    plt.plot(df2['month_number'], df2['total_profit'])
    plt.xlabel('Month')
    plt.ylabel('Total Profit')
    plt.title('Total Profit Over Time')

    plt.savefig('hwk5-4-1.png')
    plt.show()
    plt.close() 
    
    #2
    products = df2.columns.drop(['month_number', 'total_profit'])

    plt.figure(figsize=(10, 5))
    for product in products:
        plt.plot(df2['month_number'], df2[product], label=product)

    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.title('Sales of Each Product Over Time')
    plt.legend()

    plt.savefig('hwk5-4-2.png')
    plt.show()
    plt.close() 
    
    #3
    plt.figure(figsize=(10, 5))
    sns.lmplot(x='facecream', y='facewash', data=df2, line_kws={'color': 'blue'})

    plt.xlabel('FaceCream Sales')
    plt.ylabel('FaceWash Sales')
    plt.title('Relationship Between FaceCream and FaceWash Sales')
    plt.savefig('hwk5-4-3.png')
    plt.show()
    plt.close() 
    
def problem_05(filename):
    df3 = readcsv(filename) 
    
    subjects = df3['SUBJECT'].unique()
    
    #1
    fig, ax = plt.subplots()
    for subject in subjects:
        df_subject = df3[(df3['SUBJECT'] == subject) & (df3['LOCATION'] == 'OECD') & (df3['MEASURE'] == 'THND_TONNE')]
        ax.plot(df_subject['TIME'], df_subject['Value'], label=subject)

    ax.set_xlabel('Year')
    ax.set_ylabel('Value')
    ax.set_title('Change in Value of Each Subject Over Time:OECD/THND_TONNE')

    ax.legend()

    plt.savefig('hwk5-5-1.png')
    plt.show()
    plt.close()
    
    #2
    fig, ax = plt.subplots()
    for subject in subjects:
        df_subject = df3[(df3['SUBJECT'] == subject) & (df3['LOCATION'] == 'OECD') & (df3['MEASURE'] == 'THND_HA')]
        ax.plot(df_subject['TIME'], df_subject['Value'], label=subject)

    ax.set_xlabel('Year')
    ax.set_ylabel('Value')
    ax.set_title('Change in Value of Each Subject Over Time:OECD/THND_HA')

    ax.legend()

    plt.savefig('hwk5-5-2.png')
    plt.show()
    plt.close()
    
    #3
    fig, ax = plt.subplots()
    for subject in subjects:
       df_subject = df3[(df3['SUBJECT'] == subject) & (df3['LOCATION'] == 'WLD') & (df3['MEASURE'] == 'THND_TONNE')]
        ax.plot(df_subject['TIME'], df_subject['Value'], label=subject)

    ax.set_xlabel('Year')
    ax.set_ylabel('Value')
    ax.set_title('Change in Value of Each Subject Over Time:WLD/THND_TONNE')

    ax.legend()

    plt.savefig('hwk5-5-3.png')
    plt.show()
    plt.close()
    
    #4
    fig, ax = plt.subplots()
    for subject in subjects:
        df_subject = df3[(df3['SUBJECT'] == subject) & (df3['LOCATION'] == 'WLD') & (df3['MEASURE'] == 'THND_HA')]
        ax.plot(df_subject['TIME'], df_subject['Value'], label=subject)

    ax.set_xlabel('Year')
    ax.set_ylabel('Value')
    ax.set_title('Change in Value of Each Subject Over Time:WLD/THND_HA')

    ax.legend()

    plt.savefig('hwk5-5-4.png')
    plt.show()
    plt.close()
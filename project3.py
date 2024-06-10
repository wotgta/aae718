import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import os
import copy
import seaborn as sns


def first_two_graph(file):
    df1 =  pd.read_csv(file, parse_dates = ["DATE"], date_format = '%Y-%m-%d')
    df1 = df1.set_index("DATE")

    df1 = df1[(df1['NAME'] == 'KUNMING, CH') | (df1['NAME'] == 'MIAMI BEACH, FL US')]
    df1_t = df1[df1['TMAX'].notna()]


    #first graph
    kunming_data = df1_t[df1_t['NAME'] == 'KUNMING, CH']
    miami_data = df1_t[df1_t['NAME'] == 'MIAMI BEACH, FL US']

    plt.figure(figsize=(10, 6))
    plt.plot(kunming_data.index, kunming_data['TMAX'], label='Kunming')
    plt.plot(miami_data.index, miami_data['TMAX'], label='Miami')
    plt.title('The comparsion of max temperature neyween kunming and miami')
    plt.xlabel('Date')
    plt.ylabel('Temperature')
    plt.legend()
    plt.savefig('project3-1.png')
    plt.show()
    plt.close()

    #second graph
    df_2 = df1_t.loc[df1_t.index.year.isin([2020, 2021])]
    kunming_data2 = df_2[df_2['NAME'] == 'KUNMING, CH']
    miami_data2 = df_2[df_2['NAME'] == 'MIAMI BEACH, FL US']

    plt.figure(figsize=(10, 6))
    plt.plot(kunming_data2.index, kunming_data2['TMAX'], label='Kunming')
    plt.plot(miami_data2.index, miami_data2['TMAX'], label='Miami')
    plt.title('The comparsion of max temperature neyween kunming and miami in 2020 to 2021')
    plt.xlabel('Date')
    plt.ylabel('Temperature')
    plt.legend()
    plt.savefig('project3-2.png')
    plt.show()
    plt.close()

def last_two_graph(miami_file, chicago_file):

    df2 =  pd.read_csv(miami_file, parse_dates = ["DATE"], date_format = '%Y-%m-%dT%H:%M:%S')
    df2 = df2.set_index("DATE")

    df3 =  pd.read_csv(chicago_file, parse_dates = ["DATE"], date_format = '%Y-%m-%dT%H:%M:%S')
    df3 = df3.set_index("DATE")
    df_merge = pd.concat([df2,df3], axis=0)

    #first graph
    df_chicago = df_merge[(df_merge['Sunrise'].notna()) & (df_merge['Sunset'].notna()) & (df_merge['NAME'] == 'CHICAGO MIDWAY AIRPORT, IL US')]
    df_miami = df_merge[(df_merge['Sunrise'].notna()) & (df_merge['Sunset'].notna()) & (df_merge['NAME'] == 'MIAMI INTERNATIONAL AIRPORT, FL US')]


    plt.figure(figsize=(10, 6))
    plt.plot(df_chicago.index,df_chicago['Sunrise'], label='Sunrise chicago')
    plt.plot(df_chicago.index, df_chicago['Sunset'], label='Sunset chicago')
    plt.plot(df_miami.index,df_miami['Sunrise'], label='Sunrise miami')
    plt.plot(df_miami.index, df_miami['Sunset'], label='Sunset miami')
    plt.title('Sunrise and Sunset Times Throughout the Years')
    plt.xlabel('Date')
    plt.ylabel('Time')
    plt.legend()
    plt.savefig('project3-3.png')
    plt.show()
    plt.close()

    #second
    df_tm = df_merge[(df_merge['DailyAverageDryBulbTemperature'].notna()) & (df_merge['NAME'] == 'MIAMI INTERNATIONAL AIRPORT, FL US')].copy()
    df_tc = df_merge[(df_merge['DailyAverageDryBulbTemperature'].notna()) & (df_merge['NAME'] == 'CHICAGO MIDWAY AIRPORT, IL US')].copy()


    plt.figure(figsize=(10, 6))
    plt.plot(df_tc.index,df_tc['DailyAverageDryBulbTemperature'], label='temperature chicago')
    plt.plot(df_tm.index, df_tm['DailyAverageDryBulbTemperature'], label='temperature miami')
    plt.title('Temperature comparison')
    plt.xlabel('Date')
    plt.ylabel('temperature')
    plt.legend()
    plt.savefig('project3-4.png')
    plt.show()
    plt.close()


    #third
    df_merge['difference_t'] = df_merge['Sunset'] - df_merge['Sunrise'] 

    plt.figure(figsize=(10, 5))
    sns.lmplot(x='difference_t', y='DailyMaximumDryBulbTemperature', data=df_merge, line_kws={'color': 'blue'})

    plt.xlabel('time of the sun')
    plt.ylabel('temperature')
    plt.title('Relationship Between sun heat and temperature')
    plt.savefig('project3-5.png')
    plt.show()
    plt.close() 




#Ziyi Su
#HWK3

import csv
import copy
import pandas as pd
from pandas import Series, DataFrame
import os
from io import TextIOWrapper
import numpy as np
import matplotlib.pyplot as plt
from zipfile import ZipFile, ZIP_DEFLATED

#p1
def methane(path): 
    try:
        os.chdir(path)
        df = pd.read_csv('Methane_final.csv')
        df.drop('Unnamed: 0', axis=1, inplace=True)
        return df
    except SyntaxError:
        print("SyntaxError: (unicode error) unicodeescape codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape, use r at the front like r'C:\Users\ziyi Su\aae718'")
        
def methane_aggregation(path):
    df = methane(path)
    
    region_sum = df[(df['region'] != 'World') & (df['type'] == 'Agriculture')]['emissions'].sum()
    world_sum = df[(df['region'] == 'World') & (df['type'] == 'Agriculture')]['emissions']
    delta = region_sum - world_sum
    
    return df and delta 

def problem_03(): 
    subset = df[(df['region'] != 'World') & (df['type'] == 'Agriculture')]
    unique = np.array(subset['segment'].unique())
    return unique

def region_mean():
    averages = df.groupby('region')['emissions'].mean().reset_index()   
    averages.columns = ['region', 'average_emissions']
    
    fig, ax = plt.subplots(1, 1)
    table_data = []
    for row in averages.itertuples(index=False):
        table_data.append(row)
    table = ax.table(cellText=table_data, colLabels=averages.columns, loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)
    ax.axis('off')
    plt.savefig("hwk3_plot1.png")
    
    return averages

def region_total_mean():
    average = df[df['segment'] != 'Total'].groupby('region')['emissions'].mean().reset_index()
    average.columns = ['region', 'average_emissions']
    
    fig, ax = plt.subplots(1, 1)
    table_data = []
    for row in average.itertuples(index=False):
        table_data.append(row)
    table = ax.table(cellText=table_data, colLabels=averages.columns, loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)
    ax.axis('off')
    plt.savefig("hwk3_plot2.png")
    
    return average

def methane_graphs():
    #1
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='emissions', y='region', data=df)
    plt.tick_params(axis='x', labelsize=14)
    plt.title('Boxplot of Emissions Aggregated by Region')
    plt.savefig('boxplot1.png')
    plt.show()
    plt.close()
    
    #2
    df_no_world = df[df['region'] != 'World']
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='emissions', y='region', data=df_no_world)
    plt.title('Boxplot of Emissions by Region Excluding World')
    plt.savefig('boxplot2.png')
    plt.show()
    plt.close()
    
    #3
    df_total = df_no_world[df_no_world['segment'] == 'Total']
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='emissions', y='region', data=df_total)
    plt.title('Boxplot of Total Emissions by Region Excluding World and only total')
    plt.savefig('boxplot3.png')
    plt.show()
    plt.close
    
    #4
    df_no_world_total = df_no_world[df_no_world['segment'] != 'Total']
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='emissions', y='region', data=df_no_world_total)
    plt.title('Boxplot of Emissions by Segment Excluding World and Total')
    plt.savefig('boxplot4.png')
    plt.show()
    plt.close()
    
    #5
    df_agriculture = df_no_world[df_no_world['type'] == 'Agriculture']
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='emissions', y='region', data=df_agriculture)
    plt.title('Boxplot of Emissions for Agriculture type by Region')
    plt.savefig('boxplot5.png')
    plt.show()
    plt.close()
    
def animal_crossing(path):
    inner = 'Animal_Crossing'
    csv_file = 'accessories.csv'
    try:
        with ZipFile(path, 'r') as zf:
            file_path = f'{inner}/{csv_file}'
            with zf.open(file_path) as f:
                rd = pd.read_csv(f)
        return rd
    except FileNotFoundError:
        print("the input path need to be stop by the zip file like r'C:\Users\ziyi Su\aae718\Animal_Crossing.zip'")
        
def sell_price():
    a = rd['Sell'].sort_values(ascending=[False]).index[0]
    assert rd['Sell'].sort_values(ascending=[False]).iloc[0] != rd['Sell'].sort_values(ascending=[False]).iloc[1]
    
    result = rd['Name'].iloc[a]
    return result

def smallest_diff():
    b = {}
    #caculate the difference
    for i in range(len(rd)):
        try:
            c = int(rd.iloc[i]['Buy']) - int(rd.iloc[i]['Sell'])
            b[i] = c
        except ValueError:
            continue
    #find the index of the smallest
    mi = int(rd['Sell'].sort_values(ascending=[False]).iloc[0])
    for i in b:
        if b[i] < mi:
            mi = b[i]
            number = i
    #find any index that has the same smallest price     
    list1 = []
    list1.append(number)
    for i in b:
        if b[i] == b[number]:
            if i != number:
                list1.append(i)
    #get the name
    result = []
    for i in list1:
        if rd.iloc[i]['Name'] not in result:
            result.append(rd.iloc[i]['Name'])
    return result
            
    

    
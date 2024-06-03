import os
import csv
import copy
import pandas as pd
from pandas import Series, DataFrame
import copy
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import TextIOWrapper

def csv_files(directory):

    file_path = os.path.join(directory)
    files = [file for file in os.listdir(file_path) if file.endswith('.csv')]
    return files


def load_emission_csv(path, string):

    with open(path) as f:
        rd = pd.read_csv(f)
    rd.insert(loc=0, column='year', value=string)
    return rd


def load_emissions(directory):
    files = csv_files(directory)

    for file in files:
        file_path = f'{directory}/{file}'
        df = load_emission_csv(file_path, file.split('.')[0])
    
        if file.split('.')[0] == '1970':
            df1 = df.copy(deep=True)
        else:
            df1 = pd.concat([df1,df], axis=0, ignore_index=True)
    return df1


def problem_04(directory, country_path):
    df1 = load_emissions(directory)

    with open(country_path) as f:
        rd = pd.read_csv(f)
    rd.rename(columns={'name':'Country'}, inplace = True)
    
    merged_df = pd.merge(rd[['Country','alpha-2','region','sub-region']],df1)
    return merged_df


def problem_05(directory, country_path):
    
    merged_df = problem_04(directory, country_path)
    
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Ratio.Per Capita', y='sub-region', data=merged_df[(merged_df['region'] == 'Asia') & (merged_df['year'] == '2010')])
    plt.tick_params(axis='x', labelsize=14)
    plt.title('Boxplot of Ratio.Per Capita by sub-Region in asia')
    plt.savefig('hwk4_boxplot1.png')
    plt.show()
    plt.close()
    
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Ratio.Per Capita', y='sub-region', data=merged_df[(merged_df['region'] == 'Europe') & (merged_df['year'] == '2010')])
    plt.tick_params(axis='x', labelsize=14)
    plt.title('Boxplot of Ratio.Per Capita by sub-Region in Europe')
    plt.savefig('hwk4_boxplot2.png')
    plt.show()
    plt.close()
    
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Ratio.Per Capita', y='sub-region', data=merged_df[(merged_df['year'] == '2010')])
    plt.tick_params(axis='x', labelsize=14)
    plt.title('Boxplot of Ratio.Per Capita by sub-Region')
    plt.savefig('hwk4_boxplot3.png')
    plt.show()
    plt.close()
    
    
        
def dirty_data(path):
    
    with open(path) as f:
        dd = pd.read_csv(f,header=[0,1],index_col=0)
    dd = dd.reset_index()
        
    dd1 = pd.melt(dd, id_vars=['Order ID'], var_name=['Segment','Ship Mode'], value_name='Sales')
        
    dd1.loc[dd1['Segment'].str.contains('Unnamed: 2|Unnamed: 3|Unnamed: 4'), 'Segment'] = 'Consumer'
    dd1.loc[dd1['Segment'].str.contains('7|8|9'), 'Segment'] = 'Corporate'
    dd1.loc[dd1['Segment'].str.contains('12|13|14'), 'Segment'] = 'Home Office'
    
    dd1 = dd1.dropna(subset=['Sales'])
    
    dd1 = dd1.reset_index()
    dd1.drop('index',axis=1,inplace = True)
    rows_to_drop = []
    
    for i in range(len(dd1)):
        if 'Total' in dd1.iloc[i]['Segment'] or 'Total' in dd1.iloc[i]['Order ID']:
            rows_to_drop.append(i)
            
    dd1 = dd1.drop(rows_to_drop).reset_index()
    dd1.drop('index',axis=1,inplace = True)
    
    return dd1


def school_data(path):
    col_names = ['FIPS State code', 'District ID', 'District Name', 'Total Population', 
             'Population of Relevant Children 5 to 17 years of Age', 
             'Estimated Number of Relevant Children 5 to 17 years old in Poverty Related to the Householder', 
             'Tag']

    col_widths = [2, 6, 72, 10, 10, 8, 21]

    with open(path, 'rb') as file:
        df = pd.read_fwf(TextIOWrapper(file), widths=col_widths, names=col_names)
        
    return df
        
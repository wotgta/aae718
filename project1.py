import os
import pandas as pd
import copy




def parse_xls(filename,year):
    xl = pd.ExcelFile(filename)
    df = xl.parse(str(year))
    return df

def df2(filename):
    df = parse_xls(filename,'1997')
    
    df2 = df.iloc[6:, 0:2]
    df2.columns = ['nacis_code', 'description']
    
    df2.reset_index(inplace=True)
    df2.drop('index',axis=1,inplace = True)
    
    return df2

def df1(filename):
    df22 = df2(filename)
    for ii in range(1997,2021):
        df = parse_xls(filename,ii)
        for i in range(6,len(df)):
            merged_df = pd.concat([df.iloc[5], df.iloc[i]], axis=1)
    
            merged_df.drop([df.columns[0],'Unnamed: 1'], inplace=True)
            merged_df.reset_index(inplace=True)
            merged_df.drop('index',axis=1,inplace = True)
            merged_df.columns = ['commodity','value']
    
            merged_df.insert(loc=0, column='industry', value= df22.iloc[i-6]['description'])
            merged_df.insert(loc=0, column='year', value=ii)
    
            if i == 6 and ii == 1997:
                df1 = merged_df.copy(deep=True)
            else:
                df1 = pd.concat([df1,merged_df], axis=0, ignore_index=True)
                
    for i in range(len(df1)):
        if type(df1.iloc[i]['value']) == str:
            df1.loc[i, 'value'] = 0
            
    return df1
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import os
import copy

def p1_p5csv(file):
    df1 =  pd.read_csv(file, parse_dates = ["DATE"], date_format = '%Y-%m-%dT%H:%M:%S')
    df1 = df1.set_index("DATE")
    return df1


def problem_01(file):
    df1 =  p1_p5csv(file)

    df_snow = df1[df1['DailySnowDepth'].notna()].copy()
    df_snow['DailySnowDepth'] = pd.to_numeric(df_snow['DailySnowDepth'], errors='coerce')
    df_snow = df_snow[df_snow['DailySnowDepth'].notna()]

    df_snow.plot(y='DailySnowDepth')
    plt.savefig('hwk8-1.png')
    plt.show()
    plt.close() 

def problem_02(file):
    df1 =  p1_p5csv(file)

    df_sun = df1[(df1['Sunrise'].notna()) & (df1['Sunset'].notna())]

    plt.figure(figsize=(10, 6))
    plt.plot(df_sun.index,df_sun['Sunrise'], label='Sunrise')
    plt.plot(df_sun.index, df_sun['Sunset'], label='Sunset')
    plt.title('Sunrise and Sunset Times Throughout the Year')
    plt.xlabel('Date')
    plt.ylabel('Time')
    plt.legend()
    plt.savefig('hwk8-2.png')
    plt.show()
    plt.close() 

def problem_03(file):
    df1 =  p1_p5csv(file)

    df_p = df1[df1['DailyPrecipitation'].notna()].copy()
    df_p.loc[:,'DailyPrecipitation'] = pd.to_numeric(df_p['DailyPrecipitation'], errors='coerce')
    df_p['DailyPrecipitation'] = df_p['DailyPrecipitation'].fillna(0)
    df_p.loc[:,'rolling_avg'] = df_p['DailyPrecipitation'].rolling(window=7).mean()
    df_p['rolling_avg'] = df_p['rolling_avg'].fillna(0)

    plt.figure(figsize=(10, 5))
    plt.plot(df_p.index, df_p['rolling_avg'], label='Rolling Average')
    plt.xlabel('Date')
    plt.ylabel('Average Precipitation')
    plt.title('Weekly Rolling Average of Precipitation')
    plt.legend()
    plt.savefig('hwk8-3.png')
    plt.show()
    plt.close()

def problem_04(file):
    df1 =  p1_p5csv(file)

    df_t = df1[(df1['HourlyDewPointTemperature'].notna()) & (df1['HourlyDryBulbTemperature'].notna())].copy()
    df_t['difference'] = df_t['HourlyDewPointTemperature'] - df_t['HourlyDryBulbTemperature']

    plt.figure(figsize=(10, 6))
    plt.plot(df_t.index,df_t['HourlyDewPointTemperature'], label='HDT')
    plt.plot(df_t.index, df_t['HourlyDryBulbTemperature'], label='HDBT')
    plt.title('difference of two temperature meaure ways')
    plt.xlabel('Date')
    plt.ylabel('temperature')
    plt.legend()
    plt.savefig('hwk8-4-1.png')
    plt.show()
    plt.close()

    plt.figure(figsize=(10, 6))
    plt.plot(df_t.index,df_t['difference'], label='diff')
    plt.title('difference of two temperature meaure ways')
    plt.xlabel('Date')
    plt.ylabel('temperature')
    plt.legend()
    plt.savefig('hwk8-4-2.png')
    plt.show()
    plt.close()

def problem_05(file):
    df1 =  p1_p5csv(file)

    df_hl = df1[(df1['DailyMaximumDryBulbTemperature'].notna()) & (df1['DailyMinimumDryBulbTemperature'].notna())].copy()

    plt.figure(figsize=(10, 6))
    plt.plot(df_hl.index,df_hl['DailyMaximumDryBulbTemperature'], label='max')
    plt.plot(df_hl.index, df_hl['DailyMinimumDryBulbTemperature'], label='min')
    plt.title('Daily max and min temperature in 2020')
    plt.xlabel('Date')
    plt.ylabel('temperature')
    plt.legend()
    plt.savefig('hwk8-5.png')
    plt.show()
    plt.close()

def bike_data(file):
    df2 = pd.read_csv(file, parse_dates=['started_at', 'ended_at'])

    df2['Duration'] = df2['ended_at'] - df2['started_at']
    df2['DurationMinutes'] = df2['Duration'].dt.total_seconds() / 60

    df_test = df2[['ride_id','rideable_type','started_at','ended_at','member_casual']]

    for column in df_test.columns:
        assert df_test[column].notna().all(), f"The column {column} contains NaN values"

    return df2

def problem_08(file):
    df2 = bike_data(file)

    rider_bike_counts = df2.groupby(['rideable_type', 'member_casual']).size().unstack()

    rider_bike_counts.plot(kind='bar', stacked=True)
    plt.xlabel('Rider Type')
    plt.ylabel('Count')
    plt.title('Comparison of Bike Types Used by Members vs Casual Riders')
    plt.savefig('hwk8-8.png')
    plt.show()
    plt.close()

def problem_09(file):
    df2 = bike_data(file)

    avg_durations = df2.groupby([df2['started_at'].dt.day_name(), 'rideable_type'])['DurationMinutes'].mean().unstack()
    avg_durations.plot(kind='bar', stacked=False)
    plt.xlabel('Day of the Week')
    plt.ylabel('Average Trip Duration (minutes)')
    plt.title('Average Trip Duration by Day of the Week for Each Rider Type')
    plt.savefig('hwk8-9-1.png')
    plt.show()
    plt.close()

    df_nd = df2[df2['rideable_type'] != 'docked_bike'].copy()
    avg = df_nd.groupby([df_nd['started_at'].dt.day_name(), 'rideable_type'])['DurationMinutes'].mean().unstack()
    avg.plot(kind='bar', stacked=False)
    plt.xlabel('Day of the Week')
    plt.ylabel('Average Trip Duration (minutes)')
    plt.title('Average Trip Duration by Day of the Week for Each Rider Type without dock type')
    plt.savefig('hwk8-9-2.png')
    plt.show()
    plt.close()

    num_trip = df2.groupby([df2['started_at'].dt.day_name(), 'rideable_type']).size().unstack()
    num_trip.plot(kind='bar', stacked=False)
    plt.xlabel('Day of the Week')
    plt.ylabel('Number of Trips')
    plt.title('Number of Trips by Day of the Week for Each Rider Type')
    plt.savefig('hwk8-9-3.png')
    plt.show()
    plt.close()


def problem_10(file):
    df2 = bike_data(file)

    num_trip = df2.groupby([df2['started_at'].dt.day, 'rideable_type']).size().unstack()
    num_trip.plot(kind='bar', stacked=False)
    plt.xlabel('Day of the Month')
    plt.ylabel('Number of Trips')
    plt.title('Number of Trips by Day of the Month for Each Rider Type')
    plt.savefig('hwk8-10-3.png')
    plt.show()
    plt.close()


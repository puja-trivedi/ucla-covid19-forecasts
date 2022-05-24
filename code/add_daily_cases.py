import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='adds daily_cases col, daily_deaths col, and daily_deaths/daily_cases col to csv created by get_historical_data.py')
parser.add_argument('-f', '--file_name', required=True, help='name of csv file produced by get_historical_data.py')
args = parser.parse_args()

# load data from .csv to df
df = pd.read_csv(args.file_name,  dtype=str)

# convert data from 'str' to 'int'
df['cases'] = df['cases'].astype(int)
df['deaths'] = df['deaths'].astype(int)

# calculate and create new columns for daily cases and daily deaths
df['daily_cases'] = (df['cases'].shift(-1) - df['cases']).shift(1)
df['daily_deaths'] = (df['deaths'].shift(-1) - df['deaths']).shift(1)

# calculate the ratio of inc.deaths/inc.cases 
df['ratio_dth_case'] = df['daily_deaths']/df['daily_cases']

# remove first row 
df = df.iloc[1:]

# save new df 
df.to_csv(args.file_name,index=False)
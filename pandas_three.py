#!/bin/python3
import pandas as pd

df_meteorites = pd.read_csv('csv_files/Meteorite_Landings.csv')

# To get the first 5 data
head = df_meteorites.head()

# To get the last 5 data
tail = df_meteorites.tail()

# To get a random list of data
sample = df_meteorites.sample(5)

# To get the number of rows and colums of the data base
shape = df_meteorites.shape
shape_result = f'Rows: {shape[0]} | Columns: {shape[1]}'

# To get the size of the df
size_df = f'Size of df: {df_meteorites.size}'

# Get description of the data frame
pd.options.display.float_format = '{:,.1f}'.format()
describe = df_meteorites.describe()


breakpoint()

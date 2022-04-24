#!/bin/python3
import pandas as pd
# Learning pandas

# This is one series
sr = pd.Series([10, 9, 8, 7])
# To get the values of series is with
print(f'Values of series: {sr.values}')

# Get the index of the series
print(f'Index of series: {sr.index}')

# Get the dimension of the elements
print(f'Shape of series: {sr.shape}')

# Get data specific by index
print(sr[[0, 1, 2, 3]])

sr_new_index = pd.Series([10, 9, 8, 7], index=['a', 'b', 'c', 'd'])
print(sr_new_index)

# Get data from specific index in other index
print(sr[0:4], 2)

breakpoint()
breakpoint()

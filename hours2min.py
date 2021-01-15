'''
Input: .csv folder with datetime column
Output: a column with hours converted into minutes
'''

import numpy as np #used to import mathematical operations
import pandas as pd #import data sets and manage data sets

#read the csv file
dataset = pd.read_csv('file_name.csv')

#to take input as time value
dataset['column name'] = pd.to_datetime(dataset['column name'], errors='coerce',format='%H:%M:%S')

#function to convert hours:min:sec to minutes
def hourTomin(col_name):
    time = pd.DatetimeIndex(col_name)
    min = time.hour * 60 + time.minute
    return min

#calling the function
me_1 = hourTomin(dataset['column name'])

#function to remove nan from the data
def con_nan_zero(col):
    col = np.where(np.isnan(col), 0, col)
    return col

#calling nan function
me_1 = con_nan_zero(me_1)


#to save this column into .csv we need to convert it to string format
me_1 = me_1.astype(str)


#save into the csv file
import csv
import os
with open("new_file_name.csv", "w") as csv_file:   
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(("col1","col2","col3"))
    level_counter = 0
    max_levels = #number of rows
    while level_counter < max_levels:
    	writer.writerow((col1[level_counter],col2[level_counter],col3[level_counter])) 
      level_counter = level_counter +1 

dataset = pd.read_csv('new_file_name.csv')

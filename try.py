import pandas as pd
import os
import numpy as np
import psycopg2

df = pd.read_csv('df.csv')
df.head()
# df.to_csv(r'/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline/job_indeed.csv')
df=df.loc[:, ~df.columns.str.contains('^Unnamed')]
# df.drop('Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2', axis=1, inplace=True)
print(df)

cwd = os.getcwd()
print(cwd)

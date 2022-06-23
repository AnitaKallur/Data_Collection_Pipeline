import pandas as pd
import os
import numpy as np
import psycopg2

df = pd.read_csv('job_indeed.csv')
df.to_csv('df.csv')
df.to_csv(r'/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline/job_indeed.csv')
print(df)

cwd = os.getcwd()
print(cwd)

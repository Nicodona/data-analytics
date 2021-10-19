import pandas
import pandas as pd
import numpy as np
import matplotlib as plt

df = pd.read_csv('/home/nicodona/Desktop/08_gap-every-five-years.csv', sep='\t')
# print(df)
# # print(df.shape) #prints the number of rows followed by number of columes
# print(df.head) # prints the first 5 columns print(df.tail) can also be used
print(df.columns) # prints the columns headers or headings
print(df.dtypes) # prints all the columes and the datatypes of each
import pandas
import pandas as pd
import numpy as np
import matplotlib as plt

df = pd.read_csv('/home/nicodona/Desktop/08_gap-every-five-years.csv', sep='\t')
# print(df)
# # print(df.shape) #prints the number of rows followed by number of columes
# print(df.head) # prints the first 5 columns print(df.tail) can also be used
# print(df.columns) # prints the columns headers or headings
# print(df.dtypes) # prints all the columes and the datatypes of each
# print(df.info()) # prints more infos
# country_df = df['country']
# print(country_df)

# subset = df[['country', 'continent', 'lifeExp']]
# print(subset)
# .loc method is used to access rows and or cloumns when the columns must be specified as their headings meanwhile iloc is used to spefiy columns number too
# .iloc can take negative intergers to for both rows and columns

# print(df.loc[0]) # prints a particular row specified
# print(df.tail(n=1)) # give the data of the last row
# print(df.loc[[0, 99, 999]]) # prints selected rows
# print(df.iloc[0]) # works same as loc except that we can get the last row by using negative number
# print(df.iloc[-1])
# subs = df.loc[:, ['year', 'pop']] # prints selected columns with all rows subs = df.iloc[:, [1, 2 -1]]
# print(subs)

# print(df.loc[42, ['country']]) # produces the data at row 42 on the country row
# print(df.iloc[[0,99,999], [1,3,2]]) # proces specific rows and specific columns

# the groupby method: it helps group items using a specific criteria eg groupby year fetches all the data of that year specified by the seconfd criteria
# print(df.groupby('year')['lifeExp'].mean())

life = df.groupby('year')['lifeExp'].mean()
life.plot()


# Data vitualisation
# histogram, frequency table, frequency polygon,ogive, relative frequecy frequency ogive, pareto chart, scatter plot, graph, barchart, piechart, multiple barchart, simple pictogram

# central tendency
# it is number that is used to represent a group of numbers eg arithmetic mean
# mean ' mode, group mean, percentile etc

# dispersion
# this is the act of representing data using different motive eg range etc
#  standard devistaion is given by taking the mean and substactinfg each data item from it
# it will give a zero so the best way to analyse it is by taking the absolute value or by squaring it
#  standard deviation gives us the risk of the business while the mean gives us the beterness of the business

# WAYS TO MEASURE DISPERSION
# 1 SKEWNESS--- it can either be positively skewed (thats from the right hand side ) or negatively skewed that from left hand or not skewed
#  to know the skewness we take the S = 3(u-M/a) mean minus median divided by phi
# 2 kurtosis








#range, quartier = dividing data into 4 of 100 percentile hence 25 for q1 50 for q2 etc in this sense we can look for the percentile and the finding the quartier by taking the number from yhe percentile as the position
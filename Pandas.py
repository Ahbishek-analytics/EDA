# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 21:03:03 2018

@author: ABHI
"""

# Pandas
# High level data manipulation tool
# built on Numpy

pip install pandas

import pandas as pd
import numpy as np

'''
There are two types of data structures in pandas: Series and DataFrames.

Series: a pandas Series is a one dimensional data structure (“a one dimensional
 ndarray”)  that can store values — and for every value it holds a unique index, too.

DataFrame: a pandas DataFrame is a two (or more) dimensional data structure –
 basically a table with rows and columns. The columns have names and the rows
 have indexes.
'''
list(dict1)

dict1 = {'A':[1,2,3,4], 'B':[8,7,6,5], 'C':[9,12,11,10]}
dict1
pd.DataFrame(dict1)

first_df = pd.DataFrame({'A':[1,2,3,4], 'B':[8,7,6,5], 'C':[9,12,11,10]})
print(first_df)




world = { 'country': [ 'Spain','France', 'UK', 'India'],
           'Capital': [ 'Madrid','Paris', 'London', 'New Delahi' ],
           'population': [ 23,28, 25, 125 ]}
type(world)

world = pd.DataFrame(world)
world 
type(world)
###########################################################################
# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = { "country":names,
            "drives_right":dr,
            "cars_per_cap":cpc
            }
my_dict
# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)

########################################################################
import pandas as pd
market_data = pd.read_csv('market_fact.csv')

market_data1 = pd.read_csv('market_fact1.csv')
market_data1.describe()
market_data.dtypes

market_data1.isnull().sum()


market_data.head(3)
market_data.tail(2)
market_data.describe()
market_data.columns
type(market_data)
(market_data[72:80])
market_data.sample(4)
market_data.shape

market_data_facts = market_data[['Discount','Order_Quantity','Profit','Shipping_Cost','Product_Base_Margin']]
market_data_facts.head()
market_data_facts.shape


market_data_subset = market_data[['Discount','Product_Base_Margin']]
market_data[['Discount','Product_Base_Margin']].head(5)
market_data.head(7)[['Discount','Product_Base_Margin']]

market_data_subset.head()


#market_data.Discount > 0.1
market_data[market_data.Discount > 0.1]
market_data[market_data.Discount > 0.1].shape
market_data[market_data.Discount > 0.05].shape
#########################################################################

binary = pd.read_csv("C:/Users/ABHI/Documents/R_Files/binary.csv")
binary = pd.read_csv("binary.csv")
binary.head()
binary.shape


type(binary)
binary["gre"]
type(binary["gre"])     # pandas.core.series.Series

binary[["gre"]]
type(binary[["gre"]])       # pandas.core.frame.DataFrame

binary[['gre', 'rank']]
binary[1:4]

binary.describe()
binary.mean()
binary.iloc[:, 1].mean()

binary.count()
binary["admit"].max()
binary["gpa"].min()
binary["gpa"].median()
binary["gpa"].std()

binary.corr()

binary["gpa"]/2

gpa_39 = binary["gpa"]> 3.9
gpa_39
binary[gpa_39].shape
binary[gpa_39].count()

binary[(binary["gpa"]> 3.9) & (binary["gre"]> 650)]
binary[(binary["gpa"]> 3.9) & (binary["gre"]> 650)].count()

binary_filter = (binary["gpa"]> 3.9) & (binary["gre"]> 650)  
#binary_filter = (binary["gpa"]> 3.5) and (binary["gre"]> 600) 
binary_filter.count()
x = binary[binary_filter].count()
x.count()
binary[binary_filter].count()




# Take a DataFrame as input to your DataFrame 
my_df = pd.DataFrame(data=[4,5,6,7], index=range(0,4), columns=['A'])
print(my_df)
type(my_df)


my_dict = {"Z": ['1', '3'], "X": ['1', '2'], "Y": ['2', '4']}
my_df = pd.DataFrame(my_dict)
print(my_df)
my_df.iloc[ :, 0]

# loc : label based,  can select Rows, Columns, Rows & Columns
# iloc: integer position based
binary.iloc[[1,201,30,4], [1,2]]
binary.iloc[0:5, ]
binary.iloc[0:5, :]
binary.iloc[ ,: ]      # error
binary.iloc[ : ,2: ]
binary.iloc[ :,1: ].head(6)

binary.iloc[ :,: ]  # entire data frame
binary.iloc[:5,:]
binary.iloc[250:,2:]
binary.iloc[:,0]
binary.iloc[9,:]
binary.iloc


binary.loc[0:5,:]
binary.index

x = binary.iloc[10:20, ]
x
x.loc[0:5,:]

binary.loc[0:5, "admit"]
binary.loc[100:105, "gre"]
binary.loc[0:5, ["admit", "gre"]]


# Pandas Series Objects
binary.iloc[ :, 1]
type(binary.iloc[ :, 1])
binary.loc[ :,"gre"]
type(binary.loc[ :,"gre"])
binary["gre"]
type(binary["gre"])
type(binary[["gre"]])
print(type(binary["gre"]))
print(type(binary.loc[ :,"gre"]))
print(type(binary.iloc[ :, 1]))

binary[["admit", "gre"]]
print(type(binary[["admit", "gre"]]))



binary.loc[1]
print(type(binary.loc[1]))
binary.loc[[1]]
print(type(binary.loc[[1]]))

binary.loc[[1,2,3]]         # Row label            
binary.loc[[1,2,3], ['gre', 'rank']]



s1 = pd.Series([1,2,4,6,8,2])
s1

s2 = pd.Series(["Data Science", "Big Data"])
s2
type(s2)

pd.DataFrame([s1,s2])

pd.DataFrame(
    [
        [1,2],
        ["Data Science", 'Big Data']
    ]
)

pd.DataFrame(
    [
        [1,2],
        ["Data Science", "Big Data"]
    ],
    columns=["column1", "column2"]
)

df = pd.DataFrame(
    [
        [1,2],
        ["Data Science", "Big Data"]
    ],
    index=["row1", "row2"],
    columns=["column1", "column2"]
)
df

df.loc["row1":"row2", "column1"]

df = pd.DataFrame(
    {
        "column1": [1, "Data Science"],
        "column2": [2, "Big Data"]
    }
)
df



first_series = pd.Series()
first_series = pd.Series({'10':'Ahmedabad', '20':'Bangalore', '30':'Chennai','40':'Delhi','50':'Kolkatta','60':'Mumbai'})
print(first_series)
type(first_series)
first_series.shape
first_series.iloc[0:3]
first_series.iloc[0:3, :]
first_series.index


df
df.columns = ["A", "B"]
df


prod_data = pd.read_csv('prod_dimen.csv')
prod_data.dtypes
prod_data.head()
prod_data.shape
type(prod_data)

market_data = pd.read_csv('market_fact.csv')
market_data.head()
market_data.shape
market_data.columns

prod_data.columns

combined_data = pd.merge(market_data, prod_data, on='Prod_id', how='outer')
combined_data.columns
combined_data.shape


cust_data = pd.read_csv('cust_dimen.csv')
cust_data.head()
cust_data.shape
ship_data = pd.read_csv('shipping_dimen.csv')
ship_data.head()
ship_data.shape


combined_data2 = pd.merge(combined_data, cust_data, on = 'Cust_id',how='outer')
combined_master = pd.merge(combined_data2, ship_data, on = 'Ship_id', how='outer')
combined_master.columns
combined_master.shape

# write csv file
combined_master.to_csv('combined_test.csv')

combined_master.columns

#get number of observations with a profit greater than 1000
profit_grt_1000 = combined_master[combined_master.Profit > 1000]
profit_grt_1000_counts = len(profit_grt_1000)

high_value = combined_master.query('Sales >1000 and Order_Quantity <30')
high_value

#Using where
high_value_where = combined_master.where(combined_master.Sales >1000, combined_master.Order_Quantity <30,axis =1)
high_value_where

combined_master['Sales'].mean()
combined_master['Profit'].mean()

combined_master.groupby(['Product_Category'])['Sales'].mean()

combined_master.groupby(['Product_Category','Product_Sub_Category'])[['Sales','Profit']].mean()
combined_master.groupby(['Region'])[['Sales','Profit']].mean()

combined_master.groupby(['Product_Category','Product_Sub_Category'])[['Sales','Profit']].sum()

groupings = combined_master.groupby(['Product_Category','Region'])
groupings.agg([np.sum, np.mean, np.std])

groupings = combined_master.groupby(['Region', 'Product_Category'])
groupings.agg([np.sum, np.mean, np.std])

groupings = combined_master.groupby(['Product_Category', 'Product_Sub_Category'])
groupings.agg([np.sum, np.mean, np.std]).round()

combined_master.shape
pivot_ex = combined_master.drop_duplicates(subset = 'Ship_Date', inplace = False)
pivot_ex.shape



a1=np.array([1,2,3])
a2=np.array(['a','b','c'])
a3=np.array([10,20,30])
df=pd.DataFrame(data=[a1,a2,a3],columns=['colA','colB','colC'])
print(df)
df[['colA','colB']]
# Add new variable
df['colD']=[2,3,4]
print(df)

df['colE']=[20,40,3]
df
data={'Name':['a','b'],
     'age':[10,20]}
df=pd.DataFrame(data)
print(df)

# remove a column
x = df.drop(['Name'],axis=1)
x
print(df)
df.drop('Name',axis=1,inplace=True)
df
series1 = pd.Series(np.arange(8),index=['row1','row2','row3','row4','row5','row6','row7','row8'])
print(series1['row7'])
print(series1[series1>4])
series1['row1','row5']=80
print(series1)

df=pd.DataFrame(np.random.rand(16).reshape(4,4),index=['row1','row2','row3','row4'],columns=['col1','col2','col3','col4'])
df
df['col1']
df<0.3
df[df<0.3]
df.info()

df1=pd.DataFrame(np.arange(9).reshape(3,3),index=['row1','row2','row3'],columns=['col1','col2','col3'])
df1

df2=pd.concat([df,df1],axis=1)      # Column
print(df2)
df2=pd.concat([df,df1],axis=0)      # Row
print(df2)

df_x = df.round(1)
df_x

# try with inplace
df_x.append(df_x)
df_x.append(df_x, ignore_index = True)

df.shape
df
df.isnull()
df.isnull().sum()

y = df[df<0.3]
y
y.isnull()
y.isnull().sum()

df.mean()
df.mean(axis=1)
df.mean(axis=0)

df.quantile(q=np.arange(0,1,0.25))
df.quantile(.9)
df.quantile(q=np.arange(0,1,0.1))

df[(df['col1']>0.5) & (df['col2']!=0.2)]
df.query('col1>0.5 and col2!=0.2 ')

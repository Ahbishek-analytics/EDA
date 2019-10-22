# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 18:48:04 2018

@author: ABHI
"""

import matplotlib.pyplot as plt

year = [1950,1970, 1990, 2010]
pop =  [2.519, 3.692, 5.263, 6.972]
plt.plot(year, pop)     # plot(x,y)
plt.show()

plt.scatter(year, pop)
plt.show()

# Put the x-axis on a logarithmic scale
plt.xscale('log')

import matplotlib.pyplot as plt
help(plt.hist)

# default bin = 10
values = [1,1,1,4,2,2,3,4, 5,6,2,3,8,5,8,9,4,7]
plt.hist(values)
plt.hist(values, bins = 5, color = "red")
# Show and clean up plot
plt.show()


import matplotlib.pyplot as plt
year = [1950,1970, 1990, 2010]
pop =  [2.519, 3.692, 5.263, 6.972]
plt.plot(year, pop)     # plot(x,y)
plt.xlabel("Year")
plt.ylabel("population in Billion")
plt.title('Worls Population Projections')
#plt.yticks([2,4,6,8,10])

plt.yticks([2,4,6,8,10],
           ["2B", "4B", "6B", "8B", "10B"])


plt.xscale('log') 
# Definition of tick_val and tick_lab
tick_val = [1000,10000,100000]
tick_lab = ['1k','10k','100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val,tick_lab)   


plt.show()

# bubule chart
# Store pop as a numpy array: np_pop
np_pop = np.array(pop)

# Double np_pop
np_pop = np_pop*2





type(tips)

import seaborn as sns
tips = sns.load_dataset('tips')
print(tips.head())
tips.shape




tips.describe()
print(tips.sex.value_counts())

# total number of female who are smokers
tips[(tips['sex']=='Female') & (tips['smoker']=='Yes')].shape
tips.groupby('sex').size()
tips.groupby('time').size()

import pandas as pd
pd.crosstab(tips['sex'],tips['smoker'])

# how many people gave tip of more than 5 dollars
print(pd.value_counts(tips['tip']>5))
print(tips[tips['tip']>5].shape)

tips.groupby(tips['sex'])['tip'].mean()
IQR=24.127 - 13.347

outliers=tips[(tips['total_bill']<(13.347-1.5*(IQR))) | (tips['total_bill']>(24.127+1.5*(IQR)))]
 outliers.head()

%matplotlib inline
tips.columns
#Scatter plots
plt.plot(tips['total_bill'],tips['tip'],'o')
plt.xlabel("total_bill")
plt.ylabel("tip")
plt.title("Total_bill Vs Tip")

plt.hist(tips['total_bill'])
plt.hist(tips['total_bill'],density=False,bins=10,cumulative=True,align='mid')
plt.xlabel("Total_bill in Dollars")
plt.ylabel("frequeny")

plt.boxplot(tips['total_bill'])
plt.boxplot(tips['total_bill'],vert=False)

import seaborn as sns
#distribution plot
sns.distplot(tips['total_bill'])

# Joint plot: need atleast 2 "variables
sns.jointplot(tips['total_bill'],tips['tip'],kind="reg")

sns.jointplot(x="total_bill",y="tip", data=tips)

sns.pairplot(tips,hue='sex')
sns.countplot(tips['sex'])

sns.boxplot(tips['total_bill'],tips['sex'])
sns.boxplot(x="day",y="total_bill",data=tips)
sns.boxplot(data=tips,palette="rainbow")



# -*- coding: utf-8 -*-
#Heat Map
#A heatmap contains values representing various shades of the same colour for each value to be plotted. Usually the darker shades of the chart represent higher values than the lighter shade. For a very different value a completely different colour can also be used.
#The below example is a two-dimensional plot of values which are mapped to the indices and columns of the chart.




#Plot a dataframe with meaningful row and column labels:

flights = sns.load_dataset("flights")
flights
#change the shape of data
flights1 = flights.pivot("month", "year", "passengers")
flights1
ax = sns.heatmap(flights1)
#highest is white, lowest is red

#Annotate each cell with the numeric value using integer formatting:
ax = sns.heatmap(flights1, annot=True, fmt="d")

#Add lines between each cell:
ax = sns.heatmap(flights1, linewidths=.2)

#Use a different colormap:
ax = sns.heatmap(flights1, cmap="YlGnBu")

#Center the colormap at a specific value:
ax = sns.heatmap(flights1, center=flights1.loc["January", 1955])

#Don’t draw a colorbar:
ax = sns.heatmap(flights1, cbar=False)


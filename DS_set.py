# -*- coding: utf-8 -*-
#Set - collection, unordered, unindexed,curly bracket{},immutable, can add items

'''         Sets
A set is a collection which is unordered and unindexed
# Sets are a good way to get the unique elements out of a collection or finding 
common elements between various collections.
# To solve duplicates removal ,we can use sets, it is also unordered
# Unordered collection of items which are not repeated
''''
{key : value}

lst1 = [1,2, 'SIP', 'Dhiraj',3,2,1,1,1,2]
lst1
T = tuple(lst1)
T
type(T)


set1 = {1,2, 'SIP', 'Dhiraj', 2,2,2,1}
set1


L1 = list(set1)
L1

type(L1)


set1[0]  #cannot be accessed by index position, unordered
set1

for i in set1 : print(i)

'Dhiraj' in set1
'Kounal' in set1

#add item
set1.add('Pooja')
set1
#sorted
#add duplicate name of Pooja
set1.add('pooja')
set1
#no duplicates

#adding more than 1 item
set1.update(['ABC','DEF'])
set1

set1.update('XYZAB') #this will add individual
set1

len(set1)

set1.remove('Pooja')
set1  #error if Pooja does not exist
set1.remove('Akhil')

set1.discard('Akhil')  #no error now
set1

set1.discard('pooja')  #remove if found
set1

#pop
set1.pop()  #remove any location, unordered
set1.pop()
set1

set1.clear()  #empty
set1

set1 = {1,2, 'SIP', 'Dhiraj', True}
set1
del set1
str1


#other methods in sets
#add, clear, copy, difference, differenc_update(), discard, intersection, intersection_update, isdisjoint, issubset, issuperset, pop
#remove, symmetric_difference, symmetric_difference_update(), union, update

#Exercise

teamA = {'India', 'Australia','Pakistan', 'England'}
teamB = {'Bangladesh', 'New Zealand', 'West Indies', 'India'}
teamA
type(teamB)


teamB
#add Sri Lanka to TeamA
#create a teamC with all teams
#Perform all the set operations 
teamA.union(teamB)
teamA.difference(teamB)

# -*- coding: utf-8 -*-
#Tuples - collection, ordered, unchangeable/ immutatble, like list, round bracket
# [] : list
# () : tupple

'''
list 
tupple
dict
set
'''
tuple_fruit = ( 'Grapes',"apple", "banana", "cherry")
print(tuple_fruit)
type(tuple_fruit)
tuple_fruit[2] = "Mango"
print(len(tuple_fruit))
# Can not perform Remove operation
del(tuple_fruit)
tuple_fruit


tuple_misc = ('Delhi', 'Mumbai', 150, 47.67)
tuple_misc

type(tuple_misc)
print(len(tuple_misc))
tuple_misc[-1]


tuple1 = (102,2, 'SIP', 'Dhiraj', True)
tuple1

#everying like list except changes
tuple1[0] = 99

#access
tuple1[0]

for i in tuple1 : print(i)

if 'Dhiraj' in tuple1 : print('Dhiraj is present in tuple')
if 'Kounal' in tuple1 : print('Kounal is present in tuple')

tuple1.append('kounal')  #error, cannot add
len(tuple1)

#methods in tuple
#count, index, ...
tuple1
tuple1.remove()  #cannot remove also

x = 'a'
type(x)

#single value
tuple2a = 'a'
type(tuple2a)  #error incorrect way

tuple2b = 'a', 'b',
type(tuple2b)
tuple2b
#end of tuple
#where do we used it - list type of object where no changes are required
#list of gender, courses, categories, countries, list of values
#https://learnbatta.com/blog/python-working-with-tuple-data-type-41/

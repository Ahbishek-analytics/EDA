# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 22:16:46 2018

@author: ABHI
Description: Basic Learning
"""

print('Hello World')
print('Welcome to Python \n for Data Science')


# Calculator
a = 2
b = 4
c = a+ b
c
print(c)

'''
+	Addition
-	Subtraction
/	division
%	mod
*	multiplication
//	floor division
**	to the power of
'''


14 / 3   # classic division
14 // 3  # floor division
14 % 3   # remainder of the division

3 ** 2   # Square


a = 6
b = 7
print(a + b)  
print(a - b) 
print(a * b) 
print(a / b)
print(a // b)
print(a % b) 
print(a ** b)


# BMI Calculation
height = 1.86
weight = 83
BMI = weight/height**2
print(BMI)
type(BMI)   # float

day_of_week = 5
type(day_of_week)   # int

'''
==	True, if it is equal
!=	True, if not equal to
<	less than
>	greater than
<=	less than or equal to
>=	greater than or equal to
and	AND
or	OR
!=	NOT
'''
#Logical
print(3 < 4)
a=True
print(type(a))
print(True and False) 
print(True or False)
print(True and not False)

print(5>4)
print("hello"=="hello")
print(3<2 and 4>3)
print(6<5 or 5>4)
print(5 != 5)
print('7' in 'seven7')
print((5 >= 1) and (5 <= 10))

#####################################################################


# Strings
# both '' and "" can be used for strings
str1 = "Abhishek Kumar Tiwari"
str2 = 'Data Science'
type(str1)
type(str2)  #str
print(str1)
str2

'don't'
'doesn\'t'  # use \' to escape the single quote.
"don't"

'"No," you can not go.'
'No, you can not go.'
'Isn\'t, they said.'
'\'Isn\'t,\' they said.'
'"No," you "can\'t" go.'
'No, you can\'t go' 


course = 'Data Science \n Professional'
course
print(course)

first_name = "Data"
last_name = 'Science'
course_name = first_name + " " + last_name
print(course_name)

#  multiple lines
print("""
      Python is an interpreted high-level programming language 
      for general-purpose programming.
      Created by Guido van Rossum and first released in 1991
      """)

'Py' 'thon'
"Py"  "thon"

4* "DS"
2* 'Data' +  " " +"Science"

# String slicing
s = "Python, Rprogramming, SPSS, SAS and Julia"
s
type(s)
print(s[0:7])
print(s[8:9])
print(s[22:26])


z = True
type(z)     # bool



small = "i am upper cased"
print(small.upper())

large = "I AM LOWER CASED"
print(large.lower())

# strip, lstrip, rstrip
some_sentence = "There is a space at the end    "
print(some_sentence)
print(some_sentence.rstrip())

loan_rate = '10.5%'
print(loan_rate.rstrip('%')) 

start = "   There is space at the start"
print(start)
print(start.lstrip())

spaces = "   Trim whitespaces  "
print(spaces)
print(spaces.strip())

num_with_chars = '*444#'
print(num_with_chars.rstrip('#').lstrip('*'))
print(num_with_chars.lstrip('*').rstrip('#'))
val = "2 apples"
no_of_apples = val[0] 
no_of_apples
print('number of apples are', no_of_apples)
                            

#############################################################
'''
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
'''                       
############################################################
'''         List
#List is declared by using square brackets
# A list is an ordered collection, it's sequential
# List is Mutable
'''
initial_list = []
print(initial_list)

# Collection of mixed elements
DA_languages = ['R','Python', 'SAS', 'SPSS', 100]
print(DA_languages)

# Queue concept, Last elements first out LIFO
DA_languages.append('Julia')
print(DA_languages)
print(len(DA_languages))
x = DA_languages.pop()
print(x)
print(DA_languages)
print(DA_languages.pop())
DA_languages.pop(-1)
DA_languages.pop()
DA_languages.pop(0) 


DA_languages.append('R')
print(DA_languages)
DA_languages.remove('R')
print(DA_languages)
del DA_languages[2]
del DA_languages[1:3]

#print(', '.join(DA_languages))

'''
What is the difference between pop() and remove() ?
pop() requires the index of element to remove
 whereas remove() requires the element itself to remove it
 '''
# To print id: internal unique identifier that python uses to address
# the different elements that you create for your own 
# programme
print(id(DA_languages))

# new_list & DA_languages are just two different names for the same entity (list), 
new_list = DA_languages
DA_languages.append('Julia')
print(new_list)
print(id(new_list))

another_list = DA_languages.copy()
DA_languages.append('Watson')
print(id(another_list))

new_list = DA_languages[:]
print(id(new_list))

different_list = list(DA_languages)
print(id(different_list))


lst = [1, 'a', 2.3, "Abhishek", 100]
lst
lst[1]      # 1
lst[0:2]    # [1, 'a']
lst[-1]     # 100
# [start : end] --> [inclusive : exclusive]
lst[-4:-1]  # ['a', 2.3, 'Abhishek']
lst[-2:-1]
lst[2:]     # from 2nd index to end
lst[:3]     # from 0th index to 2nd index


lst_n = [["Abhi", 187],
       ['XYZ', 165],
       ["Rahul", 172]]
lst_n
lst_n[0]      # ['Abhi', 187]
lst_n[0][0]   # 'Abhi'
type(lst_n)   # list

# Cahnge list elements
lst_n[2][1] = 180
lst_n[0] = ["Abhishek", 188]

lst1 = lst_n + ["Manoj"]
lst1
lst
lst2 = lst +lst1
lst2

lst2[5]
del(lst2[7][1])

del(lst2)
lst2

x = ["a", "b", "c"]
y = x       # copy list , it just copy the address
y[1] = "B"   # Cahnge in y will affect x also
x           # ['a', 'B', 'c']

x = ["a", "b", "c"]
z = list(x)
z
z[2] = "C"
z
x


L= x[:]
L
L[0] = "A"
L
x


a_sentence = "Hi Team, this is to inform you that there will be no class today."
words_in_sentence = a_sentence.split() 
print(words_in_sentence)

a_mail = "Hi Team, this is to inform you that I'm not well today. I won't be coming to office, but I'm available on call. Thanks."
a_mail
sentences_in_mail = a_mail.split('.')
print(sentences_in_mail)
a_mail.split(',')




lst = ['Abhishek', 'Tiwari', "Rahul", 44, 26, 44, 450]
lst.index('Rahul')      # find the index of element
lst.count(44)           # count the no of time 44 present in list

lst.append("Abhi")      
lst.append(100)
print(lst)


lst1 = ['Abhishek', 'Tiwari', "Rahul", 44, 26, [10,20,30]]
lst1[5]
lst1.index(10)      # does not work

nm = "abhishek"
nm.capitalize()         # captilize the first letter of string
nm.replace("k", "k Tiwari")
nm.index("k")
nm.index("h")           # index of first occurance 


nums = [2,6,9,3,2,2,2,1]
nums
print(len(nums))
print(sorted(nums))      # check to sort in decreasing order : Home Assignment
print(max(nums))
print(min(nums))
nums.insert(2,100)
nums.insert(100,50)
nums

nums.sort(reverse=True)
print(nums)
print(nums.count(2))


nums.append(500)
nums.extend([1000, 2000, 3000])
print(nums)


game = ['Cricket', "Football", 'Hockey', 'Badminton']
game[1]
game[1:3]
game[1:5:2]
game.append('Ice Hockey')
game.insert(0,'Computer')
game.insert(2,'Polo')
game.remove('Polo')
game

a = [0,1,2,3,4,5,6,7,8,9]
a[1:5:2]
a[1:6:2]
a[1:9:2]
a[1:10:2]
a[1:8:3]

# Function: Piece of reusable code which solves perticular task
x = [1,34,546,75,42,32]
max(x)
min(x)

y  =[1.3232, 1.342]
round(y[1], 2)
round(y[0], 1)
round(y,2 )     # type list doesn't define __round__ method
round(1.432, 2)
round(1.532)    # (default 0 digits)
help(round)     # round(number[, ndigits]) -> number; ndigits is in [], an optional argument

##################################################################
'''    TUPLES
# Unike a list, once it is created, cannot be changed, Immutable. Ordered collection of elements ,
# Accessing the same like lists, Methods like append, extend will not work
# Python handle tuples more efficiently, since memory initally will be known.
# Lists are mutable, tuples are not
# one example of a tuple : Storing Latitude, longitude. Precisely i need to get the same order however i have declared.
# Tuples, Python handle far efficient in terms of memory, since it knows the
# elements when we have declared it
'''
# [] : list
# () : tupple

tuple_fruit = ( 'Grapes',"apple", "banana", "cherry")
print(tuple_fruit)
type(tuple_fruit)
tuple_fruit[2] = "Mango"
print(len(tuple_fruit))
# Can not perform Remove operation
del(tuple_fruit)

tuple_misc = ('Delhi', 'Mumbai', 150, 47.67)
tuple_misc

type(tuple_misc)
print(len(tuple_misc))
tuple_misc[-1]


l1 = [1,]
l1 = [1]
l1


times = 80
print("_" * times)

print ("[1]:Creating a tuple, Method 1") 
print ("Empty tuple") 
T = () 
type(T)
len(T)

print (T) 
print ("Tuple with single element") 
T = (1,)
print(type(T))
print (T)
T1 = (2)
T1
len(T)
T1



T = (1, 2, 3.5, 'Abhi', [2, 5, 6.9], {1:'A', 2: 'B'}, (100, 200, 300))
T
len(T)
print(T)
T[4]
T[4][2]

T = tuple("Tuple")
T
len(T)
T = tuple('Tuple')
print("T :", T)
print(len(T))

# Concatenation of tuples
T1 = (1,2,3)
T2 = ("R", "B", "G")
T1 + T2

T = T1*5
T2*3
print("After Multiplication T1* 5, value  = ", T)

T = ("DATA")
len(T)
T[2]
T = tuple("DATA Science")
len(T)
print("T[0]: ", T[0])
print("T[3]: ", T[3])
print("T[5]: ", T[5])
print("T[7]: ", T[7])

T = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print ("T:", T) 
print ("T[0:4]:", T[0:4])
#print ("T[::2]:", T[::2])
#print ("T[1::2]:", T[1::2])
#print ("T[2:9:3]:", T[2:9:3])

# Convering tuple into list
T = (1, 2, 3, 4, 5) 
print ("T:", T)
L = list (T) 
type(T)
type(L)

# Sorting a tuple
T = (5, 4, 3, 2, 1)
T.sort()  # doesnt work
sorted(T)
L = list (T)
sorted(L)



print ("Index of an existing data") 
T = (5, 4,  2, 2, 5, 4, 6, 34, 76, 2)
print ("T:", T) 
print ("34 in T:", 34 in T)
print ("345 in T:", 345 in T)
print ("T.index (5):", T.index (5))
print ("T.index (2):", T.index (2))

###############################################################
'''         Sets
A set is a collection which is unordered and unindexed
# Sets are a good way to get the unique elements out of a collection or finding 
common elements between various collections.
# To solve duplicates removal ,we can use sets, it is also unordered
# Unordered collection of items which are not repeated
''''
students_list = ['A','A','B','C','C','E','N']
type(students_list)
students_set = set(students_list)
print(students_set)
print(type(students_set))

students_list_2 = ['A','N','F','N','G','A']
students_set_2 = set(students_list_2)
students_set_2


print(students_set.intersection(students_set_2))
print(students_set.union(students_set_2))
print(students_set.difference(students_set_2))
print(students_set_2.difference(students_set))
print(students_set.symmetric_difference(students_set_2))

set_fruit = {"apple", "banana", "cherry"}
print(set_fruit)
print("banana" in set_fruit)

# add() method : To add one item to a set
# update() method: To add more than one item to a set
set_fruit.add("Mango")
set_fruit.update(['Orange', 'Grapes'])
print(set_fruit)
print(len(set_fruit))

set_fruit.remove("banana")
set_fruit.remove("sugar")   # if item doesn't exist  it throw an error
set_fruit.discard("banana") # No error

set_fruit.clear()
print(set_fruit)

del set_fruit

set_fruit = set(('apple', "banana", "cherry")) # note the double round-brackets
print(set_fruit)


a = set("Data Science")
print(a)
b = set("Data Analytics")
print(b)

sorted(a)
a-b
a | b
a ^b   # a OR b but not both
a & b
###############################################################
'''         Dictonaries
# {Key Value Pair}, key in disctonery should be unique
# should be immutable object
# Dictionary: colection of unordered items, declared by {}

Python's dictionary type is a hashed key value structure. This is comparable
to associative arrays in other languages

Keys and values may be any type. Keys must be immutable,
'''

empty_dict = {}
print(type(empty_dict))


emp = {'Name': 'Abhishek', 'Grade':  9, 'City': 'Lucknow'}
emp
emp['Grade']
emp.keys()
emp.values()
emp

world = {'UK':25, 'India':70, 'China': 75}
world['India']
world['UK']

Bharat = world['India']
Bharat
print(Bharat)

world['USA']

# Accessing by Key's, if key is not found, None is displayed
print(world.get('USA'))
print(world.get('USA', 'Not Found'))

world['india'] = 100
world
world['India'] = 500

world['Australia'] =10

print(world.keys())
print(world.values())
print(list(world.keys()))


print('UK' in world)

world['sealand'] = 0.01
'sealand' in world          # TRUE if sealand is present in world
del(world['sealand'])
'sealand' in world


# Print the sorted list of keys
x=(sorted(world))
print(x)

# To delete the element in a dictionary
del world['india']
print(world)

#Remove all entries in a dictionary
world.clear()
print(world)

#delete entire dictionary
del world
print(world)




students_data = { 1:['Amit Mishra', 24] , 2:['Udit Singh',25], 3:['Neha Gupta', 26], 4:['Prashant Awasthi',24], 5:['Priya Singhal',27]}
print(len(students_data))
print(students_data.values())
students_data[1]
Name = students_data[1][0]
Name
Age = students_data[1][1]
Age

students_data[6] = ['Super Man', 'asd asda']
students_data


new_dict = dict(Country = 'India', States = ['AP', 'MP', 'MH'])
new_dict['States'] 

# if we have same keys(duplicate) , last value declared will be overwritten
dict ={'Name': 'XYZ',
      'Age':17,
      'Name':'ABC'}
print(dict)


# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'austria':'vienna' }

# Update capital of germany
europe["germany"] = "berlin"

# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


print(europe["france"])
# Print out the capital of France
print(europe["france"]["capital"])

# Create sub-dictionary data
data = {"capital":"rome","population":59.83}

# Add data to europe under key 'italy'
europe["italy"] = data

# Print europe
print(europe)















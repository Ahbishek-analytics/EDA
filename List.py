# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 18:12:04 2019

@author: dell
"""

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

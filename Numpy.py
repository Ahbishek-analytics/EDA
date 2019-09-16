# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 20:39:06 2018

@author: ABHI
"""

# In Python every thing is object and 
# Each object have methods associated with it depending on type
# nm.replace string has replace method, list does not have replace method
# Depending on the type of object methods behave differently
# list.index will return the index of element while str.index will return indext of letter


# Packages: Directory of python scripts
# Each script = module
# These modules specify function, methods and types
# Thousands of packages avaiable
# For data Science
# Numpy         : for efficient working with arrays
# Matplotlib    : Visualization
# Scikit-leaarn : Machine Learning


# installation of packages
# http://pip.readthedocs.org/en/stable/installing
# Download  get-pip.py
# Install   python3 get-pip.py      from terminal
# pip3 insatll numpy

#  "Numeric Python" or "Numerical Python"


############################################################
pip install numpy         # 1 time activity
import numpy as np










#############################################################
my_first_array = array([1,2,3,4,5])
my_first_array = np.array([1,2,3,4,5])
print(my_first_array)
print(type(my_first_array))

type(my_first_array)


distance_in_kms = [2.1, 4.9, 5.6, 7.8]
distance_in_kms*3 

[10,100]*5

distance_in_ms = [item*1000 for item in distance_in_kms]
#distance_in_ms = [x*10000 for x in distance_in_kms]
print(distance_in_ms)


x = tuple(distance_in_kms)
type(x)

a = np.array(distance_in_kms)
a
type(a)
a*10
np.array(distance_in_kms)*1000
print(len(np.array(distance_in_kms)))




a=np.array([1,'a',3])
print(a)
print(type(a))
a*3


# arrange
# # start, end (exlusive), step
np.arange(1,13,4)
np.arange(1,4,2)
np.arange(3)
np.arange(3.0)
np.arange(3,7)
np.arange(3,7,2)
a = np.arange(1, 10, 4)
print(a)
print(type(a))

#default step of 1 and start from 0
x = np.arange(5)
print(x)

x = np.arange(0.5, 10.1, 0.7)
print(x)

y =np.array([1,2,3,4,5., 'x'])
y.dtype

int_array = np.array([1,29,3,45,51])
int_array
int_array[-3]


int_array.dtype
x = np.array([1.,2,3,4,5])
x.dtype
type(x)
print(int_array.dtype)
print(int_array.ndim)
print(type(int_array))

print(int_array[:-1])
#print(int_array[::-1]) 

array_of_floats = np.array([5.5, 5.4, 4.11, 16.0, 6.2, 5.8, 7.1], float)
print(type(array_of_floats.dtype))
array_of_floats
type(array_of_floats)
array_of_floats.dtype

array_of_floats


print(array_of_floats.mean())
print(np.median(array_of_floats))
print(array_of_floats.max())
#Index of Max value
print(array_of_floats.argmax())

print(array_of_floats>5.5) 

a = np.array([1,5,15, 2, 25])
a

greater_than = a>5.5
print(any(greater_than))
print(all(greater_than))
print(greater_than)
a



first_array = np.array([1,2,3])
second_array = np.array([4,5,6])
print(np.concatenate((first_array,second_array)))

#  functions to create arrays
import numpy as np

a = np.zeros((2,2))   # Create an array of all zeros
print(a)              

b = np.ones((3,2))    # Create an array of all ones
print(b)              

c = np.full((3,4), 6)  # Create a constant array
print(c)               

d = np.eye(4)         # Create a 2x2 identity matrix
print(d)              


                    


a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
a
type(a)
a.shape

a[1,2]

a[2,3]
a[1:3,3]
a
a[1,1:2]

b = a[:2, 1:3]      # before 2nd row
a.shape
b
type(b)
print(b.shape)
d = a[1:40, 1:3]      # after 1st row
d
print(a[0, 1])   
b[0, 0] = 100     # b[0, 0] is the same piece of data as a[0, 1]
print(a[0, 1])   
a







#################################################################
# use this
import numpy as np
np.array([1,2,3])

from numpy import array
array([10,20,30])

height = [1.78,1.84,1.55, 1.68]
weight = [82, 88, 62, 74]
BMI = weight/height**2          # will not work with list

# Solution: Numpy Easy and fast
np_height = np.array(height)
np_weight = np.array(weight)
BMI = np_weight/np_height**2

type(np_height)     # numpy.ndarray
type(BMI)           # numpy.ndarray



py_lst = [1,2,3]
py_lst + py_lst         # [1, 2, 3, 1, 2, 3]

numpy_array = np.array([1,2,3])
numpy_array  + numpy_array      # array([2, 4, 6])

# Subsetting
BMI = [32,45,21,34,12]
BMI = np.array(BMI)
type(BMI)
BMI <26
BMI[BMI <26]

np_2d = np.array([[1.78,1.84,1.55, 1.68],
                 [82, 88, 62, 74]])
np_2d.shape     #(2, 4)
np_2d.ndim
np_2d[0][2]
np_2d[0,2]
np_2d[: , 1:3]
np_2d[1,:]      # 2nd Row
np_2d[:,1:]
np_2d[:,:2]

# Avg hight
np.mean(np_2d[0, :])
np.median(np_2d[0, :])
np.std(np_2d[0, :])                  # Standard deviation 0th row(height)
np.sort(np_2d[1:,])                  # sort weight

ht = np.random.normal(1.75, 0.2, 10)      # mean, sd , #samples
ht
#

a = np.arange(10)
a
b = a[::2]
 b
a[::3]
b[0] = 12
b
a   
a = np.arange(10)
b = a[::2].copy()  # force a copy
b[0] = 12
a



# Reshaping Illustration
arr = np.array([[1, 1, 1, 1],  [2, 2, 2, 2],  [3, 3, 3, 3]])
 
# Check original shape    
print(arr.shape)
#>> (3, 4)
 
# Reshape to (4,3)
arr = arr.reshape(4,3)
arr

# Reshape to (6,2)
arr = arr.reshape(6,2)
arr
# Reshape to (2, 6)
arr = arr.reshape(2, 6)
arr
 
# Reshape to (1, 12)
arr = arr.reshape(1, 12)
arr
 
# Reshape to (12, 1)
arr = arr.reshape(12, 1)
arr




#Functions

def square(num):
    out = num**2
    return(out)
square

square(7)
square(9)

q = square(4)
print("Square of number is "+str(q))


def factorial(n):
    if n>1:
        return n*factorial(n-1)
    else:
        return n

fact = factorial(5)
print(fact)
def factorial(n):
    if n>1:
        return n*factorial(n-1)
    else:
        return n

fact = factorial(5)
print(fact)
print(type(factorial))
print(type(fact))

def addition(*args):
    print(args)
    return(sum(args))
    
print(addition(4,5,6,7,8,9))
print(addition(1,2))

def add_num(a,b):
    print(a,b)
    c=a+b
    return(c)
    
add_num(4,5)    
x = add_num(5,6)
x


def my_function(country ):
  print("I am from " + country)
  
 
my_function("Sweden")  
my_function("India")
my_function()
my_function("Brazil")




def my_function(country = "China"):
  print("I am from " + country)
  
  
# lambda Function
#A lambda function is a small anonymous function.

#A lambda function can take any number of arguments, but can only have one expression.  
  
  x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

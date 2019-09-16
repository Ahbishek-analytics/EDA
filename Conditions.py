
# if condition
'''
if some_condition:
    algorithm
    
The syntax for control structures in Python use colons and indentation.
Beware that white-space affects the semantics of Python code.
'''
Marks = 50
if Marks >35:
    print("The value of Marks is " + str(Marks))

Marks = 50
if Marks >35:
    print(Marks)


Marks = 50
if Marks >35:
    print("The value of Marks is ", Marks)

'''
If-else
if some_condition:
    algorithm
else:
    algorithm
'''
x = 2
if x > 10:
    print("X is greater than 10")
else:
    print("X is less than 10")


'''
if-elif

if some_condition:
    algorithm
elif some_condition:
    algorithm
else:
    algorithm
'''
x = 15
y = 100
if x > y:
    print("X is greater than Y")
elif x < y:
    print("X is less than Y")
else:
    print("X is equal to Y")


score = input("Enter your test score : ")
score
type(score)

score = int(input("Enter your test score : "))
type(score)

passing = 40
distinction = 90

if score >= distinction:
    print("You're at the top! You’ve earned a distinction!")

if score >= passing & score < distinction:
    print("You have passed!")

if score >= passing and score < distinction:
    print("You have passed!")

if score < passing:
    print("Sorry! You have failed")


if score==100:
    print("Perfect")
elif  90<=score<100:
    print("Distinction")
elif 60 <=score <90:
    print("First Class")
elif 40<=score<60:
    print("Second Class")
else:
    print("Failed")

######################################################    
   
           
           
num = int(input("Enter a number: "))

if num%2==0:
    print("Even number")
    if num%4==0:
        print(" and divisible by 4 too")
    else:
        print(" but not divisible by 4")
else:
    print("Odd number")
    if num%3==0:
        print(" and divisible by 3 too")
    else:
        print("but not divisible by 3")


if None:
    print("Is True")
else:
    print("Is False")

xyz = "random"

if xyz:
    print("Is True")
else:
    print("Is False")

if 4:
    print("Is True")
else:
    print("Is False")

if True:
    print("True")
else:
    print("False")
    

if True or True:
    if False and True or False:
        print('A')
    elif False and False or True and True:
        print('B')
    else:
        print('C')
else:
    print('D')    


if 1 and 0:
    print("Sucess 1 and 0")
elif 0 and 0:
    print("Sucess 0 and 0")
elif 0 and 1 or 1:
    print("Sucess 0 and 1 or 1")
elif 0 and 0 or 1 and 1:
    print("Sucess : 0 and 0 or 1 and 1")




##############################################################
for i in range(5):
    print(i)

'''
Q. Print all odd numbers between 21 and 121 excluding 121. 
Q. Print all numbers divisible by 5 between 100 and 200 including 200 itself.  
Q. Print all numbers between 300 and 500 that are divisible by 5 as well as 3. 
'''


for i in range(1,5):
    print(i)
    
for k in range(1,15,2):
    print(k)
    
for i in range(1,10,2):
    print(i)     
    
name = "My Name"
for i in name:
    print(i)



    
nums = '838848237890237388221'
all_even=''
all_odd = ''
for number in nums:
    if int(number)%2 == 0:
        all_even += number
    else:
        all_odd += number

    
#print('All Even numbers are :' + all_even)    
#print('All Odd numbers are :' + all_odd) 
print('All Even numbers are :' + all_even + ' & All Odd numbers are :' + all_odd)     
    

list_a = ['This','is','my','first','list','iteration']
list_a
for i in list_a:
    print(i)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for list1 in list_of_lists: 
    print(list1)
    for x in list1: 
        print(x)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for list1 in list_of_lists: 
    for x in list1: 
        print(x)
    print(list1)


#iterate using length of a list
for i in range(len(list_a)):
    print(i)

list_of_inventories = ['Apple', 'Banana', 'Potato', 'Mango', 'Onion', 'Toothpaste']
fruits = ['Apple','Banana','Mango','Orange','Strawberry']
vegetables = ['Potato', 'Onion','Cucumber', 'Celery']

#count of fruits in inventory list
count_fruits = 0
#count of vegetables in inventory list
count_veg = 0
for item in list_of_inventories:
    print("Item available in Inventory :" +item)
    if item in fruits:
        print(item)
        count_fruits+=1
        print(count_fruits)
    elif item in vegetables:
        count_veg +=1
    else:
        continue
print(count_fruits)
print(count_veg)


sentence = "Is Python simpler than R ?"
for word in sentence.split():
    print(word)
    
  

# Dictionary Iteration
state_capitals = {'Haryana': 'Chandigarh', 'Rajasthan': 'Jaipur', 'Punjab': 'Chandigarh', 'Tamil Nadu': 'Chennai', 'Maharashtra': 'Mumbai'}

#iterate over key-value pairs
for key, val in state_capitals.items():
    print("The capital of {} is {}".format(key,val))
    
#iterate over keys
for a in state_capitals.keys():
    print(a)
    
#iterate over vals
for a in state_capitals.values():
    print(a)



#while loop

start =20
total= 0
while start<51:
    #total+=start
    start+=1
    print(start)

print(total)
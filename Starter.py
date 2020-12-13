import random

num = 5
word = 'String'
dict1 = {"A":"Apple", "B":"Bannana", "C":"Cherry"}
list1 = [1,2,3,4]

#if elif else
num1 = 5
num2 = 10
num3 = 20

if(num1 > num3):
    print(num1)
elif(num3 > num1):
    print(num3)

#for/else
for i in range(10):
    print(i)

list2 = ['a', 'b', 'c', 'd']
for item in list2:
    if(item is 'e'):
        print('found ' + item)
        break
else: #this runs if the break doesn't run. this is based on the for loop not the if 
    print('No e found')

    
#Example of a docstring
def double(num):
    """Function to double a value"""
    return 2*num

print(double.__doc__)

print(random.randint(1,10))

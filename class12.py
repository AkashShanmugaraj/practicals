# Program 1
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
def calc(num1,num2):
    op = input("Enter an Operation [+,-,*,/,%]:")
    if op == '+':
        print(num1+num2)
    elif op == '-':
        print(num1-num2)
    elif op == '*':
        print(num1*num2)
    elif op == '/':
        print(num1/num2)
    elif op == '%':
        print(num1%num2)
    elif op == '//':
        print(num1//num2)

# Output 1
# Enter number 1: 10
# Enter number 2: 5
# Enter an Operation [+,-,*,/,%]: +
# 15

# Program 2
number = int(input("Enter a number: "))
def calc(n):
    nums = list(range(1,n+1))
    divisors = []
    total = 0
    for a in nums:
        if n%a == 0:
            divisors.append(a)
            total += a

    if n in divisors:
        total -= n
    if total == n:
        print("The given number is a perfect number")
    else:
        print("The given number is not a perfect number")

#Output 2
#Enter a number: 28
#The given number is a perfect number
##Source Code 11
#a = input("Enter a string: ")
#if a == a[::-1]:
#    print(True)
#else:
#    print(False)

# Program 3
n = input("Enter a 3 digit number: ")
s = (int(n[0])**3) + (int(n[1])**3) + (int(n[2])**3)
if s == int(n):
    print(n,"is an ArmStrong Number!")
else:
    print(n, "is not an ArmStrong Number!")

#Output 3
#Enter a 3 digit number: 371
#371
#371 is an ArmStrong Number!


#p4 + p5 = p4
# Program 4
# Factorial 
from math import factorial
n = int(input("Enter a number: "))
print(factorial(n))

# Output 4
# Enter a number: 3
# 6

# Source Code 4
# Fibonacci
terma = 0
termb = 1

l = int(input("Enter limit: "))
print(terma, end = "  ")
for i in range(l-1):
    print(termb, end = "  ")
    a = terma + termb
    terma = int(termb)
    termb = a

#Output 4
#Enter limit: 10
#0  1  1  2  3  5  8  13  21  34


# Source Code 5
msg=input("Enter any string : ")
newlist=[]
newlist[:0]=msg
I=len(newlist)
ed=I-1
for i in range(0,I):
    if newlist[i]!=newlist[ed]:
        print ("Given String is not a palindrome")
        break
    elif i>=ed:
        print ("Given String is a palindrome")
        break
    I=I-1
    ed = ed - 1

# Output 5
# Enter any string : nitin
# Given String is a palindrome

# 4/3 pi r3
# 4 pi r 2

#Program 6
# Q7
my_list = ['p','r','o','b','e']
print(my_list[0])
print(my_list[2])
print(my_list[4])
n_list = ["Happy", [2,0,1,5]]
print(n_list[0][1],n_list[0][2],n_list[0][3])
print(n_list[1 ][3])


# Q8
memo=[] 
for i in range (5): 
    x=int(input("enter no. \n")) 
    memo.insert(i,x) 
    i+=1 
print(memo) 
memo.append(25) 
print("Second List") 
print(memo) 
msg=input("Enter any string : ") 
newlist=[] 
newlist[:0]=msg 
I=len(newlist) 
print(I)



#Program 7
# Random Module
import random
print("A random number from the list is: ",end = '')
print(random.choice([1,2,3,5,6]))

print("A random number from a range is: ", end = '')
print(random.randrange(20,50,3))

# Math Module
from math import log, fabs, floor
print(log(10), fabs(-100), ceil(18.76))

#Student info system
studs = {}
menu  = '''What are you upto?
1. Create a Student Record
2. Fetch Data
'''
q = int(input(menu))

if q == 1:
    name = input("Enter student name: ")
    marks = int(input("Enter student marks: "))
    studs[name] = marks
    print("Record Added")

elif q == 2:
    name = input('What is the name? ')
    marks = studs.get(name,'Record Not Found')
    print(marks)

'''
def even(a):
    for i in range(1,a+1):
        if i%2==0:
            print(i)


while True:
    c=int(input("enter number: "))
    even
    (c)#argument
'''
'''
def odd(a):
    for  i in range(1,a+1):
        if i%2!=0:
            print(i)

while True:
    c=int(input("enter number: "))
    odd(c)
'''
'''
#reverse (from n to 1). -    us-ing while loop

def reverse(a):
    for i in range(a,0,-1):
        print(i)
        
while True:
    c=int(input("enter frist number: "))
    reverse(c)
'''
'''
#alphabets from a to z. - using while loop

def alphabets(a):
    for i in range(97,123):
        print(chr(i))

while True:
    c=input("enter alphabets: ")
    alphabets(c)
'''
'''
# sum of all natural numbers between 1 to n

def sum (n):
    s=0
    for i in range(1,n+1):
        s=s+i
    print(s)

while True:
    c=int(input("enter frist number: "))
    sum (c)
'''
'''
n=10
s=0
for i in range(1,n+1):
    s=s+i
    print(s)
'''
'''
#find sum of all odd numbers between 1 to n.

def sum(n):
    s=0
    for i in range(1,n+1):
        if i%2!=0:
            s=s+i
    print(s)

while True:
    c=int(input("enter frist number: "))
    sum(c)
'''
'''
#find sum of all even numbers between 1 to n.

def sum(n):
    s=0
    for i in range(1,n+1):
        if i%2==0:
            s=s+i
    print(s)

while True:
    c=int(input("enter frist number: "))
    sum(c)
'''
'''
# print multiplication table of any number.

def multiplaction (n):
    for i in range(1,11):
        print(i*n)
        
while True:
    c=int(input("enter number: "))
    multiplaction (c)
'''
'''
# to count number of digits in a number.

def count(n):
    c=0
    while(n!=0):
        c+=1
        n=n//10
    print("count:",c)

n=int(input("enter frist number"))#454465
count(n)

'''
'''
def count(n):
    count=0
    while(n!=0):
        count+=1
        n=n//10
    print(count)

a=int(input("enter number: "))
count(a)
'''
'''
#  find sum of first and last digit of a number.

def digit(d):
    
    l=d%10
    while (d>10):
        d=d//10
    print(d+l)

a=int(input("enter number: "))
digit(a)
'''
'''
# find first and last digit of a number
def digit(d):
    print(d%10)
    while (d//10!=0):
        d=d//10
    print(d)

a=int(input("enter number: "))
digit(a)
'''
#2n
'''
def digit(d):
    print(d%10)
    while(d>10):
        d=d//10
    print(d)

a=int(input("enter number: "))
digit(a)
'''
'''
#find sum of first and last digit of a number.
def digit(d):
    l=d%10
    while(d>10):
        d=d//10
    print(d+l)

a=int(input("enter number: "))
digit(a)
'''

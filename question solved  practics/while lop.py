'''
def even(e):
    i=0
    while i<=e:
        if i%2==0:
            print(i)
        i=i+1
        
a=int(input("enter number"))
even(a)
'''
'''
def odd (o):
    f=0
    while f<=o:
        if f%2!=0:
            print(f)
        f=f+1

a=int(input("enter frist number"))
odd(a)
'''
'''
#print all natural numbers from 1 to n. - using while loop

def number(n):
    i=0
    while i<=n:
        print(i)
        i=i+1
 
a=int(input("enter number"))
number(a)
'''

#print all natural numbers in reverse (from n to 1).
#-    us-ing while loop
'''
def reverse_number(n):
    i=n
    while i>=1:
        
        print(i)
        i=i-1

a=int(input("enter frist number"))
reverse_number(a)
'''
#print all alphabets from a to z._while loop
'''
def alphabets(g):
    i=93
    while (i<=g):
        print(chr(i))
        i=i+1

a=int(input("enter number"))
alphabets(a)
'''
'''
for i in range(97,123):
    print(chr(i))
'''
'''
#sum of all natural numbers between 1 to n.

def sum(n): 
    s=0
    i=0
    while (i<=n):
        s=s+i
        print(i,s)
        i=i+1

a=int(input("enter frist number"))
sum(a)
'''
'''
#find of sum even number between 1 to n.

def sum(n):
    i=0
    s=0
    while i<=n:
        if i%2==0:
            s=s+i
            print(s)
        i=i+1

a=int(input("enter frist number"))
sum(a)
'''
'''
#find sum of all odd numbers between 1 to n

def sum(n):
    s=0
    i=0
    while i<=n:
        if i%2!=0:
            s=s+i
            print(s)
        i=i+1

a=int(input("enter frist number"))
sum(a)
'''
'''
# print multiplication table of any number

def multiplaction(m):
    i=1
    while i<=10:
        print(i*m)
        i=i+1

a=int(input("enter the number"))
multiplaction(a)
'''
'''
#count number of digits in a number.

def count(c):
    count=0
    while c!=0:
        count=count+1
        c=c//10
    print(count)

a=int(input("enter number"))
count(a)
'''
'''
#find first and last digit of a number
def digit(d):
    print(d%10)
    while(d//10!=0):
        d=d//10
        print(d)

a=int(input("enter the number"))
digit(a)
'''
'''
#2nd methard
def digit(d):
    print(d%10)
    while(d>10):
        d=d//10
        print(d)

a=int(input("enter number"))
digit(a)
'''
'''
#find sum of first and last digit of a number.

def sum(d):
    s=d%10
    while d>10:
        d=d//10
        print(d+s)

a=int(input("enter number"))
sum(a)
'''

#swap first and last digits of a number(unsolved)
'''
def swap(d):
    s=d%10
    while d>10:
        d=d//10
        if 
'''
#check whether a number is Prime number or not
'''
n=4

i=2
s=0
while i<5:
    
    if n%i==0:
        s=1
        break
    i=i+1
if s==0:
    print("prime")
else:
    print("not")
'''
'''
def prime_number(n):
    i=2
    s=0
    while i<n:
        if n%i==0:
            s=1
            break
        i=i+1
    if s==0:
        print("prime")
    else:
        print("not")

a=int(input("enter number"))
prime_number(a)
'''
'''
# sum of all prime numbers between 1 to n
for n in range(1,100):
   

    i=2
    s=0
    sum=0
    while i<n:
        
        if n%i==0:
            s=1
            break
        i=i+1
        sum 
    if s==0:
        print(n," prime")
    else:
        print(n," not")
    
'''
'''
def number(n):
    i=0
    while i<=n:
        print(i)
        i=i+1
 
a=int(input("enter number"))
number(a)
'''
#find all factors of a number
'''
#wrong
for n in range(1,100):
    i=1
    while i<n:
        if n%i==0:
            print(i)
            i=i+1
'''
'''
def factor_number(n):
    i=1
    while i<n:
        if n%i==0:
            print(i)
        i=i+1
a=int(input("enter  frist number"))
factor_number(a)
'''
'''
#calculate factorial of a number.

def factorial_number(n):
    i=2
    while n>1:
        i=i*n
        n=n-1
        print(i)
a=int(input("enter frist number"))
factorial_number(a)

'''
'''
n=5 #factorial
i=1
while n>1:
    i=i*n
    n=n-1
    print(i)
'''
'''
def factorial(f):
    i=1
    while f>=1:
        i=f*i
        f=f-1
        print(i)
a=int(input("enter  number"))
factorial(a)
'''
'''
#print frist and last digit an factoral
def digit(d):
    while d!=0:
        r=d%10
        m=1
        for i in range(1,r+1):
            m=m*i
        print(m)
        d=d//10
    
a=int(input("enter number"))
digit(a)
'''

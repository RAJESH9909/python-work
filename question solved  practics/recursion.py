
#l[0],l[1]
'''
def p(l,first):
    if first==len(l):
        return 1
    else:
        print(l[first])
        return p(l,first+1)

    4==4
    print(l[1])
    [1,2,3,4],4
    
1
2
3
4
p([1,2,3,4,5],0)
'''
'''
def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    elif c>a and c>b:
        return c
a=1
b=2
c=3
print(greatest(a,b,c))
'''

# feranhit to celcius
'''
def f_to_c(f):
    return 5*(f-32)/9
f=int(input("enter feranhit"))
print(f_to_c(f))
'''
# print all natural numbers from 1 to n ::using  recursion
'''
def number(n):
    if n==0:
        return
    number(n-1)
    print(n)
a=int(input("enter number"))
number(a)
'''
'''
#l[0],l[1]

def p(l,first):
    if first==len(l):
        return 1
    else:
        print(l[first])
        return p(l,first+1)

    4==4
    print(l[1])
    [1,2,3,4],4
    
1
2
3
4
p([1,2,3,4,5],0)
'''

#to print all natural numbers in reverse (from n to 1).us-ing recursion
"""
def number_reverse(r):
    if r==0:
        return
    print(r)
    number_reverse(r-1)
    
a=int(input("enter number"))
number_reverse(a)
"""
#Write a  program to print all alphabets from a to z. - using recursion
'''
def alphabets(a):
    if a<97:
        return
    alphabets(a-1)
    print(chr(a))
alphabets(122)
#n=int(input("enter number"))
#alphabets(n)
'''
#write a program print even number 1 to 100 using  recursion
'''
def even(e):
    if e==0:
        return
    even(e-1)
    if e%2==0:
    else:
        
        print(e)
even(100)
#a=int(input("enter number"))
#even(a)
'''
# all odd number between 1 to 100. using recursion
'''
def odd(d):
    if d==0:
        return
    odd(d-1)
    if d%2!=0:
        print(d," odd :")
a=int(input("enter number"))
odd(a)
'''
#find sum of all natural numbers between 1 to n using recursion
'''
def sum(n,s=0):
    if n==0:
        return 1
    else:
        s=s+n
        print(s)
        sum(n-1,s)
    

a=int(input("enter number"))
sum(a)
'''
#second methard
'''
def sum(n):
    if n == 0:
        return 0

    d = sum(n - 1)
    f = n + d

    return f

a = int(input("enter number"))
print(sum(a))
'''
#sum of all even numbers between 1 to n
'''
def even(n):
    if n==0:
        
        return
        d=even(n-1)
        if d%2==0:
            print(d)


a=int(input("enter number"))#5
print(even(a))
'''
"""
# hts
def even(e,s=0):
    if e==0:
        return 0
    
    else:
        if e%2==0:
            s=s+e
            print(s)
        
        even(e-1,s)
        
    

a=int(input("enter number"))
(even(a))
"""
#Write a  program to count number of digits in a number.
"""
def count(n,c=0):
    if n==0:
        return
    else:
        n=n//10
        c=c+1
        print(c)
        count(n,c)
        

a=int(input("enter number"))
count(a)
"""
# Write a  program to print multiplication table of any number using recursion

#frist methard
"""
def table(n,i=1):
    if i>10:
        
        return 
    else:
        print(n*i)
        table(n,i+1)

a=int(input("enter number : "))
table(a)
"""
#second methard(wrong)
"""
def table (n,i=1,series=[]):
    
    if i>10:
        return series
    else:
        series.append(n*i)
        return table (n,i+1, series)
    
a=int(input("enter number"))
table(a)
"""
"""
a=int(input("enter number: "))
i=0
while i<10:
    i=i+1
    print(i*a)
"""

#Write a  program to find first and last digit of a number using recursion
def digit(n):
    f=""
    # print(n//10!=0,f,n)
    if n//10!=0:
        n=n//10
        f=digit(n)
        return f
    else:
        return n

a=int(input("enter  number"))
print("first:",digit(a))

def digit(n, last):
    if n < 10:
        print("first:", n)
        print("last:", last)
        return

    digit(n // 10, last)


a = int(input("enter number: "))
digit(a, a % 10)

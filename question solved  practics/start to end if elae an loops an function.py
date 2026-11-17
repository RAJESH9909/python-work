#Write a  program to find maximum between two numbers.
'''
def maxium(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
       return(b)
    elif c>a and c>b:
        return(c)
a=1
b=2
c=3
print(maxium(a,b,c))
'''
'''
a=int(input("enter frist number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))
if a>b and a>c:
    print ("a is greater")
elif b>a and b>c:
    print("b is greater" )
elif c>a and c>b:
    print("c is greater")
else:
    print("both are same")
'''
'''
#Write a  program to check whether a number is negative, positive or zero
a=int(input("enter number: "))
if a>0:
    print("positive")
elif a<0:
    print("negative")
elif a==0:
    print("zero")
'''
'''
def chek_number():
    if a>0:
        print("positive")
    elif a<0:
        print("negative")
    elif a==0:
        print("zero")
a=int(input("enter number: "))
chek_number()
'''
'''
#program to check whether a number is divisible by 5 and 11 or not.
a=int(input("enter number"))

if a%5==0 or a%11==0:
    print("divisible")
else:
    print("not")
'''
'''
def divisible():
    if a%5==0 or a%11==0:
        print("divisible")
    else:
        print("not")

a=int(input("enter number"))
divisible()
'''
'''
#program to check whether a number is even or odd:
a=int(input("enter number"))
if a%2==0:
    print("a is even")
else:
    print("odd")
    pass

def chek_number(a):
    if a%2==0:
        print("a is even")
    else:
        print("odd")
n=int(input("enter number"))
chek_number(n)
'''

#check whether a year is leap year or not.
'''
#check whether a character is alphabet or not
a=input("enter number")

if a.isalpha():
    print("yes")
else:
    print("not")
    pass
def alphabet_check(a):
    
    if a.isalpha():
       print("yes")
    else:
        print("not")
        
n=input("enter charactor")
alphabet_check(n)
'''
'''
#Write a  program to input any alphabet and check whether it is vowel or con-sonant
a=input("enter alphabet")
if a=="a" or a=="e" or a=="i" or a=="o" or a=="u":
    print("Vowel")
else:
    print("consonent")
    pass

def alphabet(a):
    if a=="a" or a=="e" or a=="i" or a=="o" or a=="u":
        print("Vowel")
    else:
        print("consonent")

n=input("enter alfabhate")
alphabet(n)
'''
'''
 #input any character and check whether it is alphabet, digit or special character
a=input("enter number")
if a.isalpha():
    print("afabhet")
elif a.isdigit():
    print("digit")
else:
    print("special charactor")
    pass

def cheak():
    if a.isalpha():
        print("afabhet")
    elif a.isdigit():
        print("digit")
    else:
        print("special charactor")

a=input("enter number")
cheak()  
'''
'''
#Write a  program to input week number and print week day.
a=int(input("enter number"))

if a==1:
    print("monday")
if a==2:
    print("thuesday")
if a==3:
    print("wednesday")
if a==4:
    print("thrusday")
if a==5:
    print("friday")
if a==6:
    print("saturday")
if a==7:
    print("sunday")
else:
    print("wrong number")
    pass

def number(a):
    if a==1:
        print("monday")
    if a==2:
        print("thuesday")
    if a==3:
        print("wednesday")
    if a==4:
        print("thrusday")
    if a==5:
        print("friday")
    if a==6:
        print("saturday")
    if a==7:
        print("sunday")
    else:
        print("wrong")

n=int(input("enter number"))
number(n)
'''
'''
#Write a  program to input month number and print number of days in that month
a=int(input("enter month number"))
if a==1:
    print("january :" ,  " 31")
elif a==2:
    print("feburary :",28,29)

    pass

def number():
    if a==1:
        print("january :" ,  " 31")

a=int(input("enter month  : "))
number()
'''
#count total number of notes in given amount
'''
#input angles of a triangle and check whether triangle is valid or not.
a=int(input("enter triangle: "))
b=int(input("enter triangle: "))
c=int(input("enter triangle: "))

if a+b+c==180:
    print("triangle is valid")
else:
    print("not valid")
    pass

def triangle():
    a=int(input("enter triangle: "))
    b=int(input("enter triangle: "))
    c=int(input("enter triangle: "))

    if a+b+c==180:
        print("triangle is valid")
    else:
        print("not valid")
    
(triangle())
'''
'''
# Write a  program to calculate profit or loss
a=int(input("sell price : "))
b=int(input("buy price : "))

if a-b>0:
    print("profit")
else:
    print("loos")
    pass

def calculate():
    a=int(input("sell price : "))
    b=int(input("buy price : "))

    if a-b>0:
        print("profit")
    else:
        print("loos")
calculate()
'''
'''
Write a  program to input marks of five subjects Physics, Chemistry,
Biology, Mathematics and Computer. Calculate percentage and grade according to following:
                                   Percentage >= 90% : Grade A
                                   Percentage >= 80% : Grade B
                                   Percentage >= 70% : Grade C
                                   Percentage >= 60% : Grade D
                                   Percentage >= 40% : Grade E
                                   Percentage < 40% : Grade F 
'''
'''
a=int(input("enter maths number"))
b=int(input("enter maths number"))
c=int(input("enter maths number"))
d=int(input("enter maths number"))
e=int(input("enter maths number"))

f=(a+b+c+d+e)/5
print(f)
if f>=90 and f<=100:
    print("grade a")
    
elif f>=80 and f<=90:
    print("grade b")
    
elif f>=70 and f<=80:
    print("grade c")
    
elif f>=60 and f<=70:
    print("grade d")
    
elif f>=40 and f<=50:
    print("grade e")
    
elif f<=40:
    print("grade f(fail)")

else:
    print("none")

    pass

def percentage():
    a=int(input("enter maths number"))
    b=int(input("enter maths number"))
    c=int(input("enter maths number"))
    d=int(input("enter maths number"))
    e=int(input("enter maths number"))

    f=(a+b+c+d+e)/5
    print(f)
    if f>=90 and f<=100:
        print("grade a")
    
    elif f>=80 and f<=90:
        print("grade b")
    
    elif f>=70 and f<=80:
        print("grade c")
    
    elif f>=60 and f<=70:
        print("grade d")
    
    elif f>=40 and f<=50:
        print("grade e")
    
    elif f<=40:
        print("grade f(fail)")

    else:
        print("none")
        percentage()

'''
'''
#Write a  program to input electricity unit charges and calculate total
#electricity bill according to the given condition:
                                  For first 50 units Rs. 0.50/unit
                                  For next 100 units Rs. 0.75/unit
                                 For next 100 units Rs. 1.20/unit
                                 For unit above 250 Rs. 1.50/unit

'''
'''
a=int(input("enter unit number"))

if a<=50:
      print(0.50*a)
elif  a>50 and a<=100:
    print(a*0.75)
elif a>100 and a<=200:
    print(a*1.20)
elif a>200 and a<250:
    print(1.50*a)
elif a>250:
    print(1.50*a)
'''
# 1 question pending  tv wala

#loop an interigation
'''
#program to print all natural numbers from 1 to n. - using while loop

'''
'''
n=int(input("enter number"))

for i in range(1,n):
    print(i)
    pass
def number(n):
    i=0
    while i<n:
        print(i)
        i=i+1
a=int(input("enter nnumber"))
number(a)
    pass
a=int(input("enter nnumber"))
i=0
while (i<a):
    print(i)
    i=i+1
'''
# program to print all natural numbers in reverse(from n to 1) us-ing while loop
'''
def reverse(a):
    i=a
    while i>=1:
        print(i)
        i=i-1
        

n=int(input("enter number: "))
reverse(n)


n=int(input("enter number"))
i=n
while i>=1:
    print(i)
    i=i-1 
'''
# program to print all alphabets from a to z. - using while loop
"""
for i in range(97,123):
    print(chr(i))
"""
'''
def alphabets(a):
    i=97
    while (i<=a):
        print(chr(i))
        i=i+1
n=int(input("enter number"))
alphabets(n)
'''
'''
n=int(input("enter number"))
i=97
while (i<=n):
    print(chr(i))
    i=i+1
'''
#print all even numbers between 1 to 100.
#- using while loop
'''
for i in range(1,101):
    if i%2==0:
        print(i,"even")
    else:
        print(i,"odd")
'''
'''
def even(a):
    i=0
    while i<=a:
        if i%2==0:
            print("even :",i)
        else:
            print("odd :",i)
        i=i+1
n=int(input("enter number"))
even(n)
'''
'''
n=int(input("enter number"))
i=0
while i<=n:
    if i%2==0:
        print("even :",i)
    else:
        print("odd :",i)
    i=i+1
'''
#sum of all natural numbers between 1 to n
'''
n=int(input("enter number"))
s=0
for i in range(1,n+1):
    s=s+i
    print(s)
'''
'''
def sum(a):
    i=0
    s=0
    while i<=a:
        s=s+i
        print(s)
        i=i+1

n=int(input("enter number"))
sum(n)
'''
#find sum of all even numbers between 1 to n
'''
def sum_even(a):
    s=0
    i=0
    while i<=a:
        if i%2==0:
            s=s+i
            print(i,s)
        i=i+1
n=int(input("enter number"))
sum_even(n)

pass

s=0
a=int(input("enter number"))
for i in range(1,a+1):
    if i%2==0:
        s=s+i
        print(s,"sum of number")

'''
#find sum of all odd numbers between 1 to n.
'''
s=0
a=int(input("enter number"))
for i in range(1,a+1):
    if i%2!=0:
        s=s+i
        print(s,"sum of number")
pass
def sum_odd(a):
    s=0
    i=0
    while i<=a:
        if i%2!=0:
            s=s+i
            print(i,s)
        i=i+1
n=int(input("enter number"))
sum_odd(n)
'''
#print multiplication table of any number
'''
n=int(input("enter number"))
for i in range(1,11):
    print(i*n)
'''
'''
def multiplaction(r):
    i=1
    while i<=10:
        print(i*r)
        i=i+1
a=int(input("enter number"))
multiplaction(a)
'''
#program to count number of digits in a number.
'''
def count(d):
    c=0
    while d!=0:
        c=c+1
        d=d//10
    print(c)

a=int(input("enter number"))
count(a)
'''
"""
a=int(input("enter frist number: "))
count=0
while a!=0:
    count=count+1
    a=a//10
print(count)
"""
#find first and last digit of a number
#second methard unsolved:
"""
def find_digit(d):
    print(d%10)
    while d>10:
        d=d//10
    print(d)

a=int(input("enter number"))
find_digit(a)
"""
#find sum of first and last digit of a number.
'''
def sum(d):
    l=d%10
    while (d>10):
        d=d//10
    print(d+l)

a=int(input("enter number: "))
sum(a)
'''

'''
#second methard
def sum_f(d):
    f=d%10
    while d>10:
        d=d//10
    print(f+d)

a=int(input("enter number"))
sum_f(a)
'''
'''
#third methard

a=int(input("enter number"))
l=a%10
while a>10:
    a=a//10
print(a+l)
'''
#swap first and last digits of a number.
#1.st not solved
'''
def swap(a):
    l=a%10
    while a>10:
        a=a//10
    print(a,l)

s=int(input("enter number"))
swap(s)
'''
'''
def swap():
    l=[]
    for i in str():
        l.append(i)
        l[0],l[-1]=l[-1],l[0]
        print(' '.join(l))
        while true:
                c=int(input("enter number" ))
                swap(c)

'''    
# program to calculate sum of digits of a number
'''
def sum_digit(s):
    sm=0
    while(s!=0):
        d=s%10#5,4,3
        sm=sm+d#5,9,12
        s=s//10#34,3,0
        print(sm)
a=int(input("enput number"))
sum_digit(a)#345
'''
'''
#2nd methard
s=int(input("enput number"))
sm=0
while(s!=0):
    d=s%10
    sm=sm+d
    s=s//10
    print(sm)
'''    
# program to calculate product of digits of a number
'''
def product_digit(d):
    s=1
    
    while d>0:
        l=d%10
        s=s*l
        d=d//10
    print(s)
a=int(input("enter number"))
product_digit(a)
'''
'''
a=int(input("enter number"))
s=1
while a>0:
    l=a%10
    s=s*l
    a=a//10
print(s)
'''
# program to enter a number and print its reverse.

def reverse(d):
    i=0
    while i<d:
        r=d%10
        d=d//10
        i=i+1
        
        print(reverse)
a=int(input("enter number"))
reverse(a)
    
    
    


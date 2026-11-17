"""
a=10
b=10
print(a+b)
# this is variable

a="aman123"
# this is string(collection of data
concate +
repitition *

"""

"""
a="aman123"
b="kumar"

#print(a+b)
#print(a*b) it is incorrect
print(a*2)
print(b*2)
"""
#operater
"""
a="hallo"
print(a[0]) this is called index
print(a[0:5])# this is called index
"""
"""
a=[101,"aman",67000,]# its called list
b=[2,1,3]
#print(a+b)
print(a[0:3]) #this is called index
a.append(90)
print(a)# append last index
a.insert(2,"rajesh")#  frist me kis index pe kya paste karna hai
print(a)
a.pop()# remove last
print(a)
a.remove(67000)# list me se kon sa argument hatana hai
print(a)
"""
"""
# tuple-- it is immutable(non -changeble(jaise ham list me change kar lete the isme nahi kar sakte ))
#tuple me ham bas index and count  karte hai

a=(121,"aman",70000.00)
#print(a[:3])# its called indexing
a.count(121)#not work but called aisa he ho raha hai
print(a)
"""
"""
#diticnoary--key value define
a={"name":"rajesh","rollno":121}
print(a["name"])
print(a["rollno"]) #1st index key 2nd index value
"""
"""
#set
a={2,1,3,2,1,4,5,3,5}
print(a) #it is called set like teda medha unorthorige  ko ek saath me indexing arta hai
"""
"""
#boolean--true false--,yani (are and or)

#arithmatis operater--- +,*,-,/,//,**

#logic --and , or

# control statement ---if else
"""

#Write a  program to find maximum between two numbers.
"""
a=int(input("enter frist number: "))#integer-- (positive,negitive,zero,(+,-,0)) koi v number
b=float(input("enter second number: "))#floting point(.)

if a>b:
    print("a is greater")
elif b>a:
    print("b is greater")
else:
    print("error")
"""
#Write a  program to find maximum between three numbers.
"""
a=int(input("enter  frist number"))
b=int(input("enter seconnd number"))
c=int(input("enter third number"))

if a>b and a>c:
    print(" a is greater ")
    
elif b>c and b>a:
    print("b is greater")
elif c>a and c>b:
    print("C is greater")
else:
    print("equal" ,"error")
"""
#Write a  program to check whether a number is negative, positive or zero.
"""
a=int(input("enter number"))
if a>0:
    print("positive")
elif a<0:
    print("negative")
else:
    print("zero")
"""
#Write a  program to check whether a number is divisible by 5 and 11 or not

"""
a=int(input("enter number : "))
if a/5==0 and a/11==0:
    print("yes")
else:
    print("not")
    
"""
#Write a  program to check whether a number is even or odd
"""
a=int(input("enter number"))
if a%2==0:
    print("even")
elif a%2!=0:
    print("odd")
"""
#Write a  program to check whether a character is alphabet or not.
"""
a=input("enter alphabate")
if a.isalpha():
    print("yes")
else:
    print("not")
"""
#   Write a  program to input any alphabet and check whether it is vowel or con-sonant.
"""
a=input("enter alphabet")
if a in "aeiou":
    print("vowel")
else:
    print("consonant")
"""
#Write a  program to input any character and check whether it is alphabet, digit or special character.

"""
a=input("enter character")
if a.isalpha():
    print("alphabet")
elif a.isdigit():
    print("digit")
else:
    print("special character")
"""
#Write a  program to check whether a character is uppercase or lowercase al-phabet.
'''
a=input("enter character")

if a.isupper():
    print("uppercase")
elif a.islower():
    print("lowercase")
elif a.isdigit():
    print("digitt")
'''
#Write a  program to input week number and print week day.
"""
a=int(input("enter number"))

if a==1:
    print("monday")
elif a==2:
    print("tuesday")
elif a==3:
    print("wednesday")
elif a==4:
    print("Thursday")
elif a==5:
    print("Friday")
elif a==6:
    print("saturday")
elif a==7:
    print("Sunday")
"""


#Write a  program to input month number and print number of days in that month.
"""
a=int(input("enter  numberr"))

if a==1:
    print("january, 31 days")
elif a==2:
    print("feburary, 28,29,days")
elif a==3:
    print("march, 31,days")
elif a==4:
    print("april, 30days")
elif a==5:
    print("may, 31,days")
elif a==6:
    print("june 30,days")
elif a==7:
    print("july, 31,days")
elif a==8:
    print("august 31,days")
elif a==9:
    print("september, 30,days")
elif a==10:
    print("october, 31,days")
elif a==11:
    print("November 30,days")
elif a==12:
    print("december, 31,days")
"""
# Write a  program to input angles of a triangle and check whether triangle is valid or not
"""
a=int(input("enter trangle"))
b=int(input("enter second tranngle"))
c=int(input("enter third trangle "))

if a+b+c==180 and a>0 and b>0 and c > 0:
    print("trangle is valid")
else:
    print("not")
"""
#Write a  program to calculate profit or loss.
"""
a=int(input("buy price"))
b=int(input("sell price"))

if b-a>0:
    print("profit")
elif b==a:
    print("none")
else:
    print("loose")
"""
# Write a  program to input marks of five subjects Physics,
#Chemistry, Biology, Mathematics and Computer. Calculate
#percentage and grade according to following:
           # Percentage >= 90% : Grade A
           # Percentage >= 80% : Grade B
           # Percentage >= 70% : Grade C
           # Percentage >= 60% : Grade D
           # Percentage >= 40% : Grade E
           # Percentage < 40% : Grade F
"""
a=int(input("enter english marks"))
b=int(input("enter  biology marks"))
c=int(input("enter  chemistry marks"))
d=int(input("enter  physics marks"))
e=int(input("enter  math marks"))
f=a+b+c+d+e
g=f/5

if g>90 and g<100:
    print("grade a")
elif g>80 and g<90:
    print("grade b")
elif g>70 and g<80:
    print("grade c")
elif g>60 and g<70:
    print("grade d")
elif g>50 and g<60:
    print("grade e")
elif g>=40 and g<50:
    print("grade f")
elif g<40:
    print("graed g")
"""
#Write a  program to input electricity unit charges and calculate total electricity bill according to the given condition:
   #For first 50 units Rs. 0.50/unit
   #For next 100 units Rs. 0.75/unit
   #For next 100 units Rs. 1.20/unit
   #For unit above 250 Rs. 1.50/unit
"""
a=int(input("enter electricity unit"))

if a>50 and a<=100:
      print(a*0.50)
elif a>100 and a<=200:
    print(a*0.75)
elif a>200 and a<=250:
    print(a*1.20)
elif  a>250:
    print(a*1.50)
else:
    print("none of charges")
"""

#loops and iteragtion [Also using function & recultion]

# Write a  program to print all natural numbers from 1 to n. - using while loop
"""
# for loop
a=int(input("enter number"))

for a in range (1,a+1):
    print(a)
"""
"""
# while loop

a=int(input("enter number"))
i=0
while i<a:
    i=i+1
    print(i)
"""
"""
#function

def number(n):
    i=0
    while i<n:
        i=i+1
        print(i)

a=int(input("enter number"))
number(a)
"""
"""
#recultion

def number(n):
    if n==0:
        return
    number(n-1)
    print(n)
a=int(input("enter number: "))
number(a)
"""
# Write a  program to print all natural numbers in reverse (from n to 1). -    us-ing while loop

"""
# for loop

a=int(input("enter number"))
for a in range(a,0,-1):
    print(a)
"""
#while loop
"""
a=int(input("enter number"))
i=a
while i>=1:
    print(i)
    i=i-1
"""
#function
"""
def reverse(n):
    i=n
    while i>=1:
        
        print(i)
        i=i-1
a=int(input("enter number"))
reverse(a)
"""
#recultion
"""
def reverse(n):
    if n==0:
        return
    print(n)
    reverse(n-1)
    
a=int(input("enter number"))
reverse(a)
"""
## Write a  program to print all alphabets from a to z. - using while loop
"""
# for loop
for i in range(97,123):
    print(chr(i))
"""
"""
#while loop

i=97
while i<123:
   # i=i+1
    print(chr(i))
    i=i+1
"""
#function (for loop)
"""
def alphabet(a):
    for i in range(a,124):
        print(chr(i))
              
n=int(input("enter number"))
alphabet(n)
"""
"""
#function (while loop)
def alphabet(n):
    n=0 #n=97
    while n<122:
        print(chr(n))
        n=n+1
a=int(input("enter number"))# ya a=input("enter alfabet")
alphabet(a)
"""    
#recursion
"""
def alphabet(n):
  if  n<97:
      return
  alphabet(n-1)
  print(chr(n))

#alphabet(123)
a=int(input("enter number"))
alphabet(a)
"""
# Write a  program to print all even numbers between 1 to 100. - using while loop

#for loop
"""
for i in range(1,101):
    if i%2==0:
        
        print("even:-->",i)
"""
#while loop
"""
a=int(input("enter number: "))
i=1
while i<=a:
    if i%2==0:
       print(i,"even")
    i=i+1
"""
#function (for loop)
"""
def even(n):
    for n in range(1,n+1):
        if n%2==0:
            print(n,"even")
a=int(input("enter number"))
even(a)
"""
#function while loop
"""
def even(n):
    i=1
    while i<=n:
        if i%2==0:
            print(i)
        i=i+1
a=int(input("enter number"))
even(a)
"""
#recursion
"""
def even(n):
    
    if n==1:
        return
    even(n-1)
    if n%2==0:
        print(n)

a=int(input("enter number"))
even(a)
"""
#Write a  program to print all odd number between 1 to 100.

#for loop
"""
for i in range (1,100):
    if i%2!=0:
        print(i,"odd")
"""
#while loop
"""
a=int(input("enter  number"))
i=1
while i<=a:
    if i%2!=0:
        print(i,"odd")
    i=i+1
"""
#function--for loop
"""
def odd(n):
    for i in range (1,n+1):
        if i%2!=0:
            print(i,"odd")

a=int(input("enter number"))
odd(a)

"""
#function -->while loop
"""
def odd(n):
    i=1
    while i<=n:
        if i%2!=0:
            print(i,"odd")
        i=i+1
a=int(input("enter number: "))
odd(a)
"""
#recursion
"""
def odd(n):
    if n==0:
        return
    odd(n-1)
    if n%2!=0:
        print(n, "odd")
a=int(input("enter number"))
odd(a)
"""
#Write a  program to find sum of all even numbers between 1 to n
#for loop
"""
s=0
for i in range(1,101):
    if i%2==0:
        s=s+i
print(s)
"""
#while loop
"""
a=int(input("enter number"))
s=0
i=0
while i<=a:
    if i%2==0:
        s=s+i#0,2
        print(s)
    i=i+1
"""
#function-- for loop
"""
def sum(n):
    s=0
    for i in range(1,n+1):
        if i%2==0:
            s=s+i
            print(s)
a=int(input("enter number"))
sum(a)
"""
#function--> while loop
"""
def sum(n):
    i=0
    s=0
    while i<=n:
        if i%2==0:
            s=s+i
            print(s)
        i=i+1
a=int(input("enter number"))
sum(a)
"""
#recursion
"""
def sum(n,s=0):
    
    if n==0:
        return
    else:
        if n%2==0:
            s=s+n
            print(s)
        sum(n-1,s)
        
        
a=int(input("enter number"))
sum(a)      
"""

#2nd methard(wrong hai)
"""
def sum(n):
    if n==0:
        return
    d=sum(n-1)
    if d%2==0:
        f=d+n
        return f
    else:
        return d
a=int(input("enter number"))
sum(a)
"""
#Write a  program to find sum of all natural numbers between 1 to n.
#for loop
"""
a=int(input("enter number: "))
s=0
for a in range(1,a+1):
    s=s+a
print(s)
"""

#while loop
"""
a=int(input("enter number: "))
s=0
i=0
while i<=a:
    s=s+i
    i=i+1
    print(s)
"""
#function(for loop)
"""
def sum(n):
    s=0
    for i in range(1,n+1):
        s=s+i
    print(s)

a=int(input("enter number"))
sum(a)
"""
#function while loop
"""
def sum(n):
    s=0
    i=0
    while i<=n:
        s=s+i
        i=i+1
    print(s)
a=int(input("enter number"))
sum(a)
"""
#recursion
"""
def sum(n,s=0):
    if n==0:
        return
    else:
        
        s=s+n
        print(s)
        sum(n-1,s)
    
a=int(input("enter number"))
(sum(a))
"""

#Write a  program to find sum of all odd numbers between 1 to n
#for loop
"""
a=int(input("enter number"))
s=0
for i in range(1,a+1):
    if i%2!=0:
        s=s+i
        print(s)
"""
#while loop
"""
a=int(input("enter number"))
s=0
i=0
while i<=a:
    if i%2!=0:
        s=s+i
        print(s)
    i=i+1
"""
#function(for loop)
"""
def odd(n):
    s=0
    for i in range(1,n+1):
        if i%2!=0:
            s=s+i
            print(s)
a=int(input("enter number"))
odd(a)
"""
#function (while loop)
"""
def odd(n):
    s=0
    i=0
    while i<n:
        if i%2!=0:
            s=s+i
            print(s)
        i=i+1

a=int(input("enter numbe: "))
odd(a)
"""
#recultion
"""
def odd(n,s=0):
    if n==0:
        return
    else:
        if n%2!=0:
            s=s+n
            print(s)
        odd(n-1,s)

a=int(input("enter number"))
odd(a)
"""

#Write a  program to count number of digits in a number.

#while loop
"""
n=int(input("enter number"))
count=0
i=0
while n!=0:
    count=count+1
    n=n//10
    print(count)
"""
"""
def count(n):
    count=0
    while n!=0:
        count=count+1
        n=n//10
        print(count)

a=int(input("enter number: "))
count(a)
"""
# Write a  program to find sum of first and last digit of a number.
"""

def sum_num(n):
    l=n%10
    while n!=0:
        d=n//10
        print(l+d)
a=int(input("enter number: "))
sum_num(a)
"""
"""
def count(c,count=1):
    #count=0
    while c!=0:
        c=c//10
        count=count+1
    print(count)

a=int(input("enter numbber"))
count(a)
"""
def sum(n):
    l=n%10
    while n>10:
        
        n=n//10
        l=l+n
    print(l)
a=int(input("inter number: "))
sum(a)

'''
#statics
a=10
print(a)
b=10
print(b)
'''
'''
#danamic
a=?
b=?
print(a+b)
'''
'''
#variable
1a=10 (wrong)
a1=10(right)
a b= not allow space
'''
'''
#data types
a=10   (integer)
a=10.1 (float(decemial)

a=int(input("enter number"))
b=float(input("enter number"))
'''
'''
#sequence-order
#string-collection of charactor("a","b","c",1,2,3)
#1.concate=+
#1.repitition=*
a="aman"
b="brijesh"
print(a+b)
'''
'''
a=3
b=4
print(a+b)
print(a-b)
print(a*b)
'''
'''
#slice operator []
#[start:stop:step]
a="hello"
print(a[0])
print(a[0:3])
'''
'''
#list:collection of data[]
a=["aman",101,670000]
print(a[0])
print(a[1])
print(a[2])
print(a[0:3])
b=[1,2,3]
print(a+b)
'''
'''
function
1.append()
2.index()
3.insert()
4.pop()
5.remove
6.count()
a=["hallo",101,67000]
'''
'''
#tuple collection of data same as a list but tuple is non changeble
#list:multiple(index,append,insert,remove,pop,)
#tuple:immutable(index.count)
'''
'''
#dictinary -key of value{}
a={"name":"rajesh","rollno":21,"class":12}
print(a["name"])
'''
'''
#set- collaction of unique data{}
s={1,1,2,2,3,3,4,5,6,5}
print(s)
'''
'''
#boolean:- true,false
#operator:
1. arithmatic +,-,*,/,//,**
 %modulas(reminder)
2.#relational:>,<,>=,<=,1=,==
 a=10(a is equal 10)
 a==10(kya a equal hai 10 ka)
3.logic and or
4.bitusie
5.shift operator
6.assignment
'''
#control statement
#if else
'''
#1.find between two number
a=int(input("enter number"))
b=int(input("enter number"))
if a>b:
    print("a are max")
elif b>a:
    print("b are max")
else:
    print("equal")
'''
'''
#find between four number maxium
a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))
d=int(input("enter number"))
if a>b and a>c and a>d:
    print("a is greater")
elif b>c and b>a and b>d:
    print("b is maxium")
elif c>a and c>b and c>d:
    print("c is maxium")
elif d>a and d>b and d>c:
    print("d is greater")
else:
    print("equal")
'''
'''
#check  number is negative, positive or zero.
a=int(input("enter number"))
if a>0:
    print("positive")
elif a<0:
    print("negative")
else:
    print("zero")
'''
'''
#number is divisible by 5 and 11 or not
a=int(input("enter number"))
if a%5==0 and a%11==0:
    print("yes")
else:
    print("not")
'''
'''
# check whether a number is even or odd.
a=int(input("enter number"))
if  a%2==0:
    print("even")
else:
    print("odd")
'''
#check whether a year is leap year or not
'''
#check whether a character is alphabet or not
a=input("enter charactor")
if a.isalpha():
    print("alfabhate")
else:
    print("not")
'''
'''
# input c whether it is vowel
#or con-sonant.
ch=input("enter alfabhate")
if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
    print("vowel")
else:
    print("consonant")
'''
'''
#cheak alphabet digit or special charactor
a=input("enter charactor")
if a.isalpha():
    print("alfabhate")
elif a.isdigit():
    print("digit")
else:
    print("special charactor")
'''
'''
#character is uppercase or lowercase al-phabet.
a=input("enter charactor")
if a.isupper():
    print("uppercase")
elif a.islower():
    print("lowecase")
else:
    print("special charector")
'''
'''
#input week number and print week day
week=int(input("enter week number"))
if week==1:
    print("monday")
elif week==2:
    print("tuesday")
elif week==3:
    print("wednesday")
elif week==4:
    print("thrusday")
elif week==5:
    print("friday")
elif week==6:
    print("saturday")
elif week==7:
    print("sanday")
'''
'''
#input month number and print number of days in
#that month
a=int(input("enter month number"))
if a==1:
    print("january",31)
elif a==2:
    print("feburary",28,29)
elif a==3:
    print("march",31)
elif a==4:
    print("april",30)
elif a==5:
    print("may",31)
elif a==6:
    print("june",30)
else:
    print("error")
'''
'''
#input angles of a triangle and check whether
#triangle is valid or not.
a=int(input("enter trangle"))
b=int(input("enter trangle"))
c=int(input("enter trangle"))
if a+b+c==180:
    print("valid")
else:
    print("not")
'''
'''
#Write a  program to calculate profit or loss
a=int(input("enter buy price"))
b=int(input("enter sell  price"))
if b-a>0:
    print("profit")
elif b-a<0:
    print("loos")
'''
'''
#Write a  program to input marks of five subjects
   #             Percentage >= 90% : Grade A
   #             Percentage >= 80% : Grade B
   #             Percentage >= 70% : Grade C
   #             Percentage >= 60% : Grade D            Percentage >= 40% : Grade E
   #             Percentage < 40% : Grade F

a=int(input("enter math number"))
b=int(input("enter biology number"))
c=int(input("enter physics number"))
d=int(input("enter chemistry number"))
e=int(input("enter english number"))
p=(a+b+c+d+e)/5
if p>90 and p<100:
    print("grade a")
elif p>80 and p<90:
    print("grade b")
elif p>70 and p<80:
    print("grade c")
elif p>=60 and p<70:
    print("grade d")
else:
    print("fail")
'''
'''
#electricity unit charges and calculate
#  For first 50 units Rs. 0.50/unit
#  For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
a=int(input("enter electric unit"))
if a>50:
    print(a*0.50)
elif a>50 and a>100:
    print(a*0.75)
elif a>100 and a<250:
    print(a*1.20)
elif a>250:
    print(a*1.50)
'''
#loop and iteration
# print all natural numbers from 1 to n.using while loop
'''
n=12
for i in range(1,n+1):
    print(i)
'''
'''
#reverse (from n to 1). -    us-ing while loop
n=12
for i in range(n,1,-1):
    print(i)
'''
'''
#print all alphabets from a to z. - using while loop
for i in range (93,127):
    print(chr(i))
'''
'''
# print all even numbers between 1 to 100.using while loop
n=100
od=[]
en=[]
for i in range(1,n+1):
    if i%2==0:
        en.append(i)
    else:
        od.append(i)
print(en)
print(od)
'''
'''
#all odd number between 1 to 100.
od=[]
n=100
for i in range(1,n+1):
    if i%2!=0:
        od.append(i)
print(od)
'''
'''
#find sum of all natural numbers between 1 to n.
n=100
s=0
for i  in range(1,n+1):
    s=s+i
    print(s)
'''
'''
#find sum of all even numbers between 1 to n.
en=[]
n=10
s=0
for i in range(1,n+1):
    if i%2==0:
        s=s+i
        en.append(i)
print(s)
'''
'''
#sum of all odd numbers between 1 to n
od=[]
n=10
s=0
for i in range(1,n+1):
    if i%2!=0:
        s=s+i
        od.append(i)
print(s)
'''
'''
#print multiplication table of any number
a=int(input("enter number"))
for i in range(1,11):
    print(a*i)
'''
'''
#count number of digits in a number
a=87987
count=0
while a!=0:
    a=a//10
    count+=1
print(count)
'''
'''
#find first and last digit of a number.
a=87987
print(a%10)
while a>10:
    a=a//10
print(a)
'''
#find sum of first and last digit of a number.
'''
a=87987
s=0
l=a%10
while a>0:
    a=a//10
    print(a)
'''

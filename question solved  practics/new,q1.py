# if else question 
'''
a=int(input("enter frist number"))
b=int(input("enter second number"))

if a>b:
    print("frist num greater")
elif b>a:
    print("second num greater")
else:
    print("equal")
'''
'''
a=int(input("enter frist number"))
b=int(input("enter second number"))
c=int(input("enter three number"))
d=int(input("enter four number"))
e=int(input("enter five number"))

if a>b and a>c and a>d and a>e:
    print( "a is greater")
elif b>a and b>c and b>d and b>e:
    print("b is greater")
elif c>d and c>e and c>a and c>b:
    print("c is greater")
elif d>a and d>b and c>d and c>e:
    print("d is greater")
elif e>a and e>b and e>c and e>d:
    print("e is greater")
else:
    print("equal")
'''
'''
a=int(input("enter number"))

if a>0:
    print("positive")
elif a<0:
    print("negative")
else:
    print("zero")
'''
'''
a=int(input("enter number"))

if a%5==0 and a%11==0:
    print("true")
else:
    print("false")
'''
'''
a=int(input("enter number"))

if a%2==0:
    print("even")
else:
    print("odd")
'''
#question o
'''
a=int(input("enter angle"))
b=int(input("enter angle"))
c=int(input("enter angle"))

if a+b+c==180:
      print("valid")
else:
    print("not vallid")
'''
'''
#r.Write a  program to calculate profit or loss.

a=int(input("enter buy price"))
b=int(input("enter sell price"))

if b-a>0:
    print("profit")
else:
    print("loss")
'''
'''
#percentage

a=int(input("physics number"))
b=int(input("chemistry number"))
c=int(input("mathmatics number"))
d=int(input("biology number"))
e=int(input("english number"))

p=(a+b+c+d+e)/5

if p>90 and p<100:
    print("gread a")
elif p>80 and p<90:
    print("gread b")
elif p>70 and p<80:
    print("gread c")
elif p>60 and p<70:
    print("gread d")
elif p>40 and p<60:
    print("gread e")
elif p<40:
    print("f")
else: 
    print("fail")

'''
'''
#electricity bill

a=int(input("enter unit"))
if a<50:
    print(a*0.50)
elif a>50 and a<100:
    print(a*0.75)
elif a>100 and a<200:
    print(a*1.20)
elif a>200 and a<250:
    print(a*1.50)
else:
    print("error")
'''

# Write a  program to check whether a character is uppercase or lowercase al-phabet.
'''
ch=input("enter character")

if ch.isalpha():
    print("alfabhate")
    if ch.isupper():
        print("uppercase")
    else:
        print("lowecase")

    if ch=="a" or ch=="e" or ch=="i"or ch=="o" or ch=="u":
        print("vowel")
    else:
        print("consonant")
elif ch.isdigit():
    print("digit")
else:
    print("special creactor")
'''
'''
#digit not print
ch=input("enter character")
print(ch.isdigit())

if(ch.isalpha()== True):
    print("alfabhate")
elif (ch.isdigit() == True):
    print("digit")
else:
    print("special creactor")
'''

'''
ch=input("enter character")

if ch=="a" or ch=="e" or ch=="i"or ch=="o" or ch=="u":
    print("vowel")
else:
    print("consonant")
'''
'''
ch=input("enter character")

if ch.isupper():
    print("uppercase")
elif ch.islower():
    print("lowecase")
else:
    print("special creactor")
'''

# k.	Write a  program to input week number and print week day
'''
w=int(input("enter week days number"))

if w==1:
    print("monday")
elif w==2:
    print("tuesday")
elif w==3:
    print("wednesday")
elif w==4:
    print("thursday")
elif w==5:
    print("friday")
elif w==6:
    print("saturday")
elif w==1:
    print("sunday")
else:
    print("error")
'''
# l.Write a  program to input month number and print number of days in that month.
'''
m=input("enter month number an valid days")

if m=="january" or m=="1":
    print("31")
else:
    print("not")
'''

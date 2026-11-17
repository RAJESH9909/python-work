'''
#Write a  program to find maximum between two numbers.
a=int(input("enter frist number"))
b=int(input("enter  second number"))

if a>b:
    print("a is max")
elif b<a:
    print("b is max")
else:
    print("equal")
'''
'''
#Write a  program to find maximum between three numbers.
a=int(input("enter frist number"))
b=int(input("enter second number"))
c=int(input("enter third number"))

if a>b and a>c:
    print("a is greater")
elif b>c and b>a:
    print("b is greater")
elif c>a and c>b:
    print("c is greater")
else:
    print("equal")
'''
'''
#write a  program to check whether a number is negative, positive or zero

a=int(input("enter number"))

if a>0:
    print("positive")
elif a<0:
    print("negative")
else:
    print("zero")
'''
'''
#Write a  program to check whether a number is divisible by 5 and 11 or not
a=int(input("enter number"))
if a%5==0 and a%11==0:
    print("yes")
else:
    print("not")
'''
'''
#Write a  program to check whether a number is even or odd
a=int(input("enter number"))
if a%2==0:
    print("even")
else:
    print("odd")
'''
'''
#Write a  program to check whether a character is alphabet or not.
a=input("enter character")
if a.isalpha():
    print("yes")
else:
    print("not")
'''
'''
#Write a  program to input any alphabet and check whether it is vowel or con-sonant
ch=input("enter charactor")

if ch=="a" or ch=="e" or  ch=="i" or ch=="o" or ch=="u":
    print("vowel")
else:
    print("conso-nant")
'''
'''
#Write a  program to input any character and check
#whether it is alphabet, digit or special character.

a=input("enter any character")
if a.isalpha():
    print("alphabet")
elif a.isdigit():
    print("digit")
else:
    print("special creactor")
'''
'''
#Write a  program to check whether a character is
#uppercase or lowercase al-phabet.
a=input("enter character")
if a.isupper():
    print("upper")
elif a.islower():
        print("lower")
'''
'''
#Write a  program to input week number and
#print week day.
a=int(input("enter week"))
if a==1:
    print("sunday")
elif a==2:
    print("monday")
elif a==3:
    print("tuesday")
elif a==4:
    print("wednesday")
elif a==5:
    print("thursday")
elif a==6:
    print("friday")
elif a==7:
    print("saturday")
else:
    print("error")
'''
#Write a  program to count total number of
#notes in given amount.
'''
#Write a  program to input angles of a
#triangle and check whether triangle is
#valid or not.

a=int(input("enter frist trangle"))
b=int(input("enter second trangle"))
c=int(input("enter third trangle"))

if a+b+c==180:
    print("valid")
'''
'''
#Write a  program to calculate profit or loss.

a=int(input("buy price"))
b=int(input("sell price"))

if b-a>0:
    print("profit")
else:
    print("loos")
'''
'''
#Write a  program to input marks of five
#subjects Physics, Chemistry, Biology,
#Mathematics and Computer. Calculate
#percentage and grade according to following:
 #       Percentage >= 90% : Grade A
 #       Percentage >= 80% : Grade B
 #       Percentage >= 70% : Grade C
 #      Percentage >= 60% : Grade D
 #      Percentage >= 40% : Grade E
 #      Percentage < 40% : Grade F

a=int(input("enter physics number"))
b=int(input("enter chemistry number"))
c=int(input("enter biology number"))
d=int(input("enter mathmatics number"))
e=int(input("enter computer number"))
f=(a+b+c+d+e)/5
if f>90 and f<100:
    print("grade a")
elif f>80 and f<90:
    print("grade b")
elif f>70 and f<80:
    print("grade c")
elif f>60 and f<70:
    print("grade d")
elif f>40 and f<60:
    print("grade e")
else:
    print("grade  f")
'''
'''
#Write a  program to input electricity unit
#charges and calculate total electricity bill
#according to the given condition:
#     For first 50 units Rs. 0.50/unit
#    For next 100 units Rs. 0.75/unit
#    For next 100 units Rs. 1.20/unit
#    For unit above 250 Rs. 1.50/unit

a=int(input("enter electric unit"))
if  a<51:
    print(a*0.50)
elif a>50 and a<100:
    print(a*0.75)
elif a>100 and a<250:
    print(a*1.20)
elif a>250:
    print(a*1.50)
'''
'''
ch=input("enter charactor")

if ch.isalpha():
    print("alfabhate")
    if ch.isupper():
        print("uppercase")
    elif ch.islower():
            print("lowercase")
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
        print("vowel")
    else:
        print("consonant")
elif ch.isdigit():
    print("digit")
else:
    print("special creactor")
'''

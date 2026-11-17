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
program to check whether a number is even or odd

    
    

#if-else condition


#Write a  program to find maximum between two numbers.
"""
a=int(input("enter number"))
b=int(input("enter number"))
if a>b:
    print("a is greater")
elif(b>a):
    print("b is greater")
else:
    print("equal,error")
"""
#b.	Write a  program to find maximum between three number
""" 
a=int(input("enter number"))
b=int(input("enter number"))
if a>b and a>c:
    print("a is greater")
elif(b>a) and b>c:
    print("b is greater")
elif c>a and c>b:
    print("c is grater")
else:
    print("equal,error")
"""
#c.  	Write a  program to check whether a number is negative, positive or zero.
"""
a=int(input("enter number : "))

if a>0:
    print("positive")
elif a<0:
    print("negative")
elif a==0:
    print("zero")
"""
#d.	Write a  program to check whether a number is divisible by 5 and 11 or not.
"""
a=int(input("enter number: "))

if a%5==0 and a%11==0:
    print("yes")
else:
    print("not")
"""
#	Write a  program to check whether a number is even or odd.
"""
a=int(input("enter number"))
if a%2==0:
    print("even")
else :
    print("odd")
"""
# Write a  program to check whether a character is alphabet or not.
"""
a=input("enter character")
if a.isalpha():
    print("yes")
else:
    print("not")
"""
# h.	Write a  program to input any alphabet and check whether it is vowel or con-sonant.
"""
a=input("enter character")
if a in "aeiou":
#if a=="a,e,i,o,u":
    print("vowel")
else:
    print("consonant")
"""
#Write a  program to check whether a character is uppercase or lowercase al-phabet.
#Write a  program to input any character and check whether it is alphabet, digit or special character.
"""
a=input("enter subject")
if a.isalpha() and a.isupper():
    print("uppercaseaa"",  ""alphabet")  
elif a.isalpha() and a.islower():
    print("lowercase""  : "" alphabet")
elif a.isdigit():
    print("digit")
else:
    print("special cractor")
"""
#Write a  program to input week number and print week day.
"""
a=int(input("enter number"))
if a==1:
    print("monday")
elif(a==2):
    print("thusday")
elif a==3:
    print("wednesday")
"""
#Write a  program to input month number and print number of days in that month.
"""
a=int(input("enter number"))
if a==1:
    print("31"" ,""january")
    
elif a==2:
    print("28,29"" ,""februaru")
    
elif a==3:
    print("31"" ,""march")
    
elif a==4:
    print("30"" ,""april")
    
elif a==5:
    print("31"" ,""may")
    
elif a==6:
    print("30"" ,""june")
    
elif a==7:
    print("31"" ,""july")
    
elif a==8:
    print("31"" ,""august")
    
elif a==9:
    print("30"" ,""september")
"""
#Write a  program to input angles of a triangle and check whether triangle is valid or not.
#Write a  program to input all sides of a triangle and check whether triangle is valid or not.
"""
a=int(input("eneter number"))
b=int(input("enter number"))
c=int(input("enter bnumber"))

if a+b+c==180:
    print("valid trangle")
"""
#Write a  program to calculate profit or loss.
"""
a=int(input("enter sell price"))
b=int(input("enter buy price"))

if a-b>0:
    print("profit")
else:
    print("loss")
"""  
#Write a  program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. Calculate percentage and grade according to following:
#                               Percentage >= 90% : Grade A
#                               Percentage >= 80% : Grade B
#                               Percentage >= 70% : Grade C
#                               Percentage >= 60% : Grade D
#                               Percentage >= 40% : Grade E
#                               Percentage < 40% : Grade F

"""

a=int(input("enter Physics number"))
b=int(input("enter Chemistry number"))
c=int(input("enter Mathematics number"))
d=int(input("enter Computer number"))
e=int(input("enter biology  number"))
f=a+b+c+d+e 
g=f/5
if g>90 and g<100:
    print("gread A")
elif g>80 and g<=90:
    print("grade b")
elif g>70 and g<=80:
    print("grade c")
elif g>60 and g<=70:
    print("grade d")
elif g>50 and g<=60:
    print("grade e")
elif g<=40:
    print("fail")
"""


#loops

# write a program to print all nactural number form 1 to n-- using while loops:
"""
n=int(input("enter number"))
i=0
while i<n:
    i=i+1
    print(i)
    
"""
"""
n=int(input("enter number"))
for i in range(1,n+1):
    print(i)
""" 
#Write a  program to print all natural numbers in reverse (from n to 1). -    us-ing while loop

"""
a=int(input("enter  number"))
i=a
while i>0:
    print(i)
    i=i-1
"""
"""
a=int(input("enter number"))
for i in range(a,0,-1):
    
    print(i)

"""

#c)	Write a  program to print all alphabets from a to z. - using while loop
"""
a=int(input("enter number"))
i=97
while i<a:
    print(chr(i))
    i=i+1
"""
#d)Write a  program to print all even numbers between 1 to 100. - using while loop
"""
a=int(input("enter number"))
i=0
while i<a:
    i=i+1
    if i%2==0:
        print(i)
"""
#e)	Write a  program to print all odd number between 1 to 100.
"""
a=int(input("enter number"))
i=0
while i<a:
    i=i+1
    if i%2!=0:
        print(i)
"""
#Write a  program to find sum of all natural numbers between 1 to n.
"""
n=int(input("enter number"))

i=0
s=0
while i<n:
    i=i+1
    s=s+i
    print(s)
"""

#Write a  program to find sum of all even numbers between 1 to n.
"""
a=int(input("enter number"))
i=0
s=0
while i<a:
    i=i+1
    if i%2==0:
        s=s+i
        print(s)
"""
#g)	Write a  program to find sum of all odd numbers between 1 to n.
"""

a=int(input("enter number"))
i=0
s=0
while i<a:
    i=i+1
    if i%2!=0:
        s=s+i
        print(s)
"""
#i)	Write a  program to print multiplication table of any number.
"""
a=int(input("enter number"))
i=0
while i<10:
    i=i+1
    print(i*a)
"""
#j)	Write a  program to count number of digits in a number.
"""
n=int(input("enter number"))
count=0

while n!=0:
    n=n//10
    count=count+1
print(count)
"""
#Write a  program to find first and last digit of a number.
"""
n=int(input("enter number"))
print(n%10)
while n//10!=0:
    n=n//10
print(n)
"""
#Write a  program to calculate sum of digits of a number.
"""
n=int(input("enter number: "))
s=0
n=n%10
while n//10:
    n=n//10
    s=s+n
    print(s)56

"""


users = [
    {
        "name": "raja",
        "email": "raja123@gmail.com",
        "password": "raka@1123"
    },
    {
        "name": "ravi",
        "email": "ravi123@gmail.com",
        "password": "ravi_321"
    },
    {
        "name": "raka",
        "email": "rakaraka@gmail.com",
        "password": "432rakaraka"
    }
]


def login():
    email = input("Enter email: ")
    password = input("Enter password: ")

    for user in users:
        if email == user["email"] and password == user["password"]:
            print("Login successful")
            return

    print("Invalid email or password")


def register():
    name = input("Enter name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    for user in users:
        if email == user["email"]:
            print("Email already exists")
            return

    new_user = {
        "name": name,
        "email": email,
        "password": password
    }

    users.append(new_user)
    print("Registration successful")


def delete():
    email = input("Enter email to delete: ")

    for user in users:
        if email == user["email"]:
            users.remove(user)
            print("User deleted successfully")
            return

    print("User not found")


q = ""

while q != "0":
    print("\n1. Login")
    print("2. Register")
    print("3. Delete")
    print("0. Exit")

    q = input("Enter your choice: ")

    if q == "1":
        login()

    elif q == "2":
        register()

    elif q == "3":
        delete()

    elif q == "0":
        print("Exiting...")

    else:
        print("Invalid choice")

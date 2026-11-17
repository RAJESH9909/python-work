'''
#Write a  program to count number of digits
#in a number.
a=89837
count=0
print(a%10)
while a!=0:
    a=a//10
    count+=1
    print("value of a:",a)
    print(count)

 ''' 
'''
#Write a  program to find first and last
#digit of a number.
a=89837
print(a%10)
while a>10:
    a=a//10
print(a)
'''
'''
#Write a  program to find sum of first and
#last digit of a number

s=0
a=89837
l=a%10
while a>10:
    a=a//10
print(l+a)
'''
'''
#find maxium number

a=89837
max=0
while a!=0:
    r=a%10
    if(r>max):
        max=r
    a=a//10
print(max)
'''
#1423
#3421
'''
a=987654
min=9
while a!=0:
    r=a%10
    if(r<min):
        min=r
    a=a//10
print(min)

''''
'''
a=12
b=11
temp=a
a=b
b=temp
print(a)
print(b)
''''
a=1423

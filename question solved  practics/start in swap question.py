  and last digits of a number.

def swap (s):
    l=[]
    for i in str(s):
        l.append(i)
    l[0],l[-1]=l[-1],l[0]
    print(''.join(l))

while True:
    c=int(input("enter frist number: "))
    
    swap(c)
'''
'''
def swap (s):
    l=[]
    for i in str(s):
        l.append(i)
    l[0],l[-1]=l[-1],l[0]
    print(' '.join(l))

while True:
        c=int(input("enter frist number: "))
        swap (c)
'''
'''

#calculate sum of digits of a number.


def  sum_digit(d):
    s=0
    while d!=0:
        r=d%10
        s=s+r
        d=d//10
    print(s)

a=int(input("enter frist number: "))
sum_digit(a)

'''
'''
#calculate product of digits of a number.

def product_digit(d):
    s=1
    while d>
    0:
        r=d%10
        s=s*r
        d=d//10
    print(s)

a=int(input("enter  frist number: "))
product_digit(a)
'''
'''
#enter a number and print its reverse.

def reverse(r):
    for i in range(r,0,-1):
        print(i)

while True:
    a=int(input("enter  frist number: "))
    reverse(a)
'''
'''
#check whether a number is palindrome or not

def palindrome(p):
    #for i in range(1,p+1):
        if str(p)==str(p)[-1]:
            print(p)
        else:
            print("not palindrom: ")

while True :
    c=int(input("enter number"))
    palindrome(c)
'''
'''
def palindrome(n):
    temp=n
    rn=0
    while n!=0:
        r=n%10
        
        rn=rn*10+r
        n=n//10
    if temp==rn:
        print("palindrome because",temp,"=",rn)
    else:
        print("not palindrome",temp,"!=",rn)
a=int(input("enter frist number: "))
palindrome(a)
'''
#wrong answer in down 
'''
#frequency of each digit in a given integer

def frequency(f):
    c=0
    for i in range(1,f+1):
        for j in range(i+1,f):
            if i==j:
                c=c+1

while True:
    a=int(input("enter frist number: "))
    frequency(a)
'''
'''
l=[2,2,3,3,456,7,7,8,8]
for i in range(len(l)):
    c=0
    for j in range(len(l)):
        if l[i]==l[j]:
            c=c+1
    if c==1:
        print(l[i]," ",c)
'''
'''
l=[1,1,2,2,3,3,4,4,5]
count=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            #l[i],l[j]=l[j],l[i]
            count=count+1
            print(count)
'''
'''
l=[1,1,2,2,3,3,4,4,5]
unique=[]
for item in l:
    if item not in unique:
        unique.append(item)
print(unique)
'''
'''
l=[1,1,2,2,3,3,4,4,5]
unique=0
l1=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            l1.append (l[i])
    if i in l1:
        l.remove(i)
print(l)
'''
'''
#duplicate

l=[2,2,3,3,45,7,7]
for i in range(len(l)):
    count=0
    for j in range(i+1,len(j)):
        if l(i)==l(j):
            count=count+1
            if count==1:
                print(l[i]," ",c)
        
'''

l=[5,6,1,7,2,2,1,3,5,4]
unique=[]
count=0
nonduplicate=[]
mode_count=0
mode_num=""

for i in range(len(l)):
    for j in range(i+1,len(l)):
        



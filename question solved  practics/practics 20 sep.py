#Create a list of 10 numbers and print all elements
'''
a=[1,2,3,4,5,6,7,8,9,10]
print(a)
'''
#Find the length of a list without using len()
'''
a=[1,2,3,4,5,6,7,8]
count=0
for i in a:
    count=count+1
print(count)
'''
#Find the largest element in a list without using max()
'''
a=[1,2,3,4,5,6,7,8]
#print(max(a))
l=8
for i in a:
    i>l
print(i)
'''
#smallest element in a list without using min()
'''
a=[1,2,3,4,5,6]
#print(min(a))
l=a[0]
for i in a:
    if i<l:
        l=i
print(l)
'''
#Calculate the sum of all elements without using sum()
'''
a=[1,2,3,4,5,6,7,8]
#print(sum(a))
s=0
for i in a:
    s=s+i
print(s)
'''
#Count the number of elements in a list.
'''
a=[1,2,3,4,5,6,7,8,7,6,5,4,3]
count=0
for i in a:
    count=count+1
print(count)
'''
#print all even number in list
'''
a=[1,2,3,4,5,6,7,8,9,10]
for i in a :
    if i%2==0:
        print(i,"even")
'''
#Print all odd numbers from a list.
'''
a=[1,2,3,4,5,6,77,9,10]
for i in a:
    if i%2!=0:
        print(i,"odd")
'''
#Find the average of elements in a list.
'''
a=[1,2,3,4,5,6,7,8,9]
s=0
count=0
for i in a:
    s=s+i
    count=count+1
    r=s/count
print(r)
'''
#Intermediate List Programs
#Count how many times a given number occurs in a list
'''
a=[1,1,2,2,3,3,3,4,4,4,4,5]
count=0
for i in a:
    if i==2:
        count=count+1
print(count)
'''
#Reverse in list without using reverse (dekh liya)
'''
l=[1,2,3,4,5,6,7,8,9,0]
reverse=l[9::-1]
print(reverse)
'''
#Sort a list without using sort()
'''
l=[5,6,4,3,5,8,4,5,7,8,9]
for i in range(0,11):
    for j in range(i+1,11):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print(l)
'''
#Find the second-largest number in a list
#a=[1,2,3,4,5,6,7,,8,9]
'''
a=[234958679]
max=0
second_max=0
while a[0]!=0:
    r=a[0]%10
    if r>max:
        second_max=max
        max=r
    elif second_max<r and max!=r:
        second_max=r
    a[0]=a[0]//10
print(max)
print(second_max)
'''
#Find the second-smallest number in a list
'''
a=[2,3,4,5,6,7,8,]
sort.a
min=0
second_min=0
while a[0]!=0:
    r=a[0]%10
    if r<min:
        second_min=min
        min=r
    elif second_min>r and min!=r:
        second_min=r
        a[0]=a[0]//10
print(min)
print(second_min)
'''
#
'''
a=[23,49,58,67,9]
max=0
second_max=0
i=0
while i<len(a):
    if a[i]>max:
        second_max=max
        max=a[i]
    elif second_max<a[i] and max!=a[i]:
        second_max=a[i]
    i+=1
print(max)
print(second_max)

'''
#Separate positive and negative numbers into two lists
'''
a=[-1,-2,-3,1,2,3]
b=[]
c=[]
for i in a:
    if i>0:
        b.append(i)
    else:
        c.append(i)
print(b,c)
'''
#Create a list containing squares of numbers from 1 to 20
'''
a=[]
for i in range(1,21):
    a.append(i*i)
print(a)
'''
#Replace all negative numbers with 0
'''
a=[1,-1,2,-2,3,-3]
for n in range(len(a)):           
    if a[n]<0:
        a[n]=0
print(a)
'''

Find common elements between two lists#
'''
a=[1,2,3,4,5,6,6,7,8]
b=[9,7,8,6,5,4,6]
c=[]
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            c.append(a[i])
            break
print(c)
'''
#Merge two lists into a single list
'''
a=[1,2,3,4,5,6,7,8,9]
b=[2,3,2,3,4,5,6,7,5,6]
print(a+b)
'''

##Find element present in list but not i the second
'''
a=[1,2,3,4,5,6,6,7,8]
b=[9,7,8,6,5,4,6]
c=[]
for i in range(len(a)):
    found=0
    for j in range(len(b)):
        if a[i]==b[j]:
            found=1
            
    if not found:
        c.append(a[i])
print(c)
'''
#Find all duplicate elements in a list.
'''
a=[5,6,1,7,2,2,1,3,5,4,5]
duplicate=[]
for i in range(len(a)):
    found=0
    for j in range(i+1,(len(a))):
        if a[i]==a[j]:
            found=1
            duplicate.append(a[i])
            break
print(duplicate)
            
'''                   
#Find the frequency of every element in a list
'''
a=[5,6,1,7,2,2,1,3,5,4,5]
duplicate=[]

for i in range(len(a)):
    count=1
    for j in range(i+1,(len(a))):
        if a[i]==a[j]:
            count=count+1
    if count>1:
        
        print(a[i],"->",count)
'''
#Remove all occurrences of a particular element
#1.methard
'''
l=[5,6,1,7,2,2,1,3,5,4,5,2,5,6]
unique=[]
for i in range(len(l)):
    if l[i] not in unique:
        unique.append(l[i])

print(unique)
'''
#2nd.methard
'''
l=[5,6,1,7,2,2,1,3,5,4,5,2,5,6]
for i in range(len(l)):
    for j in range(i+1,(len(l))):
        if l[i]==l[j]:
            del l[j]
            break
'''
#target value
'''
l=[5,6,5,4,5,2,1,3]
i=0
d=15
found=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==d:
            found=1
            print(l[i],"+",l[j],"=>",d)

if(not found):
    print("ni mila kuch bhi")

'''


#Recursion : function calling itself is called recursion


#factorial : 5! 1x2x3x4x5= 120
'''
n=5
m=1
for i in range(1,n+1):
   m=m*i
     1*1
     1*2
     2*3
     6*4
     24*5=120
print(m)
'''
'''
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
            
#               5*fact(4)
#               5*4*fact(3)
#               5*4*3*fact(2)
#               5*4*3*2*fact(1)

print(fact(5))


'''
'''
l[0],l[1]

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







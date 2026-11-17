#find frequency of each digit in a given intege
'''
def frequency (d):
    unique=[]
    while d!=0:
        r=d%10
        t=d//10
        c=1
        while t!=0:
            if r==t%10:
                c=c+1
            t=t//10
        if r not in unique:
            unique.append(r)
            print(r," ",c)
        d=d//10
a=int(input("enter number"))
frequency(a)
'''
'''
l=[2,2,83,3,4,4]
unique=[]
for i in range(len(l)):
 if l[i] not in unique:
            unique.append (l[i])
print(unique)
'''

l=[2,2,3,3,4,4]
count=0
for i in range(len(l)):
    for j in range (i+1,len(l)):
        if l[i]==l[j]:
            count=count+1
print(count)
'''
'''
l=[2,2,3,83,4,4]
duplicate=[]
non_duplicate=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
         duplicate.append(l[i])
print(duplicate)

'''
l=[2,2,3,83,4,4,2]

non_duplicate=[]
unique=[]
for i in range(len(l)):
    if l[i] not in unique:
        unique.append(l[i])
        found=0
        count=0
        for j in range(i+1,len(l)):
            if found==0:
                if l[i]==l[j]:
                    found=1
                    count+=1
        print(i,j,count)
        if found==0:           
            non_duplicate.append(l[i])
print(non_duplicate)
'''
'''
def unique(d):
    while (d!=0):
        d=d%10
        r=d//10
        while
'''       

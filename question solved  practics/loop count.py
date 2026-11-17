'''
l=[1,2,3,1,2,3,4,5,6,5,6,]
count=0
for i in range(0,11):
    for j in range(i+1,11):
        if l[i]==l[j]:
            count=count+1
print(count)
'''
'''
l=[1,2,3,4,3,2,1,6]
unique=0
l1=[]
for i in range(0,8):
    for j in range(i+1,8):
       if l[i]==l[j]:
           l1.append(l[i])
            
for i in l1:
    l.remove(i)
print(l)

'''
'''
l=[3,3,2,2,6,6,7,8,9]
unique_l=[]
for item in l:
    if item not in unique_l:
        unique_l.append(item)
print(unique_l)
'''
'''
#wrong
l=[6,7,3,4,7,8,9]
for i in range(0,9):
    for j in range(i+1,9):
        if l[i]<l[j]:
            l[i],l[j]=l[j],l[i]
print(l)
'''
l=[3,1,3,4,5,3,4,5,6,7]
count=0
unique=[]
for i in range(0,8):
    if l[i] not in unique:
        unique.append(l[i])
        for j in range(i+1,8):
            if l[i]==l[j]:
                count=count+1
        print(l[i],"->",count+1)
    count=0
            

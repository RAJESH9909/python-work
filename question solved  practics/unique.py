'''
list=[2,2,3,3,456,7,7,8,8]
unique=[]
for i in list:
    if i not in unique:
        unique.append(i)
print(unique)
'''

'''
list=[2,2,3,3,456,7,7,8,8]
count=0
for i in range(0,9):
    for j in range(i+1,9):
        if list[i]!=list[j]:
            count=count1
print(count)
'''
'''
list=[2,2,3,3,456,7,7,8,8]
for i in range(0,9):
    for  j in range(i+1,9):
        if list[i]>list[j]:
            list[i]list[j]=list[j]list[i]
print(list)
'''
'''
l=[2,2,3,3,456,7,7,8,8]
dublicate=[]
for i in l:
    #if l.count(i)==1:
        print(i,"=",l.count(i))
'''
'''
l=[2,2,3,3,456,7,7,8,8]
for i  in range(0,9):
    for j in range(i+1,9):
        if l[i]==l[j]:
            l[i],l[j]=l[j],l[i]
print(l)
'''
l=[2,2,3,3,456,7,7,8,8]
count=0
unique=[]
duplicate=[]
nonduplicate=[]

for i in range(0,len(l)):
    if l[i] not in unique:
        unique.append(l[i])
        found=0
        for j in range(i+1,9):
            if(found==0):
                if l[i]==l[j]:
                    found=1
                    duplicate.append(l[i])
                    count=count+1
                    
print("unique:",unique,"\nduplicate:",duplicate,"\ncount:",count)

l=[2,2,3,3,456,7,7,8,8]
nonduplicate=[]
for i in range(0,9):
    nonduplicate.append(l[i])
    for j in range(i+1,9):
        if l[i]!=l[j]:
            nonduplicate=nonduplicate+1
print(nonduplicated)
        

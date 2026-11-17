
l=[2,2,3,3,456,7,7,8,8]
for i in range(len(l)):
    c=0
    for j in range(len(l)):
        if l[i]==l[j]:
            c=c+1
    if c==1:
        print(l[i]," ",c)

'''
#c=count
l=[5,5,6,6,78,9,0]
for i in range(len(l)):
    c=0
    for j in range(len(l)):
       if l[i]==l[j]:
           c=c+1
    print(l[i]," ",c)

'''
'''
l=[5,5,6,6,78,9,0]
duplicate=[]
unique=[]
count=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            duplicate.append(l[i])
        elif l[i]==l[j]:
            unique.append(l[i])
        elif l[i]==l[j]:
            count=count+1
print(duplicate," " ,count," ",unique)
'''   


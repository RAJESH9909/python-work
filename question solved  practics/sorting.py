'''
l=[3,5,7,8,1,3]
for i in range(0,6):
    for j in range(i+1,6):
        if l[i]<l[j]:
            l[i],l[j]=l[j],l[i]
print(l)

'''
'''
l=[55,78,98,34,45]
for i in range(0,5):
    for j in range(i+1,5):
        if l[i]<l[j]:
            l[i],l[j]=l[j],l[i]
print(l)

'''
'''
#Write a  program to swap first and last digits of a number.

a=[23,32]
a[0],a[-1]=a[-1],a[0]
print(a)
'''
'''
l=[6,5,4,8,9,2,0]
for i in range(0,7):
    for j in range(i+1,7):
        ik
        f l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print(l)
'''
'''
l=[6,5,4,8,9,2,0]
for i in range(0,7):
    for j in range(i+1,7):
        if l[i]<l[j]:
            l[i],l[j]=l[j],l[i]
print(l)
'''
'''
l=[3,4,11,6,8,9,64]
for i in range(0,7):
    for j in range(i+1,7):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
           
print(l[-2])
'''
'''
l=[3,4,11,6,8,9,63]
for i in range (0,7):
    for j in range(i+1,7):
        if l[i]<l[j]:
            l[i],l[j]=l[j],l[i]
print(l)
'''
'''
l=[3,3,2,2,6,6,7,8,9]
count=0
for i in range(0,9):
    for j in range(i+1,9):
        if l[i]==l[j]:
            count=count+1
            
print(count)
'''
'''
l=[3,3,2,2,6,6,7,8,9]
for i in range(0,9):
    for j in range(i+1,9):
        if l[i]==l[j]:
            l.remove()
print(l)
            
'''
'''
l = [3, 3, 2, 2, 6, 6, 7, 8, 9]
unique_l = []

for item in l:
  if item not in unique_l:
    unique_l.append(item)

print(unique_l)
'''
'''
l=[3,3,2,2,1,1,6,5,6,5,7,9,8,7,9]
unique=[]
for item in l:
    if item not in  unique:
        unique.append(item)
print(unique)
''
l

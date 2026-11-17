#loop
'''
n=2
for i in range(1,11):
    print(n*i)
'''
'''
for i in range(1,11):
    if i%2==0:
        print("even ",i)
    else:
        print("odd ",i)

n=int(input("enter: "))
s=0
for i in range(1,n+1):
    s=s+i
print(s)
    
'''
'''
n=int(input("enter: "))
s=0
for i in range(1,n+1):
    if i%2==0:
        s=s+i
print(s)

n=int(input("enter: "))
s=0
for i in range(1,n+1):
    if i%2!=0:
        s=s+i
print(s)
'''

l=[2,3,4,5,6,7,8]

s=0
for i in l:
    if i%2==0:
        s=s+i
print(s)

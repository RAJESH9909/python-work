'''
for n in range(1,100):
   

    i=2
    s=0
    while i<n:
        
        if n%i==0:
            s=1
            break
        i=i+1
    if s==0:
        print(n," prime")
    else:
        print(n," not")
'''
'''
count=5
while(count>0):
    print(count)
    count=count+1
'''
sum=0
for n in range(1,100):


    i=2
    s=0
    while i<n:
        
        if n%i==0:
            s=1
            break
        i=i+1
    if s==0:
        sum+=n
        print(n,sum," prime")
    else:
        print(n," not")

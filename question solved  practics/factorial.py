
def digit(d):
    s=0
    org=d
    while d!=0:
        r=d%10
        m=1
        
        for i in range(1,r+1):
            m=m*i
        
        s=s+m
        d=d//10
    print(s)
    if org==s:
        print("strong")
    
a=int(input("enter number"))
digit(a)
'''
def digit(d):
    while d!=0:
        r=d%10
        m=1
        for i in range(1,r+1):
            m=m*i
        print(m)
        d=d//10
    
a=int(input("enter number"))
digit(a)
'''



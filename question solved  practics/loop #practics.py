'''start=1
end=10
en=[]
on=[]
#                1    11 
for i in range(start,end+1):
    #print(i)
    if i%2==0:
        en.append(i)
        #print(i," is even")
    else:
        on.append(i)
        #print(i,"is odd")
print("odd no",on)
print("even no",en)
'''
'''
n=2
for i in range(1,11+1):
     print(n*i)
     if i%2==0:
         print("even")
     
'''
'''
sum=0
start=1
end=10
for i in range(start,end+1):#1,2,3...
    sum=sum+i#1,3,6...
    print("s:",sum)
'''
'''
s=0
n=10
for i  in range(1,n+1):
    s=s+i
    print(s)
'''
'''
n=2
for i in range(1,11):
    print(n*i)
'''
'''
n=int(input("enter number"))
for i in range(1,10+1):
      print(n*i)
'''
'''
u=20
n=int(input("enter number"))
for i in range(1,u+1):
    print(n*i)
    if i%2==0:
        print("even")
'''
#Write a  program to print all natural numbers
#from 1 to n. - using while loop
'''
n=10
for i in range(1,n+1):
    print(i)
'''
#Write a  program to print all natural numbers
#in reverse form (n to 1)us-ing while loop
'''
n=10
for i in range(n,1,-1):
    print(i)
'''
#Write a  program to print all alphabets from
#a to z. - using while loop
'''
al==a or al==z
for i  in range(al):
    print(al)
'''
'''
for i in range(97,123):
    print(chr(i))
'''
'''
for i in range(65,91):
    print(chr(i))
'''
'''
for i in range(1,200):
    print(chr(i))
'''
#Write a  program to print all even numbers
#between 1 to 100. - using while loop

n=100
en=[]
on=[]
for i in range(1,n+1):
    print(i)
    en.append(i)
    if i%2==0:
        print(i, "is even")
    else:
        on.append(i)
        print(i,"is odd")

#Write a  program to find sum of all natural
#numbers betweenz1 to n.
'''
n=10
s=0
for i in range(n,0,-1):
    s=s+i
    print(s)
'''
#Write a  program to find sum of all even number
#between 1 to n.
'''
n=10
s=0
for i in range(1,n+1):
   if i%2==0:
    s=s+i
    print(s)
'''
# Write a  program to find sum of all odd
#numbers between 1 to n  

'''
n=10
s=0
for i in range(1,n+1):
    if i%2!=0:
        s=s+i
        print(s)
'''
#program to print multiplication table of any number
n=10
a=int(input("enter number"))
for i in range(1,11):
    print(a*i)
    

"""
with open("C:\\Users\\Lenovo\\Desktop\\data.txt","w") as f:
    f.write("datadata")
    print("success")
"""
"""
a=int(input("enter: "))
b=int(input("enter" ))
with open("C:\\Users\\Lenovo\\Desktop\\data.txt","a") as f:
    f.write("a= "+str(a)+" b= "+str(b)+"\n")
    print("success")
print(a+b)
"""
"""
with open("C:\\Users\\Lenovo\\Desktop\\N Document.txt","w") as f:
    f.write ("N Document")
    print("success")
"""
"""
a=int(input("enter number"))
b=int(input("enter number"))

with open("C:\\Users\\Lenovo\\Desktop\\N Document.txt","a") as f:
    f.write("a= "+str(a)+" b= "+str(b)+"\n")
    print(a+b)
"""
"""
#Write a  program to find maximum between two numbers

a=int(input("enter number"))
b=int(input("enter number"))

with open(r"C:\\Users\\Lenovo\\Desktop\\N Document.txt","a") as f:
    if a>b:
        f.write("a= "+ str(a)+">" "b= "+str(b)+"\n" "a is greater")
        print("a is greater")
    
    elif b>a:
        f.write("b= " +str(b)+ ">" "a=" +str(a)+"\n" "b is greater")
        print( "b is greater")

"""
"""
#Write a  program to check whether a number is negative, positive or zero

a=int(input("enter number"))
with open("C:\\Users\\Lenovo\\Desktop\\N Document.txt","a") as f:
    

    if a>0:
        f.write("a= " + str(a) + ">0\n positive\n")
        print("positive")
          
    elif a<0:
        f.write("a= " + str(a) + "<0\n negative\n")
        print("negative")
    else:
        print("zero")
        f.write("a= " + str(a) + "0\n negative\n")
"""

#Write a  program to check whether a number is divisible by 5 and 11 or not.
"""
    
a=int(input("enter number"))
with open("C:\\Users\\Lenovo\\Desktop\\N Document.txt","a") as f:
        
        if a%5==0 and a%11==0:
            f.write("a= " +str(a)+ "%5==0 and" +str(a)+"%11==0\n divisible \n")
            print("divisible")
        else:
            print("not")
"""
"""
f=open(r"C:\\Users\\Lenovo\\Desktop\\N Document.txt","w")
f.write("Write a  program to check whether a number is even or odd.\n")
a=int(input("enter number"))

if a%2==0:
        f.write("a= " +str(a)+"%2==0 \n even\n")
        print("even")
elif a%2!=0:
        f.write("a= " +str(a)+ "%2!=0 \n odd \n")
        print("odd")

f.close()
"""

#Write a  program to input any alphabet and check whether it is vowel or con-sonant.
ch=input("enter charactor")
with open("C:\\Users\\Lenovo\\Desktop\\N Document.txt","a"):
    
    if ch.isalpha(ch=="a" or ch=="e"or ch=="i" or ch=="o" or ch=="u"):
        f.write("a= " +str(ch)+"==a or " +str(ch)+ "==e or " +str(ch)+ "==i or" +str(ch)+ "==o or "+str(ch)+ "==u \n vowel \n ")
        print("vowel")
    else:
        print("consonant")

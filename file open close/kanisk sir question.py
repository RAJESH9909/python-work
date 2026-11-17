#1. Write a Python program to create a new text file named data.txt.
"""
with open("C:\\Users\\Lenovo\\Desktop\\kanisk sir question.txt","a") as f:
    f.write("datadata" "\n")
"""
#Write a program to write "Hello Python" into a file
"""
with open("C:\\Users\\Lenovo\\Desktop\\kanisk sir question.txt","a") as f:
    f.write("Hallo python" "\n")
"""
#Write a program to read and display the contents of a text file
"""
with open("C:\\Users\\Lenovo\\Desktop\\kanisk sir question.txt","r") as f:
     print(f.read())
"""

#4. Write a program to append new text to an existing file.
"""
with open("C:\\Users\\Lenovo\\Desktop\\kanisk sir question.txt","a") as f:
     f.write("new text" "\n")
"""
#5. Write a program to count the total number of characters in a file.
"""
count=0
with open("C:\\Users\\Lenovo\\Desktop\\kanisk sir question.txt","r") as f:
    l=f.read()
    for i in range(1,len(l)):           
        count=count+1
        print(count)
"""
#6. Write a program to count the total number of words in a file.
"""
with open("C:\\Users\\Lenovo\\Desktop\\kanisk sir question.txt","r") as f:
    l=f.read()
    l=l.split()
    count=len(l)
    print(count)
"""
#7. Write a program to count the total number of lines in a file.
"""
with open("C:\\Users\\Lenovo\\Desktop\\kanisk sir question.txt","r") as f:
    l=f.read()
    #l=l.splitlines()
    l=l.split("\n")
    count=len(l)
    print(count)
"""
#8. Write a program to read a file line by line.
"""
with open("C:\\Users\\Lenovo\\Desktop\\kanisk sir question.txt","r") as f:
   # print(f.readline())
   for i in f:
       print(i)
    
"""
# Write a program to display the first five lines of a file.
"""
with open("C:\\Users\\Lenovo\\Desktop\\kanisk sir question.txt","r") as f:
    
    for i in range(5):
        print(f.readline())
"""
"""
with open("C:\\Users\\Lenovo\\Desktop\\kanisk sir question.txt", "r") as f:
    count = 0
    for line in f:
        print(line)
        count += 1
        if count == 5: break

"""

# Write a program to display the last three lines of a file.
"""
with open("C:\\Users\\Lenovo\\Desktop\\kanisk sir question.txt", "r") as f:
    l=f.readlines()
    print(l[-3:])
"""
#11. Write a program to check whether a file exists.(chor do )as par gpt
"""
import os

print(os.path.exists("data.txt"))
print(os.path.exists("abc.txt"))
print(os.path.exists("test.txt"))
"""
# 12. Write a program to print the name and size of a file.
"""
import os
print(os.path.basename("C:\\Users\\Lenovo\\Desktop\\kanisk sir question.txt",))
print(os.path.getsize("C:\\Users\\Lenovo\\Desktop\\kanisk sir question.txt",))
"""
#Write a program to copy the contents of one text file into another
"""
with open(r"C:\\Users\\Lenovo\\Desktop\\kanisk sir question.txt","r")as f:
    l=f.read()
    with open(r"C:\\Users\\Lenovo\\Desktop\\N Document.txt","w")as f2:
        f2.write(l)
"""
#14. Write a program to clear all contents from an existing file.
"""
with open(r"C:\\Users\\Lenovo\\Desktop\\kanisk sir question.txt","w")as f:
    pass
"""

#write a program to read using the open () statement
"""
with open("C:\\Users\\Lenovo\\Desktop\\kanisk sir question.txt","r")as f:
    l=f.read()
    print(l)
"""
#16. Write a program to count the number of uppercase letters in a file.
"""
with open(r"C:\\Users\\Lenovo\\Desktop\\N Document.txt","r")as f:
    l=f.read()
    count=0
    for i in l:
        if i.isupper():
            count=count+1
            print(count)
"""
#17. Write a program to count the number of lowercase letters in a file.
"""
with open(r"C:\\Users\\Lenovo\\Desktop\\N Document.txt","r")as f:
    l=f.read()
    count=0
    for i in l:
        if i.islower():
            count=count+1
    print(count)
"""


# Write a program to count the number of digits in a file.
"""
with open(r"C:\\Users\\Lenovo\\Desktop\\N Document.txt","r")as f:
    l=f.read()
    count=0
    for i in l:
        if i.isdigit():
            count=count+1
    print(count)

"""
#19. Write a program to count vowels and consonants in a file.
"""
with open(r"C:\\Users\\Lenovo\\Desktop\\N Document.txt","r")as f:
    l=f.read()
    vowelcount=0
    consonantcount=0
    vowel="aeiou"
    for i in l:
        if i in vowel:
            vowelcount=vowelcount+1
        elif i.isalpha and i.lower()not in vowel:
                consonantcount=consonantcount+1
    print(consonantcount)
    print(vowelcount)
"""
#20. Write a program to find the longest word in a file.
"""

with open(r"C:\\Users\\Lenovo\\Desktop\\N Document.txt","r") as f:
    l=f.read()
    l=l.split()
    longest=l[0]
    for i in l:
        if len(i) > len(longest):
            longest = i
    print(longest)
"""
#Write a program to find the shortest word in a file
"""
with open (r"C:\\Users\\Lenovo\\Desktop\\N Document.txt","r") as f:
    l=f.read()
    l=l.split()
    shortest=l[0]
    for i in l:
        if len(i)< len(shortest):
            shortest=i
    print(shortest)
"""
#22. Write a program to search for a specific word in a file.
"""
with open(r"C:\\Users\\Lenovo\\Desktop\\N Document.txt","r") as f:
    l=f.read()
    l=l.split()
    wrd="datadata"
    if wrd in l:
        print("true")
    else:
        print("false")

"""
#23. Write a program to count how many times a particular word occurs in a file.
"""
count=0
with open(r"C:\\Users\\Lenovo\\Desktop\\N Document.txt","r") as f:
    l=f.read()
    l=l.split()
    wrd="datadata"
    if wrd in l:
        count=count+1
        print(count)
    else:
        print("not found")
"""
"""
count = 0

with open(r"C:\\Users\\Lenovo\\Desktop\\N Document.txt", "r") as f:
    l = f.read()
    l = l.split()
    wrd = "datadata"

    for i in l:
        if i == wrd:
            count = count + 1

    if count > 0:
        print("Word occurs", count, "times")
    else:
        print("Word not found")
"""
#24. Write a program to replace a specific word with another word throughout a file.
"""
with open(r"C:\\Users\\Lenovo\\Desktop\\N Document.txt", "r") as f:
    l=f.read()
    #l=l.split()
    wrd="datadata"
    wed="databeta"
    if wrd in l:
        l=l.replace (wrd,wed)
        print(l)
    else:
        print("not found")
    
with open(r"C:\\Users\\Lenovo\\Desktop\\N Document.txt", "w") as f:
    f.write(l)
"""

# 24. Replace a specific word with another word throughout a file
"""
path = r"C:\\Users\\Lenovo\\Desktop\\N Document.txt"

with open(path, "r") as f:
    l = f.read()

wrd = "datadata"
wed = "databeta"

if wrd in l:
    l = l.replace(wrd, wed)

    with open(path, "w") as f:
        f.write(l)

    print("Word replaced successfully")
else:
    print("Word not found")
"""
#25. Write a program to remove blank lines from a file.
"""
path=r"C:\\Users\\Lenovo\\Desktop\\N Document.txt"

with open(path, "r") as f:
     l=f.readlines()
     l2=[]
     for i in l:
         if i.strip():
             l2.append(i)

with open(path, "w") as f:
    #f.write(l)
    f.writelines(l2)

"""

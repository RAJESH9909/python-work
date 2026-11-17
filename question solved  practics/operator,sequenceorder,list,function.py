Python 3.13.15 (tags/v3.13.15:4061bc4, Aug  5 2026, 13:05:39) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="hello",12,32,42,67000.00,"rajesh"
a.[0:3]
SyntaxError: invalid syntax
a.(0:3)
SyntaxError: invalid syntax
a[0]
'hello'
a[0:3]
('hello', 12, 32)
a[-5]
12
a[-6]
'hello'
a.apeend()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a.apeend()
AttributeError: 'tuple' object has no attribute 'apeend'
a.append(90)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a.append(90)
AttributeError: 'tuple' object has no attribute 'append'
a.append()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a.append()
AttributeError: 'tuple' object has no attribute 'append'
a.append(90)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a.append(90)
AttributeError: 'tuple' object has no attribute 'append'
a.append(90)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a.append(90)
AttributeError: 'tuple' object has no attribute 'append'
a=[1,2,3,4,5,"rajesh"]
a.append()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.append()
TypeError: list.append() takes exactly one argument (0 given)
a.append(90)
a
[1, 2, 3, 4, 5, 'rajesh', 90]
>>> a.index(4)
3
>>> a.insert(4,3)
>>> 
>>> a
[1, 2, 3, 4, 3, 5, 'rajesh', 90]
>>> a.pop()
90
>>> a
[1, 2, 3, 4, 3, 5, 'rajesh']
>>> a.remove("rajesh")
>>> a
[1, 2, 3, 4, 3, 5]
>>> dh={"name":"aman","rollno":21,"class":10}
>>> print("name")
name
>>> print(dh.name)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(dh.name)
AttributeError: 'dict' object has no attribute 'name'
>>> print(dh.["name"])
SyntaxError: invalid syntax
>>> s={1,1,2,2,3,3,4,4,5,5,}
>>> s
{1, 2, 3, 4, 5}
 dh={"name":"aman","rollno":21,"class":10}
 print[]





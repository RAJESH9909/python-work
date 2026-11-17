#1. Create a Student class with attributes name, roll_number, and marks. Create three objects and display their details.
'''
class Student:
    def __init__(self,name,roll_number,marks):
        self.name=name
        self.roll_number=roll_number
        self.marks=marks
    def __str__(self):
        return f"name:{self.name} \n roll_number:{self.roll_number}\n marks:{self.marks}"
"""
class Student:(Student):
    def __init__(self,name,roll_number,marks):
        super().__init__(name,roll_number,marks)
    def __str__(self):
        return f"{super().__str__()}\n"


class Student:(Student):
    def __init__(self,name,roll_number,marks):
        super().__init__(name,roll_number,marks)
    def __str__(self):
        return f"{super().__str__()}\n"

"""
s1=Student("rakesh","9","121")
print("s1:\n", s1)
s2=Student("rajesh","10","122")
print("s2: \n", s2)
s3=Student("ravi","11","123")
print("s3: \n ", s3)

'''
# 2. Create an Employee class with attributes name and salary. Add a method to calculate and display the annual salary.
"""
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def __str__(self):
        return f"name: {self.name} salary :{self.salary}"
    
    def annual_salary(self):
        print("annual_salary:",self.salary*12)

e1=Employee("rajesh",12000)
print("e1 \n",e1)
e1.annual_salary()
"""
#3. Create a Rectangle class with length and width. Implement methods to calculate area and perimeter.
"""
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def __str__(self):
        return f"lenth :{self.length}  \n width {self.width}"

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

r1=Rectangle(12,12)
print("r1: \n",r1)

print(r1.area())
print(r1.perimeter())
"""
"""
# 4. Create a Circle class with a radius attribute. Implement methods to calculate area and circumference.

import math
class Circle:
    def __init__(self,radius):
        self.radius=radius

    def __str__(self):
        return f"radius:{self.radius}"

    def area(self):
        return math.pi*self.radius**2

    def circumference(self):
        return 2 * math.pi * self.radius

c1=Circle(12)
print("c1: \n", c1.area())
print(c1.circumference())
"""
# 5. Create a BankAccount class with methods to deposit money, withdraw money, and display the balance.
"""
class BankAccount:
    def __init__(self,deposit_money,withdraw_money,balance):
        self.deposit_money=deposit_money
        self.withdraw_money=withdraw_money
        self.balance=balance

    def __str__(self):
        return f"deposit_money:{self.deposit_money},\n withdraw_money{self.withdraw_money},\n balance :{self.balance}"

    def  total_balance(self):
        return self.deposit_money- self.withdraw_money

b1= BankAccount(12000,3000,9000)
print("b1 \n",b1)
print(b1.total_balance())
"""
# 6. Create a Book class with a constructor that initializes the title, author, and price. Display the book details.
"""
class book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    def __str__(self):
        return f"title{self.title} \n ,author {self.author} \n price{self.price}"

b1=book("tital","martin luther king","1700")
print("b1 \n",b1)
"""
# 7. Create a Car class with a constructor that accepts the brand, model, and manufacturing year. Add a method to display its age.
"""
class car:
    def __init__(self,brand,modal,manufacturing_year,current_year):
        self.brand=brand
        self.modal=modal
        self.manufacturing_year =manufacturing_year
        self.current_year=current_year
    def __str__(self):
        return f"brand {self.brand} \n  modal {self.modal} \n manufacturing_year{self.manufacturing_year}"

    def age(self):
        return self.current_year - self.manufacturing_year

c1=car("suzuki","fronex",2021,2026)
print("c1 \n ",c1)
print(c1.age())
"""
#8. Create a Product class that initializes its name, price, and quantity. Implement a method to calculate the total inventory value.
"""
class product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def __str__(self):
        return f" name: {self.name} \n price {self.price} \n quantity {self.quantity}"

    def value_inventry(self):
        return self.price*self.quantity


p1=product("book",1200,55)
print("p1 \n",p1)
print(p1.value_inventry())
"""
# 9. Create a Laptop class with a constructor that sets default values for RAM and storage. Allow users to override these values.
"""
class Laptop:
    def __init__(self, ram=8, storage=256):
        self.ram=ram
        self.storage=storage

    def __str__(self):
        return f" ram:  {self.ram} \n storage {self.storage}"
    # def __str__(self):
    #     return f"ram=8, storage=256"
l1=Laptop()
l2=Laptop(12,500)

print("l1 \n",l1)
print(l2)
"""
# 10. Create a Temperature class that initializes temperature in Celsius and provides methods to convert it to Fahrenheit and Kelvin.
"""
# class  temperature:
#     def __init__(self,celsius):
#         self.celsius=celsius
#         #self.Fahrenheit=Fahrenheit
#         #self.Kelvin=Kelvin
#     # def __str__(self):
#     #     return f"celsius {self.celsius} \n"

#     def f_to_c(self,f):
#         return (f-32)*(5/9)
# a=temperature(5)

# f=int(input("enter temperture in f"))
# print(a.f_to_c(f))
"""
"""
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def c_to_f(self):
        return (self.celsius * 9/5) + 32

    def c_to_k(self):
        return self.celsius + 273.15


a = float(input("Enter temperature in Celsius: "))
t1 = Temperature(a)

print("Fahrenheit:", t1.c_to_f())
print("Kelvin:", t1.c_to_k())
"""
# 11. Create a Person class with name and age. Derive a Student class that adds a student ID and course.
"""
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"name {self.name} \n age {self.age} "
    
class student(Person):
    def __init__(self,name,age,student_id,course):
        super().__init__(name,age)
        self.student_id=student_id
        self.course=course
    
    def __str__(self):
        return f" {super().__str__()} \n student_id : {self.student_id} \n course : {self.course}"

p1=Person("rakesh",21)
print("p1 : \n", p1)
p2=student("ravi",21,"rk_9027","data_science")
print("p2 : \n", p2)
"""
# 12. Create a base class Vehicle with a method start(). Derive Car and Bike classes that provide their own implementations.
"""
class Vehicle:
    def start (self):
        print("vehicle is starting  ")
       
class car (Vehicle) :
     def start (self):
        print("car is starting")

class bike(Vehicle):   
        def start(self):
            print("bike is starting ")

v1=Vehicle()
c1=car()
b1=bike()

v1.start()
c1.start()
b1.start()
"""
# 13. Create an Employee base class and derive Manager and Developer classes. Calculate salaries differently for each role.
"""
class Employee:
    def __init__(self,name,basic_salary):
        self.name=name
        self.basic_salary=basic_salary
        
    def  calculate_salary(self):
        pass

class manager(Employee):
    def calculate_salary(self):
        bonus=self.basic_salary*20/100
        total=self.basic_salary+bonus

        return f" name {self.name} \n basic_salary {self.basic_salary} total_salary: {total}"
    

class Developer(Employee):
    def calculate_salary(self):
        bonus=self.basic_salary*10/100
        total=self.basic_salary+bonus

        return f"name {self.name} \n basic_salary {self.basic_salary} \n total_salary:{total}"

m1=manager("ravi",30000)
m2=Developer("ravi_2",25000)

print(m1.calculate_salary())
print(m2.calculate_salary())

"""

# 14. Create a Shape base class and derive Rectangle, Circle, and Triangle classes. Implement an area calculation method in each subclass.
""" not compleat
class shape:
    def area(self):
        pass

class Rectangle(shape):
    def __init__(self,lenth,width):
        self.length=lenth
        self.width=width

    def area(self):
        return self.length*self.width
"""




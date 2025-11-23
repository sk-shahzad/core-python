# if 5 < 2:
#      print("Five is greater than two!")
# else:
#      print('Python is awesome')
# variables
# x = 5
# y = "John"
# print(x)
# print(y)

# x = "awesome "
# y = 'and easy'
# print("Python is " + x + y)
#
# x = 5
# y = 10
# print(x + y)
# print(type(x))

# # input string
# print("Enter your name:")
# x = input()
# print("Hello, " + x)



# x= int(input("enter a value "))
# y= int(input("enter a value "))
# print(x + y)
# print(type(x))



# birth_year = input('birth year: ')
# age = 2025 - int(birth_year)
# print("You are ", age, "Years old")

# a = "i am a programmer"
# print(a.replace("programmer","Coder"))
# print(a.find("r"))

#Data Types
#int
# a = 43
# #Float
# weight = 59.32
# #String
# name = 'sk'
# #boolean
# is_boy = True
# #list
# list1=[100,200,300]
# #Dictionary
dict1={'name':'shahzad', 'age':25}

print(dict1['age'], type(dict1))

#String
# a = """I don't "hello", world"""
# b = a.split(',')
# print(a)
# name = 6
# raw = f"hello world {1+2}" 
# print(raw)

# string formating
# name = 'Khalid'
# age = 9
# gender = "male"

# print (name==age)
# c = "my name is %s and I live in %s" % (name, age)
# print(f'My name is {name.upper()} I am {age} ')
# print("My name is {} and I live in {:.2f}.".format(name, age))
# print("I got {0:.2f}% marks in  English.".format(97.55))
# print("my name is {} and I am {:d} ".format(name, age))
# print(f"My name is {name} I am {age}."\
#     f"and I am a {gender}")

#String Methods
#Strip remove leading and trailing characters and whitespaces
# x = "aaaaHello Worldaaa".strip('a')
# print(x)
# p = "   Solve any problem is an art.   ".strip('. ')
# print(p)

#lstrip remove the leading whitespaces
# s = "   Hello world   '".lstrip()
# print(s)

#rstrip remove from right i-e trailing
# c = "Hello world    ".rstrip()
# print(c)

# h = "my name is klaus ".rstrip('my ')
# print(h)

# split -> used to split a sting into a list. string.split(separator, maxsplit)
# print("Hello! I am klaus".split())
# print("Hello!$I$am$klaus".split('$', maxsplit=3))

# rsplit method used to split the string from the right. string.split(separator, maxsplit)
# print("Hello!$I$am$klaus".rsplit('$', maxsplit=2))
# print("Hello! I am klaus".rsplit())

# join used to join the element of iterable
# l1 = ['h','e','l','l','o']
# print(''.join(l1))
# l2 = ['I', 'am', 'klaus']
# print(' '.join(l2))
# l3 = ['name', 'of', 'a', 'variable']
# print('_'.join(l3))
# d = {'name': 'adam', 'country': 'US'}
# print(' and '.join(d))

# Replace s.replace(old,new,count)
s = "i love to eat strawberries."
# print(s.replace('strawberries', 'mangoes'))
# print(s.replace(' ', '_', 2))

# Upper(), lower(), isalpha(), isnumeric() and isalnum is easy
# print(s.capitalize())
# print(s.isupper())
# print(s.islower())

# count(sub, start, end)
# print(s.count('r'))
# print(s.count('love', 0, 13))

# find (sub, start, end), rfind(returns from right occurences)
# print(s.find('eat'))
# print(s.find('eat', 1, 10))

# index and find are same but index only run valueError rather than find run -1

# Typecasting / type conversion has two types. Implicit and explicit. Implicit is the aility of pyhon 
# That convert from lower type to upper eg. x= 10, y = 20.9 if we add them the 10 will convert it to 10.0 (implicit)
# Explicit
# x = 10
# y = 20
# total = x+y
# print("The total is " + str(total))

# x = '110'
# print(int(x, 2))
# x = int(x)
# print(type(x))
# print(float(x))

# x = "pakistan "
# print(x * 3)
# print(x[0])

# a = str(5)
# b = str(6)
# print(a+b)

# print('enter your name')
# a= input()
# print('hello ' + a)

# try:
#     print(x)
# except NameError:
#     print('x is undefined')
# except:
#     print('an Error has occured')
# finally:
#     print('Try except is finished')

'''
course =  hi
    i am janooo
    i love you
    will you ...
print(course) #it gives the code as how we write it but after = and last must be mlc
'''

'''
course = 'python is a programming language'
print(course[0]) #it will show the first letter of line
'''

'''
course = 'python is a programming language'
print(course[-1]) #it will display the last letter from line
'''
'''
course = 'python is a programming language'
print(course[0:3]) #it gives the first three words
print(course.upper()) #convert to upper case
print(course.find('p')) #it shows index address
print(course.replace('programming','high level')) # replacing
print('python' in course)  #returns boolean value
'''

# is_hot=False
# is_cold=False
# if is_hot:
#     print("it's hot day")
# elif is_cold:
#     print("it is cold day")
# else:
#     print("lovely day")
# print("enjoy your day")

# banana = ["banana","apple", "mango"]
# banana.pop("mango")
# print(banana)
# # for x in banana:
# banana[1] = "cherry"
# banana.append("orange")
#   print(banana)

# import mymodule
# mymodule.greeting(" sana")

# import datetime

# x = datetime.datetime.now()
# print(x.year)

# import camelcase

# c = camelcase.CamelCase()

# txt = "lorem ipsum dolor sit amet"

# print(c.hump(txt))

# #This method capitalizes the first letter of each word.
# try:
#   print(t)
# except:
#   print("An exception occurred")

# File handling
# f = open("demo.txt","x")
# f = open("demo.txt", "r")
# print(f.readline())
# print(f.readline())
# for x in f:
#   print(x)

# f = open("demo.txt", "a")
# f.write("\nNow the file has one more line!")
# f = open("demo.txt", "r")
# print(f.read())

# import os
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")

# age = int(input("Enter age: "))
# if(age > 18):
#     if(age > 80):
#       print("cannot drive")
#     else:
#       print("can drive")
# else:
#   print ("cannot drive")

# num = int(input("Enter a number: "))
# if(num % 2 == 0):
#   print("Even")
# else:
#   print("Odd")

# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))
# c = int(input("Enter 3rd number: "))
# if(a > b and a >= c):
#   print("1st Number is largest ", a)
# elif(b >= c):
#   print("2nd is the largest number ", b)
# else:
#   print("3rd is the largest number ", c)

# mov = []

# mov.append(input("Enter item to list: "))
# mov.append(input("Enter item to list: "))
# mov.append(input("Enter item to list: "))
# mov.sort(reverse=True)
# print(mov)

# info = {
#   "name" : "Khalid",
#   "subjects" : ["python","C","Java"],
#   "Topic"   :   ("dict","set"),
#   "CGPA" :  4.0,
#   "BS"    :  "CS"
# }

# # print(info["name"])
# info["name"] = "Shahzad"
# info["Age"] = 25
# info.update({"Address" : "swat"})
# print(info)

#Nested
# student = {
#   "name" : "Khalid",
#   "subjects" : {"phy" : 23,
#                 "chem":  34,
#                 "COmp":  23},
#   "Topic"   :   ("dict","set"),
#   "CGPA" :  4.0,
#   "BS"    :  "CS"
# }
# print(student["subjects"])
# print(student.get("subject"))
# print((student.keys()))
# print(list(student.keys()))
# print((student.values()))


# set
# Collection = {1, 2, 3, 4, "hello", "world", "world"}

# print(Collection)

# col = set()
# col.add(1)
# col.add(2)
# col.add(2)

# col.remove(1)
# print(col)

# Loop
# i = 1
# while i <= 5:
#   print("Hello ", i)
#   i += 1

# break
# i = 1
# while i <= 5:
#   print("Hello ", i)
#   if i == 3:
#     break
#   i += 1

# continue
# i = 0
# while i <= 6:
#   if (i == 3):
#     i += 1
#     continue
#   print(i)
#   i += 1
  

# i = 3
# while i <= 30:
#     print(i)
#     i += 3

# i = 1
# while i <= 5:
#   print(3*i)
#   i += 1

# traverse
# num = [1,4,9,18,29,22]
# idx = 0
# while idx < len(num):
#   print(num[idx])
#   idx += 1

# t = (1,2,4,2,6,2,4,)
# x = 4
# i = 0
# while i < len(t):
#   if t[i] == x:
#     print("Found at idx: ", i, "value is",  str(x))
#   # print(t[i])
#   else:
#     print("Finding...")
#   i += 1

# nums = (1,44,33,22,66,33,66,22)
# x = 22
# idx = 0
# for i in nums:
#   if (i == x): 
#     print("Number found at idx: ", idx, x)
#     break
#   idx +=1 

# for i in range(1, 20, 2):
#   print(i)

# Function
# def sum(a,b):
#   s = a + b
#   print(s)
#   return s
  
# sum(5,7) 

# Recursion
# def show(n):
#   if (n == 0):
#     return
#   print (n)
#   show(n-1)

# show(4)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("Shahzad", 25)
# print(p1.name)
# print(p1.age)


# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age

#   def myfunc(ad, address):
#     print("Hello my name is " + ad.name, "\nand my age is")
#     print(ad.age)
#     ad.address = address
#     print("my address is" + address)

# p1 = Person("John", 36)
# p1.name = "shahzad"
# p1.age = 25
# p1.myfunc(" swat")


# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     x = self.a
#     self.a += 1
#     return x

# myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# class Students:
#   College_name = "JCH"
#   name = "Anonymous"

#   def __init__(self, name, marks):
#     self.name = name
#     self.marks = marks
#     # print("adding new student in Database")

#   def welcome(self):
#     print("Welcome student", self.name)

# s1 = Students("karan", 97)
# s1.welcome()
# print(s1.name, s1.College_name, s1.marks)

# class student:
#   def __init__(self, name, marks):
#     self.name = name
#     self.marks = marks

#   def avg(self):
#     sum = 0
#     for val in self.marks:
#       sum += val
#     print("Hi", self.name, "your avg score is:", sum/3)

#   @staticmethod
#   def hello():
#     print("hello func")

# m3 = student("Sk" ,[43,34,34])
# m3.avg()

# class Account:
#   def __init__(self, bal, acc):
#     self.balance = bal
#     self.account_no = acc
  
#   def debit(self, amount):
#     self.balance -= amount
#     print("Rs.", amount, "was debited")
#     print("total balance =", self.get_bal())

#   def credit(self, amount):
#     self.balance += amount
#     print("Rs", amount, "was credited")
#     print("total balance =", self.get_bal())

#   def get_bal(self):
#     return self.balance

# acc1 = Account(1000, 12345)
# # print(acc1.balance, acc1.account_no)
# acc1.debit(900)
# acc1.credit(1000)

# class student:
#   def __init__(self, name):
#     self.name = name

# s1 = student("shradha")
# print(s1.name)
# del s1
# print(s1.name)

# private entity
# class Account:
#   def __init__(self, acc_no, acc_pass):
#     self.acc_no = acc_no
#     self.__acc_pass = acc_pass

#   def reset_pass(self):
#     print(self.__acc_pass)

# acc1 = Account("2344","abcd")
# # print(acc1.__acc_pass)
# print(acc1.reset_pass())

# class Person:
#   __name = "anonymous"

#   def __hello(self):
#     print("Hello")

#   def welcome(self):
#     self.__hello()


# p1 = Person()
# # print(p1.__name)
# # print(p1.__hello())
# print(p1.welcome())

# Inheritance
# class Car:
#   color = "black"
#   @staticmethod
#   def start():
#     print("car started")

#   @staticmethod
#   def stop():
#     Print("car stoped")

# class ToyotaCar(Car):
#   def __init__(self, name):
#     self.name = name

# car1 = ToyotaCar("4by4")

# print(car1.name)
# car1.start()
# print(car1.color)

# Multi-level inheritance have more than one child class.
# Multiple inheritance have more than one parent class.

# class Complex:
#   def __init__(self, real, img):
#     self.real = real
#     self.img = img

#   def showNumber(self):
#     print(self.real,"i", self.img,"j")
# # dunder Function
#   def __add__(self, num2):            
#     newReal = self.real + num2.real
#     newImg = self.img + num2.img
#     return Complex(newReal, newImg)

# num1 = Complex(1,3)
# num1.showNumber()
# num2 = Complex(4, 6)
# num2.showNumber()

# # num3 = num1.add(num2)
# num3 = num1 + num2
# num3.showNumber()

# class Circle:
#   def __init__(self, radius):
#     self.radius = radius

#   def area(self):
#     return (22/7) * self.radius ** 2

#   def perimeter(self):
#     return 2 * (22/7) * self.radius

# c1 = Circle(21)
# print(c1.area())
# print(c1.perimeter())

# class Employee:
#   def __init__(self, role, dept, salary):
#     self.role = role
#     self.dept = dept
#     self.salary = salary

#   def showDetails(self):
#       print("role = ", self.role)
#       print("dept = ", self.dept)
#       print("salary = ", self.salary)

# class Engineer(Employee):
#     def __init__(self, name, age):
#       self.name = name
#       self.age = age
#       super().__init__("Engineer", "IT", "75,000")

# # e1 = Employee("manager", "Finance", "60,000")
# # e1.showDetails()
# eng1 = Engineer("Elon musk", 40)
# eng1.showDetails()

# class Order:
#   def __init__(self, item, price):
#     self.item = item
#     self.price = price

#   def __gt__(self, ordr2):
#     return self.price > ordr2.price

# ordr1 = Order("chips", 10)
# ordr2 = Order("tea", 15)

# print(ordr1 > ordr2)


# Basic again
# j = (1,2,4,2,6,2,4,)
# x = 3

# for index, value in enumerate(j):
#     try:
#         if value == x:
#             print(f"The value {value} is found at index numer {index}")
#             break
#     except Exception as e:
#         print(f"Got an error in the code : {e}")
#         print("Something went wrong")

# d = {
#     "name": "Shahzad",
#     "Address": "swat"
# }

# for x in d.items():
#     print(x)

# for key, value in d.items():
#     print(key, value)

# t = (1,2,4,5,3,5,6)
# x = 2

# for idx, val in enumerate(t):
#     if val == x:
#         print(f"value {x} is found at index {idx} ")
#     elif idx == len(t) - 1:
#          print("Tuple Ends Here...")
#     else:
#         print("Finding..")

# lst = ['shahzad','khalid','ali','fawad']
# print([name for name in lst])

# names1 = ['ahmad','ali','hasnain','izhar']
# emp_list = []
# for x in names1:
#     emp_list.append(x)
# print(emp_list)

# square all nmbers
# nmbrs = [1, 2, 3, 4, 5]
# sqrs = [x ** 2 for x in nmbrs]

# print(sqrs)

# Filter out odd numbers
# nmbrs = [1, 2, 3, 4, 5]
# even_nmbrs = [x for x in nmbrs if x % 2 ==0]
# print(even_nmbrs)

# convert string to uppercase
# strng = ["Hello","world"]
# upr = [x.upper() for x in strng]
# print(upr)

# Flatten a list of lists
# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# flate_list = [x for sublist in matrix for x in sublist]
# print(flate_list)

# list of tuples with coordinates
# coords = [(x, y) for x in range(3) for y in range(3)]
# print(coords)

# list of dictionary
# students = [
#   {"name": "khalid", "Age": 19},
#   {"name": "ubaid", "Age": 22},
#   {"name": "Ikram", "Age": 33}
# ]

# std_names = [student["name"] for student in students]
# print(std_names)

# cartesian product
# colors = ["red", 'green', "blue"]
# shapes = ["circle", "square", "triangle"]

# combination = [(color, shape) for color in colors for shape in shapes]
# print(combination)

# Regex
import re

# pattern = r"[A-Z]hop"
# text = ''' A quick brown fox jumps over the lazy dog and jumps to the next of the Shop Xhop then
#             they disappeared'''

# # match = re.search(pattern, text)
# matches = re.finditer(pattern, text)
# for match in matches:
#     print(match)

# pattern = re.compile("^[A-Z]+$")
# pattern = re.compile("^[A-Z\s]+$")
# print(pattern.search("Hello world"))
# print(pattern.search("HELLO World"))
# print(pattern.search("HELLOWORLD"))
# print(pattern.search("HELLO WORLD"))

# 3 lowercase letters
# 3 to 5 digits
# one symbol
# up to two uppercase letters (optional)

# hzu6681$K
# pattern = re.compile("^[a-z]{3}[0-9]{3,5}[^a-zA-Z0-9]{1}[A-Z]{0,2}$")
# print(pattern.search("ahd2331#AJ"))
# print(pattern.search("lll44411.K"))
# print(pattern.search("ll44411."))

# pattern = re.compile("^.{10}$")
# print(pattern.search("ahd2331#AJ"))
# print(pattern.search("lll44411.K"))
# print(pattern.search("ll44411."))

# email validation
# pattern = re.compile("^[a-zA-Z0-9\.\-_]+@{1}[A-Za-z0-9]+\.{1}[a-zA-Z]{2,3}$")
# print(pattern.search("polestohac@thraml.com"))
# print(pattern.search("+jdb@Gmail.com"))
# print(pattern.search("ll44411.com"))

# Decorators

# def greet(fx):
#     def mfx(*args, **kwargs):
#         print("Good Morning")
#         fx(*args, **kwargs)
#         print("Thanks for visit here")
#     return mfx

# @greet
# def hello():
#     print("Hello")

# @greet
# def add(a,b):
#     print(a+b)
# hello()
# # greet(add)(1,2)
# add(1,2)

# add = lambda a:a+10

# print(add(10))

# a = lambda a,b:a+b
# print(a(10,20)) 

# b = lambda a,b:(a+b, a-b)
# print(b(10,20))








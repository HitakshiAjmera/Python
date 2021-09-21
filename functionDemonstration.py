#6	Write a program to demonstrate usage of  functions , passing list as argument , recursion, local and global scope using  in Python

#Define and calling of function
def Name():
  print("Hello I am Hitakshi Ajmera")
Name() #function calling
""""OUTPUT
Hello I am Hitakshi Ajmera
"""

def product(x,y):
  print("Product of ",x," and ",y," is ",x*y)
product(5,6)
product(110,456)
product(23,45)
"""OUTPUT:-
Product of  5  and  6  is  30
Product of  110  and  456  is  50160
Product of  23  and  45  is  1035
"""

#passing list as an argument
def print_List(f):
  for x in f:
    print(x)
fruits = ["Apple", "Banana", "cherry"]
print_List(fruits)
"""OUTPUT:-
Apple
Banana
cherry
"""

#Global and local variable
a = 45 #global variable
def f1():
  print('Inside f1() a = ', a)
def f2():
  a = 23     # Variable 'a' is redefined as a local
  print('Inside f2() a = ', a)
def f3():
  global a   # Uses global keyword to modify global 'a'
  a = 76
  print('Inside f3() a =  ', a)
print('outside function a = ', a)
f1()
print('outside function a = ', a)
f2()
print('outside function a = ', a)
f3()
print('outside function a = ', a)

"""OUTPUT:-
outside function a =  45
Inside f1() a =  45
outside function a =  45
Inside f2() a =  23
outside function a =  45
Inside f3() a =   76
outside function a =  76
"""



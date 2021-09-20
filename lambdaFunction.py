#4	Write  problem codes to demonstrate usage of Lambda functions

#Program to find cube of number
cube = lambda x: x **3
print("Cube :- ",cube(15))
"""OUTPUT:-
Cube :- 3375
"""

#Program to print table
table = [lambda x=x: x * 19 for x in range(1, 11)]
for t in table:
    print(t())
"""OUTPUT:-
19
38
57
76
95
114
133
152
171
190
"""

#Programe to find smallest number
Min = lambda a,b: y if (a > b) else a
print("Minimum number is :- ",Min(111231,111461))
"""OUTPUT:-
Minimum number is :-  111231
"""

# Program to find even number using  filter() with lambda()
List = [9, 11, 42, 112, 75, 34, 88, 111, 56, 67]
FL = list(filter(lambda x: (x % 2 == 0), List))
print("List of even number :- ",FL)
"""OUTPUT:-
List of even number :-  [42, 112, 34, 88, 56]
"""

# Program to filter marks greater then 80
marks = [45, 88, 90, 78, 95, 65, 85, 82, 80 ]
M = list(filter(lambda mk: mk >= 80, marks))
print("Marks greater then 80 are :- ",M)
"""OUTPUT:-
Marks greater then 80 are :-  [88, 90, 95, 85, 82, 80]
"""

# Program to get double of a Number using map() with lambda() .
l = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
dl = list(map(lambda x: x * 2, l))
print("List of double of a Number",dl)
"""OUTPUT:-
List of double of a Number [10, 14, 44, 194, 108, 124, 154, 46, 146, 122]
"""

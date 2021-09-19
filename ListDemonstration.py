# 1	Write a program to demonstrate List in Python and List comprehension

# Creating a List
List = []

# Creating a List of branch
List = ["CI", "CO", "CT"]
print("\nList of branch in CSIT: ")
print(List)
"""output:-
List of branch in CSIT: 
['CI', 'CO', 'CT']
"""

# Creating a List of strings and accessing using index
List = ["Hitakshi", "Ajmera", "Jain"]
print("\nList Items: ")
print(List[0])
print(List[2])
"""output:-
List Items: 
Hitakshi
Jain
"""

# Creating a Multi-Dimensional List
List1 = [['Hitakshi ', 'Ajmera'], ['CI']]
print("\nMulti-Dimensional List: ")
print(List1)
#Accessing a element from a Multi-Dimensional list
print(List1[0][0])
"""output:-
Multi-Dimensional List: 
[['Hitakshi ', 'Ajmera'], ['CI']]
Hitakshi 
"""

#function for knowing size of list
print("size of Multi-Dimension list : ",len(List1))
"""output:-
size of Multi-Dimension list :  2
"""

#Slicing of a List
List2 = ['H', 'I', 'T', 'A', 'K', 'S','H', 'I']
print("\nInitial List: ",List)
# Print elements of a range using Slice operation
Sliced_List = List2[2:5]
print("Slicing elements in a range 2-5: ",Sliced_List)
"""OUTPUT:-
Initial List:  ['Hitakshi', 'Ajmera', 'Jain']
Slicing elements in a range 2-5:  ['T', 'A', 'K']
"""

Sliced_List = List2[:]
print("\nPrinting all elements using slice operation: ",Sliced_List)
"""OUTPUT:-
Printing all elements using slice operation:  ['H', 'I', 'T', 'A', 'K', 'S', 'H', 'I']
"""

#Negative index List slicing
Sliced_List = List2[::-1]
print("\nPrinting List in reverse: ",Sliced_List)
"""OUTPUT:-
Printing List in reverse:  ['I', 'H', 'S', 'K', 'A', 'T', 'I', 'H']
"""

#List Comprehension
#  list contains square of all  numbers from range 1 to 26
square = [x ** 2 for x in range(1, 26)]
print("\nsquare of numbers from 1 to 26")
print (square)
"""OUTPUT:-
square of numbers from 1 to 26
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625]
"""

odd_square = [x ** 2 for x in range(1, 30) if x % 2 == 1]
print("\nsquare of odd numbers from 1 to 30")
print (odd_square)
"""OUTPUT:-
square of odd numbers from 1 to 30
[1, 9, 25, 49, 81, 121, 169, 225, 289, 361, 441, 529, 625, 729, 841]
"""




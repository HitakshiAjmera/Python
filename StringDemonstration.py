#3	Write a program to demonstrate String in Python

# Creating a String
Str1 = 'Hitakshi Ajmera'
print("String with the use of Single Quotes: ")
print(Str1)
"""ÖUTPUT:-
Hitakshi Ajmera
"""

# String with multiple lines
Str2 = '''CI
CS
IT'''
print("\nCreating a multiline String: ")
print(Str2)
"""ÖUTPUT:-
Creating a multiline String: 
CI
CS
IT
"""

#Accessing character  from string
Str3 = "HitakshiAjmera"
print("\nFirst character of String is: ")
print(Str3[0])
print("Last character of String is: ")
print(Str3[-1])
"""ÖUTPUT:-
First character of String is: 
H
Last character of String is: 
a
"""

#String Slicing
print("\nSlicing characters from 2-11: ",Str3[2:11])
print("Slicing characters between 5th and 2nd last character: ",Str3[3:-2])
print("Reversing of string: ",Str3[::-1])
"""ÖUTPUT:-
Slicing characters from 2-11:  takshiAjm
Slicing characters between 5th and 2nd last character:  akshiAjme
Reversing of string:  aremjAihskatiH
"""
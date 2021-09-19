#2	Write a program to demonstrate Tuple in Python

# Creating tuple
tupl = ('Hitakshi', 'Ajmera')
print (tupl)
"""OUTPUT:-
('Hitakshi', 'Ajmera')
"""


# printing the length of a tuple
print("\nLength of tuple is ",len(tupl))
"""OUTPUT:-
Length of tuple is 2
"""


# concatenating 2 tuples
tupl1 = ('CI',1)
tupl2 = tupl+tupl1
print("\nConcatenated Tuple :- ", tupl2)
"""OUTPUT:-
Concatenated Tuple :-  ('Hitakshi', 'Ajmera', 'CI', 1)
"""


# creating nested tuples
tupl3 = (tupl, tupl1)
print("\nNested tuple:- ",tupl3)
"""OUTPUT:-
Nested tuple:-  (('Hitakshi', 'Ajmera'), ('CI', 1))
"""


# Slicing in Tuples
print(tupl2[1:])
print(tupl2[::-1])
print(tupl2[2:4])
"""OUTPUT:-
('Ajmera', 'CI', 1)
(1, 'CI', 'Ajmera', 'Hitakshi')
('CI',1)
"""


# Code for converting a list and a string into a tuple
List = ['CI','CS','EC','CO','IT']
print(tuple(List))
print(tuple('Hitakshi'))
"""OUTPUT:-
('CI', 'CS', 'EC', 'CO', 'IT')
('H', 'i', 't', 'a', 'k', 's', 'h', 'i')
"""


"""
Assignments on Lessons From 24 to 25
"""

from icecream import ic
from regex import B
"""

Ass 1:
-----

"""
my_tuble = "Mahmoud",
ic(my_tuble[0])
ic(type(my_tuble))

# Needed Output
# ic| my_tuble[0]: 'Mahmoud'
# ic| type(my_tuble): <class 'tuple'>


"""

Ass 2:
-----

"""
friends = ("Osama", "Ahmed", "Sayed")
friends2 = list(friends)
friends2[0] = "Elzero"
friends = tuple(friends2)
ic(friends)
ic(type(friends))
ic(len(friends))

# Output
# ic| friends: ('Elzero', 'Ahmed', 'Sayed')
# ic| type(friends): <class 'tuple'>
# ic| len(friends): 3


"""

Ass 3:
-----

"""
nums = (1, 2, 3)
letters = ("A", "B", "C")
nums_and_letters_one = nums+letters
print("nums_and_letters_one = ", nums_and_letters_one)
print(f"{len(nums_and_letters_one)} Elements")

#  Output
# nums_and_letters_one =  (1, 2, 3, 'A', 'B', 'C')
# 6 Elements


"""

Ass 4:
-----

"""
my_tuple = (1, 2, 3, 4)
a, b, _, c = my_tuple
ic(a)
ic(b)
ic(c)

# Output
# ic| a: 1
# ic| b: 2
# ic| c: 4

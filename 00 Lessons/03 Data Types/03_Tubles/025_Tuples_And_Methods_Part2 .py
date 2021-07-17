# 00 Lesson
# >> 03 Data Types
# >> 03 Tubles
# >> 025_Tubles_and_mothods_part1.py

from icecream import ic

# how interpreter knows Tuble with one element with paranthes and no paranthes is tuble:
myTuble1 = ("Mahmoud")
myTuble2 = "Mahmoud"

ic(type(myTuble1))  # ic| type(myTuble1): <class 'str'>
ic(type(myTuble2))  # ic| type(myTuble2): <class 'str'>

myTuble3 = ("Mahmoud",)
myTuble4 = "Mahmoud",

ic(len(myTuble3))  # ic| len(myTuble3): 1
ic(len(myTuble4))  # ic| len(myTuble4): 1

ic(type(myTuble3))  # ic| type(myTuble3): <class 'tuple'>
ic(type(myTuble4))  # ic| type(myTuble4): <class 'tuple'>


# [7] Operartors used in strings and lists available with tuble
# tuble Concatination:
t1 = (1, 2, 3)
t2 = (4, 5)
c = t1+t2
ic(c)  # ic| c: (1, 2, 3, 4, 5)

d = t1+("a", "b")+t2
ic(d)  # ic| d: (1, 2, 3, 'a', 'b', 4, 5)

# String , Tuble , List Repeat by (*)
s = "Mahmoud"
l = [1, 2]
t = ["A", "B"]
ic(s * 6)  # ic| s * 6: 'MahmoudMahmoudMahmoudMahmoudMahmoudMahmoud'
ic(l * 6)  # ic| l * 6: [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
ic(t * 6)  # ic| t * 6: ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B']



# Methods:
# count():
myTuble5 = (1, 2, 3, 4, 5, 6, 7, 7, 7)
ic(myTuble5.count(7))  # ic| myTuble5.count(7): 3


myTuble6 = (1, 2, 3, 4, 5, 6, 7, 7, 7)
ic(myTuble5.index(7))  # ic| myTuble5.index(7): 6
ic(myTuble5.index(7, 7))  # ic| myTuble5.index(7,7): 7


# Tubles Destructing: simple info


myTuble6 = ("A", "B", "C")

x, y, z = "A", "B", "C"
ic(x)  # ic| x: 'A'
ic(y)  # ic| y: 'B'
ic(z)  # ic| z: 'C'


ic(x)  # ic| x: 'A'
ic(y)  # ic| y: 'B'
ic(z)  # ic| z: 'C'

myTuble7 = ("A", 4, "B", "C")
# x, y, z = myTuble7  # ValueError: too many values to unpack (expected 3)
x, _, y, z = myTuble7

ic(x)  # ic| x: 'A'
ic(y)  # ic| y: 'B'
ic(z)  # ic| z: 'C'

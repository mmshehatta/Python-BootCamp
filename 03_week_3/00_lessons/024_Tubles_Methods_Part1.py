# 00 Lesson
# >> 03 Data Types
# >> 03 Tubles
# >> 024_Tubles_and_mothods_part1.py

from icecream import ic

# -----------------------------
# [1] tubles items inclosed in paranthes
# [2] you can remove paranthes if you want
# [3] tuble items are ordered , you can use index to access their items
# [4] tube are immutable => you can not add or delete
# [5] tuble items not unique
# [6] tuble can have any data type
# [7] Operartors used in strings and lists available with tuble

# -----------------------------

# [1] tubles items inclosed in paranthes
# [2] you can remove paranthes if you want

myTuble1 = ("Mahmod", "Shehata")
myTuble2 = "Mahmod", "Shehata"

ic(myTuble1)  # ic| myTuble1: ('Mahmod', 'Shehata')
ic(myTuble2)  # ic| myTuble2: ('Mahmod', 'Shehata')

ic(type(myTuble1))  # ic| type(myTuble1): <class 'tuple'>
ic(type(myTuble2))  # ic| type(myTuble2): <class 'tuple'>

# [3] tuble items are ordered , you can use index to access their items
myTuble3 = (1, 2, 3, 4, 5)
ic(myTuble3[0])  # ic| myTuble3[0]:  1
ic(myTuble3[-1])  # ic| myTuble3[-1]: 5
ic(myTuble3[-3])  # ic| myTuble3[-3]: 3

# [4] tube are immutable => you can not add or delete
myTuble4 = (1, 2, 3, 4, 5)
# myTuble4[2] = "Three"
# ic(myTuble4)    #TypeError: 'tuple' object does not support item assignment
# myTuble4[2] = []
# ic(myTuble4)    #TypeError: 'tuple' object does not support item assignment


# [5] tuble items not unique
# [6] tuble can have any data type
myTuble5 = (1, 2, "Mahmoud", "Mahmoud", 100, 100.300, True, ["a", "b", False])

ic(myTuble5[0])  # ic| myTuble5[0]: 1
ic(myTuble5[-1])  # ic| myTuble5[-1]: ['a', 'b', False]
ic(myTuble5[-2])  # ic| myTuble5[-2]: True
ic(myTuble5[-3])  # ic| myTuble5[-3]: 100.3


# [7] Operartors used in strings and lists available with tuble
# ic| myTuble5[:]: (1, 2, 'Mahmoud', 'Mahmoud', 100, 100.3, True, ['a', 'b', False])
ic(myTuble5[:])
# ic| myTuble5[0:]: (1, 2, 'Mahmoud', 'Mahmoud', 100, 100.3, True, ['a', 'b', False])
ic(myTuble5[0:])
ic(myTuble5[:4])  # ic| myTuble5[:4]: (1, 2, 'Mahmoud', 'Mahmoud')
ic(myTuble5[1:3])  # ic| myTuble5[1:3]: (2, 'Mahmoud')
ic(myTuble5[1:3:1])  # ic| myTuble5[1:3:1]: (2, 'Mahmoud')
ic(myTuble5[0:0:2])  # ic| myTuble5[0:0:2]: ()
ic(myTuble5[0:6:2])  # ic| myTuble5[0:6:2]: (1, 'Mahmoud', 100)
ic(myTuble5[1:3:2])  # ic| myTuble5[1:3:2]: (2,)

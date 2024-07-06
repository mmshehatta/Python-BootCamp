# 00 Lesson
# >> 03 Data Types
# >> 01_Numbers
# >> 020_Arithematic_Operators.py

from icecream import ic

# Arithematic Operators
# ---------------------
# [+]add
# [-]sub
# [*] mul
# [/] int divesion
# [%] modules
# [**] Exponent
# [//] floor devision
# Floor Division and the divmod() Function

# ----------------------

# Addition:
ic(1+2)  # ic| 1+2: 3
ic(10+20)  # ic| 10+20: 30
ic(1.2+2.3)  # ic| 1.2+2.3: 3.5
ic(-1+2)  # ic| -1+2: 1
ic(-1.2+2.3)  # ic| -1.2+2.3: 1.0999999999999999
ic(((2+4j)+(2+4j)))  # ic| (2+4j)+(2+4j): (4+8j)


# subtraction:
ic(1-2)  # ic| 1-2: -1
ic(10-20)  # ic| 10-20: -10
ic(1.2-2.3)  # ic| 1.2-2.3: -1.0999999999999999
ic(-1-2)  # ic| -1-2: -3
ic(-1.2-2.3)  # ic| -1.2-2.3: -3.5

# multiplaction:
ic("multiplaction:")
ic(10*20)  # ic| 10*20: 200
ic(5+10*20)  # ic| 5+10*20: 205
ic((5+10)*20)  # ic| (5+10)*20: 300


# Division:
ic("Division:")
ic(100/20)  # ic| 100/20: 5.0
ic(int(100/20))  # ic| int(100/20): 5

# moduls:
ic("moduls:")

ic(8 % 2)  # ic| 8 % 2: 0
ic(9 % 2)  # ic| 9 % 2: 1
ic(20 % 4)  # ic| 20 % 4: 0
ic(22 % 4)  # ic| 22 % 4: 2


# exponent:
ic("exponent:")

ic(2**5)  # ic| 2**5: 32

# floor div:
ic("floor div:")
ic(100//20)  # ic| 100//20: 5
ic(119//20)  # ic| 119//20: 5
ic(120//20)  # ic| 120//20: 6
ic(130//20)  # ic| 130//20: 6
ic(139//20)  # ic| 139//20: 6
ic(140//20)  # ic| 140//20: 7
ic(142//20)  # ic| 142//20: 7

# https://www.codingem.com/python-floor-division/#Floor_Division_in_Python
# Floor Division and the divmod() Function
# In Python, the built-in divmod() function calculates both the floor division
#  and the modulo between two numeric values.
# Syntax:
# r = divmod(a, b)
# >>> napples, nleftovers = divmod(7, 3)
# >>> napples
# 2
# >>> nleftovers
# 1
ic("Floor Division and the divmod() Function: ")
# Table of Contents::
# Floor Division in Python
# Regular Division in Python
# Math.floor() Function in Python
# Floor Division
# Floor Division with Negative Numbers
# Floor Division with Floats
# Floor Division and Modulo in Python
# Floor Division and the divmod() Function
# Floor Division Precedence
# Advanced Use of Floor Division
# The __floordiv__() Method in Python
# Conclusion
# Further Reading
napples, nleftovers = divmod(7, 3)
ic(napples)
ic(nleftovers)
# c| 'Floor Division and the divmod() Function: '
# ic| napples: 2
# ic| nleftovers: 1

# --------------------------
# -- Assignment Operators --
# --------------------------
# =
# +=
# -=
# *=
# /=
# **=
# %=
# //=
# Refs:
# [1] https://www.tutorialspoint.com/python/assignment_operators_example.htm
# [2] https://www.w3schools.com/python/gloss_python_assignment_operators.asp
# [3] https://stackoverflow.com/questions/38922606/what-is-x-1-and-x-1 	(x = x >> 3)

# --------------------------
from icecream import ic

# --------------------------
# -- Comparison Operators --
# --------------------------
# [ == ] Equal
# [ != ] Not Equal
# [ > ] Greater Than
# [ < ] Less Than
# [ >= ] Greater Than Or Equal
# [ <= ] Less Than Or Equal
# --------------------------

# Equal + Not Equal

print(100 == 100)
print(100 == 200)
print(100 == 100.00)

print("#" * 50)

print(100 != 100)
print(100 != 200)
print(100 != 100.00)

print("#" * 50)

# Greater Than + Less Than

print(100 > 100)
print(100 > 200)
print(100 > 100.00)
print(100 > 40)

print("#" * 50)

print(100 < 100)
print(100 < 200)
print(100 < 100.00)
print(100 < 40)

print("#" * 50)

# Greater Than Or Equal + Less Than Or Equal

print(100 >= 100)
print(100 >= 200)
print(100 >= 100.00)
print(100 >= 40)

print("#" * 50)

print(100 <= 100)
print(100 <= 200)
print(100 <= 100.00)
print(100 <= 40)

print("#" * 50)

# >> 00 Lesson
# >> 08 Functions
# >> 072 - Built In Functions Part 4.py
from os import sep
from icecream import ic
# -------------------------------------------------
# --- 072 - Built In Functions Part 4.py -------------------------------------------------

# ------------------------------------------------
# [1] Map take a function + iterator
# [2] Map called map because it map the fun on each element in the iterator
# [2] Fun can be pre-defiend or built-in or lambda function
# ------------------------------------------------

# built-in fun:
myFloats = [1.12, 2.5, 3.4]

for n in map(int, myFloats):
    print(n)  # 1 2 3

# pre-defined fun :


def myFormattedText(text):
    return f"-{text.strip().capitalize()}- "


myTexts = ["mahmoud", "ahmed", "ali"]

for name in map(myFormattedText,  myTexts):
    print(name)

# -Mahmoud-
# -Ahmed-
# -Ali-


# lampda fun:
for name in map(lambda text:  f"-{text.strip().capitalize()}- " ,myTexts):
    print(name)
# -Mahmoud-
# -Ahmed-
# -Ali-


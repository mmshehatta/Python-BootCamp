
# >> 00 Lesson
# >> 08 Functions
# >> 072 - Built In Functions Part 4.py
from icecream import ic
# -------------------------------------------------
# --- 072 - Built In Functions Part 4.py -------------------------------------------------

# ------------------------------------------------
# [1] filter take a function + iterator
# [2] filter called map because it map the fun on each element in the iterator
# [3] Fun can be pre-defiend or built-in or lambda function
# [4] filter out all elements for which fuction return True
# [5] Fun need to return bollean value
# ------------------------------------------------

# pre-defined fun:

def check_my_num(num):
    ''' this fun must to return T or F to work with filter '''
    if num < 10:
        return num


def check_my_num2(num):
    ''' this fun must to return T or F to work with filter '''
    if num < 10:
        return True


myNumbers = [1, 2, 0, -1, -2]

myRes = filter(check_my_num, myNumbers)

for num in myRes:
    ic(num)   # 1 2 -1 -2 ..zero not included because it is falsy value can included if we return True
# ic| num: 1
# ic| num: 2
# ic| num: -1
# ic| num: -2

myRes2 = filter(check_my_num2, myNumbers)
for num in myRes2:
    ic(num)  # 1 2 0 -1 -2
# ic| num: 1
# ic| num: 2
# ic| num: 0
# ic| num: -1
# ic| num: -2


# built-in fun:
for t in filter(bool, (1, 2, 3, 0, False, '', [])):
    ic(t)

# ic| t: 1
# ic| t: 2
# ic| t: 3


# lampda fun:
for number in filter(lambda num: num < 10, myNumbers):
    ic(number)
# ic| number: 1
# ic| number: 2
# ic| number: 0
# ic| number: -1
# ic| number: -2

persons = ["Ahmed", "Mahmoud", "Majed", "Maher", "Amr", "Ali" , "murad"]

for person in filter(lambda name: name.startswith("M"), persons):
    ic(person)
# ic| person: 'Mahmoud'
# ic| person: 'Majed'
# ic| person: 'Maher'
# ic| person: 'murad'

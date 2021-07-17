
# >> 00 Lesson
# >> 08 Functions
# >> 069 - Built In Functions Part 1.py
from icecream import ic
# -------------------------------------------------
# --- 069 - Built In Functions Part 1.py -------------------------------------------------

# ------------------------------------------------
# all()
# any()
# bin()
# id()
# ------------------------------------------------

# 1.all():
# all: (__iterable: Iterable[object]) -> bool
# Return True if bool(x) is True for all values x in the iterable.
# If the iterable is empty, return True.
a = [1, 2, 3, 4]
# ic| 'all elemrnt are true'
if all(a):
    ic("all elemrnt are true")
else:
    ic("at least one element is false")  

b=[1,2,3,[]]
ic ('at least one element is false')
if all(b):
    ic("all elemrnt are true")
else:
    ic("at least one element is false")


# 2.any():
# any: (__iterable: Iterable[object]) -> bool
# Return True if bool(x) is True for any x in the iterable.
# If the iterable is empty, return False.

x = [1, 2, 3, 4]
# ic| 'at least one element is True'
if any(x):
    ic("at least one element is True")
else:
    ic("There is no element is true but all false")


# 3.bin():
# bin: (__number: int | SupportsIndex) -> str
# Return the binary representation of an integer.
# >>> bin(2796202)  '0b1010101010101010101010'
ic(bin(10))  #ic| bin(10): '0b1010'


# 4.id():
# id: (__obj: object) -> int
# Return the identity of an object.
# This is guaranteed to be unique among simultaneously existing objects. (CPython uses the object's memory address.) # id

a=1
b=2
ic(id(a))  #ic| id(a): 9788608
ic(id(b))  #ic| id(b): 9788640

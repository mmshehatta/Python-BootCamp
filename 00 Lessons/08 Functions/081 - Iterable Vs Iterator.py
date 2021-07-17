# >> 00 Lesson
# >> 08 Functions
# >> 081 - Iterable Vs Iterator.py
from icecream import ic
# -------------------------------------------------
# ---   081 - Iterable Vs Iterator      -----------
# ------------------------------------------------
# iterable:
# [1] Object contains Data that can be iterated upon 
# [2] Examples (string , list ,tuble ,set , dict)
# ------------------------------------------------

# ------------------------------------------------
# iterator:
# [1] Object used to iterate over Iteratable using next() Method Return 1 element at a time  
# [2] You can generate Iterator from Iteratable when using iter method()
# [3] for loop already calls iter() method on the Iteratable behind the scene 
# [4] Gives "StopIteration" if theres no next element 
# ------------------------------------------------

# iterable:

myStr = "Mahmoud"
for s in myStr:
    ic(s)
# ic| s: 'M'
# ic| s: 'a'
# ic| s: 'h'
# ic| s: 'h'
# ic| s: 'm'
# ic| s: 'o'
# ic| s: 'u'
# ic| s: 'd'


# iterator:
myIterator = iter(myStr)
ic(next(myIterator))
ic(next(myIterator))
ic(next(myIterator))
ic(next(myIterator))
ic(next(myIterator))
ic(next(myIterator))
ic(next(myIterator))
# ic(next(myIterator))
# ic| next(myIterator): 'M'
# ic| next(myIterator): 'a'
# ic| next(myIterator): 'h'
# ic| next(myIterator): 'm'
# ic| next(myIterator): 'o'
# ic| next(myIterator): 'u'
# ic| next(myIterator): 'd'
# Traceback (most recent call last):
#   File "/media/mahmoud/Mon3at3(100_GB)/From-Desktop/01 Back-End/00 Python (Basics and OPP) Projects  🐍/01 By_Elzero/GitHup/Python-BootCamp/00 Lessons/08 Functions/081 - Iterable Vs Iterator.py", line 45, in <module>
#     ic(next(myIterator))
# StopIteration





# for loop already calls iter() method on the Iteratable behind the scene 

for s in iter("Mahmoud"):
  ic(s)
# ic| s: 'M'
# ic| s: 'a'
# ic| s: 'h'
# ic| s: 'm'
# ic| s: 'o'
# ic| s: 'u'
# ic| s: 'd'
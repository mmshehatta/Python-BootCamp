
# 00 Lesson
# >> 03 Data Types
# >> 03 Sets
# >> 028_set_methods_p2.py

from icecream import ic


# issuperset():
# (s: Iterable) -> bool
# Report whether this set contains another set

a = {1, 2, 3, 4}
b = {1, 2, 3}
c = {1, 2, 3, 4, 5}

ic(a.issuperset(b))  # ic| a.issuperset(b): True
ic(a.issuperset(c))  # ic| a.issuperset(c): False


# issubset():
# (s: Iterable) -> bool
# Report whether another set contains this set.

e = {1, 2, 3, 4}
f = {1, 2, 3}
g = {1, 2, 3, 4, 5}

ic(f.issubset(e))  #ic| f.issubset(e): True
ic(f.issubset(g))  #ic| f.issubset(g): True
ic(g.issubset(e))  #ic| g.issubset(e): False

# isdisjoin():
# (s: Iterable) -> bool
# Return True if two sets have a null intersection.

k = {1, 2, 3, 4}
l = {1, 2, 3}
ic(k.isdisjoint(l))  #ic| k.isdisjoint(l): False

y = {"1", "2", "3"}
x = {1, 2, 3, 4}
ic(x.isdisjoint(y))  #ic| x.isdisjoint(y): True


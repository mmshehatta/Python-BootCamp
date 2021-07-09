
# 00 Lesson
# >> 03 Data Types
# >> 03 Sets
# >> 028_set_methods_p2.py

from icecream import ic


# defference(): or(a-b)
# (*s: Iterable) -> Set[int]
# Return the difference of two or more sets as a new set.
# (i.e. all elements that are in this set but not the others.)

a = {1, 2, 3, 4, }
b = {1, 2, "Ali", "Amr"}
ic(a)  # ic| a: {1, 2, 3, 4}
ic(a.difference(b))  # ic| a.difference(b): {3, 4}
ic(a - b)  # ic| a - b: {3, 4}


# # defference_update():
# (*s: Iterable) -> None
# Remove all elements of another set from this set.

c = {1, 2, 3, 4, }
d = {1, 2, "Ali", "Amr"}

ic(c)  # ic| c: {1, 2, 3, 4}
c.difference_update(d)
ic(c)  # ic| c: {3, 4}


# intersection(): == e&f
# (*s: Iterable) -> Set[int]
# Return the intersection of two sets as a new set.
# (i.e. all elements that are in both sets.)

e = {1, 2, 3, 4, }
f = {1, 2, "Ali", "Amr"}

ic(e)  # ic| e: {1, 2, 3, 4}
ic(e.intersection(f))  # ic| e.intersection(f): {1, 2}
ic(e)  # ic| e: {1, 2, 3, 4}


# intersection_update():
# (*s: Iterable) -> None
# Update a set with the intersection of itself and another.

g = {1, 2, 3, 4}
h = {1, 2, "Ali", "Amr"}
ic(g)  # ic| g: {1, 2, 3, 4}
g.intersection_update(h)
ic(g)  # ic| g: {1, 2}


# symmetric_difference(): ==  l^m
# (s: Iterable) -> Set
# Return the symmetric difference of two sets as a new set.
# (i.e. all elements that are in exactly one of the sets.)


l = {1, 2, 3, 4}
m = {1, 2, "Ali", "Amr"}

ic(l)  # ic| l: {1, 2, 3, 4}
# ic| l.symmetric_difference(m): {'Amr', 3, 4, 'Ali'}
ic(l.symmetric_difference(m))
ic(l)  # ic| l: {1, 2, 3, 4}


# symmetric_difference_update():  == i^j
# (s: Iterable) -> None
# Update a set with the symmetric difference of itself and another.

i = {1, 2, 3, 4}
j = {1, 2, "Ali", "Amr"}

ic(i)   #ic| i: {1, 2, 3, 4}
i.symmetric_difference_update(j)
ic(i)   #ic| i: {3, 4, 'Ali', 'Amr'}





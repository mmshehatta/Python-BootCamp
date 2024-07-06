
# 00 Lesson
# >> 03 Data Types
# >> 03 Sets
# >> 027_set_methods_p1.py

from icecream import ic


# clear():
a = {1, 2, 3}
a.clear()
ic(a)  # ic| a: set()

# unio():
b = {"one", "two", "three"}
c = {1, 2, 3}
d = {True, False}
ic(b | c)         # ic| b | c: {1, 2, 3, 'two', 'three', 'one'}
ic(b | c | d)     # ic| b | c | d: {'three', 1, 2, 3, False, 'one', 'two'}
ic(b.union(c))    # ic| b.union(c): {1, 2, 3, 'two', 'three', 'one'}
ic(b.union(c, d))  # ic| b.union(c,d): {'three', 1, 2, 3, False, 'two', 'one'}


# add():
e = {1, 2, 3, 4}
# e.add(5, 6)
# ic(e)   #TypeError: add() takes exactly one argument (2 given)
e.add(5)  #
e.add(6)  #
ic(e)  # ic| e: {1, 2, 3, 4, 5, 6}


f = {1, 2, 3}
g = f.copy()

ic(g)  # ic| g: {1, 2, 3}
f.add(4)
ic(g)  # ic| g: {1, 2, 3}


# remove():
h = {1, 2, 3}
h.remove(1)
ic(h)  # ic| h: {2, 3}
# h.remove(1)
# ic(h)  # KeyError: 1
# h.remove(4)
# ic(h)  # KeyError: 4


# dicard()
j = {1, 2, 3}
j.discard(1)
ic(j)  # ic| j: {2, 3}
j.discard(1)
ic(j)  # ic| j: {2, 3} no error


# pop(): remove random element
k = {1, 2, 3}
k.pop()
ic(k)  # ic| k: {2, 3}
k.pop()
ic(k)  # ic| k: {3}


# update():
l = {1, 2, 3}
m = {1, 2, "A", "b"}

l.update(["css", "js"])
l.update(m)

ic(l)   #ic| l: {1, 2, 3, 'b', 'css', 'A', 'js'}

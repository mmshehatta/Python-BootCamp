# ---------------------
# -- Type Conversion --
# ----------------------
from icecream import ic
# str()

a = 10
ic(type(a))
ic(type(str(a)))

ic("#" * 50)

# tuple()

c = "Osama"  # String
d = [1, 2, 3, 4, 5]  # List
e = {"A", "B", "C"}  # Set
f = {"A": 1, "B": 2}  # Dictionary

ic(tuple(c))
ic(tuple(d))
ic(tuple(e))
ic(tuple(f))

# list()

c = "Osama"  # String
d = (1, 2, 3, 4, 5)  # Tuple
e = {"A", "B", "C"}  # Set
f = {"A": 1, "B": 2}  # Dictionary

ic(list(c))
ic(list(d))
ic(list(e))
ic(list(f))

ic("#" * 50)

# set()

c = "Osama"  # String
d = (1, 2, 3, 4, 5)  # Tuple
e = ["A", "B", "C"]  # List
f = {"A": 1, "B": 2}  # Dictionary

ic(set(c))
ic(set(d))
ic(set(e))
ic(set(f))

ic("#" * 50)

# dict()

d = (("A", 1), ("B", 2), ("C", 3))  # Tuple
e = [["One", 1], ["Two", 2], ["Three", 3]]  # List

ic(dict(d))
ic(dict(e))
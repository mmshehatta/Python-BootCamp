
# >> 00 Lesson
# >> 08 Functions
# >> 071 - Built In Functions Part 3.py
from icecream import ic
# -------------------------------------------------
# --- 071 -Built In Functions Part 3.py -------------------------------------------------

# ------------------------------------------------
# abs()
# pow()
# min()
# max()
# slice()
# ------------------------------------------------

# 1.abs()
# abs: (__x: SupportsAbs[_T@abs]) -> _T@abs
# Return the absolute value of the argument.
ic(abs(100))  # ic| abs(100): 100
ic(abs(-100))  # ic| abs(-100): 100
ic(abs(1.5))  # ic| abs(1.5): 1.5
ic(abs(-1.5))  # ic| abs(-1.5): 1.5

# 2.pow():
# (base: int, exp: int, mod: None = ...) -> Any
# Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments

# Some types, such as ints, are able to use a more efficient algorithm when invoked using the three argument form.

ic(pow(2, 5))  # ic| pow(2, 5): 32
ic(pow(2, 5, 10))  # ic| pow(2, 5, 10): 2


# # 3.min():
# min(iterable, *[, default=obj, key=func]) -> value min(arg1, arg2, *args, *[, key=func]) -> value

# With a single iterable argument, return its smallest item. The default keyword-only argument specifies an object to return if the provided iterable is empty. With two or more arguments, return the smallest argument.

ic(min(1, 2, 3, 4, -2, -5))  # ic| min(1,2,3,4,-2,-5): -5

myNums = (1, 2, 3, 4, 0, -1)
ic(min(myNums))  # ic| min(myNums): -1

myStrs = ("A", "B", "mahmoud")
myStrs2 = ("x", "w", "mahmoud")
ic(min(myStrs))  # ic| min(myStrs): 'A'
ic(min(myStrs2))  # ic| min(myStrs2): 'mahmoud'


# 4.max():
# max(iterable, *[, default=obj, key=func]) -> value max(arg1, arg2, *args, *[, key=func]) -> value

# With a single iterable argument, return its biggest item. The default keyword-only argument specifies an object to return if the provided iterable is empty. With two or more arguments, return the largest argument.
ic(max(1, 2, 3, 4, -2, -5))  # ic| max(1,2,3,4,-2,-5): 4
myNums2 = (1, 2, 3, 4, 0, -1)
ic(max(myNums))  # ic| max(myNums): 4
myStrs = ("A", "B", "mahmoud")
ic(max(myStrs))  # ic| max(myStrs): 'mahmoud'


# slice():
# (stop: Any) -> None
# slice(stop) slice(start, stop[, step])

# Create a slice object. This is used for extended slicing (e.g. a[0:10:2]).
a = [1, 2, 3, 4, 5, 6]
ic(a[:])        #ic| a[:]: [1, 2, 3, 4, 5, 6]
ic(a[:4])       #ic| a[:4]: [1, 2, 3, 4]
ic(a[1:3])      #ic| a[1:3]: [2, 3]
ic(a[1:5:2])    #ic| a[1:5:2]: [2, 4]

# slice do the same above thing.
ic(a[slice(0,6)])     #
ic(a[slice(4)])       #
ic(a[slice(1,3)])     #
ic(a[slice(1,5,2)])   #



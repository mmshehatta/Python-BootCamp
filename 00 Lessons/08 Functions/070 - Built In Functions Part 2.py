
# >> 00 Lesson
# >> 08 Functions
# >> 070 - Built In Functions Part 2.py
from os import sep
from icecream import ic
# -------------------------------------------------
# --- 070 - Built In Functions Part 2.py -------------------------------------------------

# ------------------------------------------------
# sum()
# round()
# range()
# print()
# ------------------------------------------------

# 1.sum(iterable , start?)
# sum(__iterable: Iterable[_T@sum], start: _S@sum) -> (_T@sum | _S@sum)

a = [1, 2, 3]
ic(sum(a))  # ic| sum(a): 6
ic(sum(a, 1))  # ic| sum(a,1): 7

b = [1, 2, 3, "A"]

# ic(sum(b))   #TypeError: unsupported operand type(s) for +: 'int' and 'str'

# 2.round(num , numofdigits):
# round(number: SupportsRound, ndigits: None) -> int

ic(round(100.444))  # ic| round(100.444): 100
ic(round(100.444, 2))  # ic| round(100.444 , 2): 100.44
ic(round(100.444, 3))  # ic| round(100.444 , 3): 100.444
ic(round(100.544))  # ic| round(100.544): 101
ic(round(100.544, 1))  # ic| round(100.544 , 1): 100.5
ic(round(100.544, 2))  # ic| round(100.544 , 2): 100.54
ic(round(100.544, 3))  # ic| round(100.544 , 3): 100.544


# 3.range()
# class range()
# range(stop) -> range object range(start, stop[, step]) -> range object

# Return an object that produces a sequence of integers from start (inclusive) to stop (exclusive) by step. range(i, j) produces i, i+1, i+2, ..., j-1. start defaults to 0, and stop is omitted! range(4) produces 0, 1, 2, 3. These are exactly the valid indices for a list of 4 elements. When step is given, it specifies the increment (or decrement).

l = [1, 2, 3, 4]
for i in range(len(l)):
    print(i, end=" ")  #0 1 2 3




# 4.print():
# print: (*values: object, sep: str | None = ..., end: str | None = ..., file: SupportsWrite[str] | None = ..., flush: bool = ...) -> None
# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

# Prints the values to a stream, or to sys.stdout by default. Optional keyword arguments:
# file: a file-like object (stream); defaults to the current sys.stdout.
# sep: string inserted between values, default a space.
# end: string appended after the last value, default a newline.
# flush: whether to forcibly flush the stream.




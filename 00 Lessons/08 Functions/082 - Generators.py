
# >> 00 Lesson
# >> 08 Functions
# >> 082 - Generators.py
from icecream import ic

# ------------------------------------------------
# [1] Generator is a function with "Yield" Keyword insteed of return 
# [2] It support iteration and return generator iterator by calling "yield"
# [3] Generator function can have one or more yield
# [4] By using next() it Resume fro where it called "yield" not from beginning
# [5] when called it is not run automatically , it is only give you the control
# ------------------------------------------------

# example1: simple genetator 
def myGenerator():
    print("first item")  #first item , ic| next(myGen): 1
    yield 1
    print("Second Item")
    yield 2
    print("Third Item")
    yield 3

myGen = myGenerator()
ic(next(myGen))
ic(next(myGen))
ic(next(myGen))
# ----------------
# first item
# ic| next(myGen): 1
# Second Item
# ic| next(myGen): 2
# Third Item
# ic| next(myGen): 3


# exampl2: squares Generator:
def sq_generator(number):
    for i in range(number):
        yield i*i

seq = sq_generator(5)
ic(next(seq))
ic(next(seq))
ic(next(seq))
ic(next(seq))
ic(next(seq))
# --------------
# ic| next(seq): 0
# ic| next(seq): 1
# ic| next(seq): 4
# ic| next(seq): 9
# ic| next(seq): 16


# example3 : generator-expression:
seq_by_gen_exp = (i*i for i in range(5))
# ic(type(seq_by_gen_exp)) #ic| type(seq_by_gen_exp): <class 'generator'>
# ic(next(seq_by_gen_exp))
# ic(next(seq_by_gen_exp))
# ic(next(seq_by_gen_exp))
# ic(next(seq_by_gen_exp))
# ic(next(seq_by_gen_exp))
# --------------
# ic| next(seq_by_gen_exp): 0
# ic| next(seq_by_gen_exp): 1
# ic| next(seq_by_gen_exp): 4
# ic| next(seq_by_gen_exp): 9
# ic| next(seq_by_gen_exp): 16


# above example by using while loop:
print("*"*50)

# while True:
#     try:
#         ic(next(seq_by_gen_exp))
#     except StopIteration:
#         break

# -----------
# **************************************************
# ic| next(seq_by_gen_exp): 0
# ic| next(seq_by_gen_exp): 1
# ic| next(seq_by_gen_exp): 4
# ic| next(seq_by_gen_exp): 9
# ic| next(seq_by_gen_exp): 16

# by for loop:
print("*"*50)

for num in seq_by_gen_exp:
    ic(num)

# **************************************************
# ic| num: 0
# ic| num: 1
# ic| num: 4
# ic| num: 9
# ic| num: 16
# >> 00 Lesson
# >> 08 Functions
# >>085 - Decorators - Practical Speed Test.py
from icecream import ic
from time import time

#############################################################
# >> 085 - Decorators - Practical Speed Test.py
#############################################################


def speedTest(fun):

    def wrapper():
        start = time()
        fun()
        end = time()
        ic(f"excuetion time = {end -start}")
    return wrapper


@speedTest
def bigLoop():
    # for i in range(20000): # ic| f"excuetion time = {end -start}": 'excuetion time = 0.20180273056030273'
    for i in range(200000):  #ic| f"excuetion time = {end -start}": 'excuetion time = 5.897944927215576'
        print(i)
bigLoop()  
        
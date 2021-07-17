
# >> 00 Lesson
# >> 08 Functions
# >> 074 - Built In Functions Part 4.py
from icecream import ic
from functools import reduce
# -------------------------------------------------
# --- 074 - Built In Functions Part 4.py -------------------------------------------------

# ------------------------------------------------
# [1] Reduce take a function + iterator
# [2] Reduce run a function on first and second element and give result
# [3] then run function on the result and the third element
# [4] then run function on the result and the fourth element and so on
# [5] till one element os left and this the result of the reduce
# [6] Fun can be bre-defiend or lambda
# ------------------------------------------------

# pre-defined fun:


def sumAll(n1, n2):
    return n1+n2


myNumbers = [1, 2, 3, 4, 5, 6]

result = reduce(sumAll, myNumbers)

ic(result)  # ic| result: 21
# (((((1+2)+3)+4)+5)+6)


# lambda fun:

ic( reduce(lambda n1,n2 : n1+n2 , myNumbers) )  #ic| reduce(lambda n1,n2 : n1+n2 , myNumbers): 21

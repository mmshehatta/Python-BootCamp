

# 00 Lesson
# >> 03 Data Types
# >> 06 Boolean
# >> 033_boolean.py

from icecream import ic
# -----------------
# --- Boolean----
# -----------------
#  [1] in programming we need to check if code is true or false
#  [2] 
# -----------------
name = " "
ic(name.isspace())  #ic| name.isspace(): True

ic(100 > 200)      #ic| 100 > 200: False
ic(100 > 100)      #ic| 100 > 100: False
ic(100 > 90)      #ic| 100 > 60: True



# test truthey value be built in bool() function:
ic(bool("Mahmoud"))    #ic| bool("Mahmoud"): True
ic(bool(1))            #ic| bool(1): True
ic(bool(-1))           #ic| bool(-1): True
ic(bool(True))         #ic| bool(True): True
ic(bool((1,2,3)))      #ic| bool((1,2,3)): True
ic(bool([1,2]))        #ic| bool([1,2]): True
ic(bool({'one':1}))    #ic| bool({'one':1}): True


# test Falsey value be built in bool() function:
ic(bool(""))         #ic| bool(""): False
ic(bool(0))          #ic| bool(0): False
ic(bool(False))      #ic| bool(False): False
ic(bool(()))         #ic| bool(()): False
ic(bool([]))         #ic| bool([]): False
ic(bool({}))         #ic| bool({}): False
ic(bool(None))       #ic| bool(None): False



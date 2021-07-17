
# >> 00 Lesson
# >> 08 Functions
# >>062 - Function Scope.py
from icecream import ic
# ----------------------------------------------------------------
# --- 062 - Function Scope.py ----
# ---------------------------------------------------------------


x = 10  #Globla Scope

def one():
    global x
    x=2
    ic(f"variable form Function scope: {x}")


ic(f"variable form global scope:{x}")  #ic| f"variable form global scope:{x}": 'variable form global scope:10'
one()                                  #ic| f"variable form Function scope: {x}": 'variable form Function scope: 10'
one()                                  #ic| f"variable form Function scope: {x}": 'variable form Function scope: 2'

def two():
    x = 4
    ic(f"variable form Function2 scope:{x}") 

two()                                #ic| f"variable form Function2 scope:{x}": 'variable form Function2 scope:4'





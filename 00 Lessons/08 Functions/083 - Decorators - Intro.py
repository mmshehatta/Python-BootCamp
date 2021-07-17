# >> 00 Lesson
# >> 08 Functions
# >> 083 - Decorators - Intro.py
from icecream import ic

# ------------------------------------------------
# [1] Decorator somtimes called Meta programming
# [2] Every thing in python is object also  functions
# [3] Decorator takes function add some functionality and return it
# [4] Decorator wrap other function and enhance their behavouir
# [5] Decorator is heigher order function (function accept other fun as param)
# [6] Funion take Decorator affect by 2-ways , as param or as @Decorator upon function name
# ------------------------------------------------

def myDecorator(fun):

    def nestedFun():
        print("before fun : ")
        fun()
        print("After fun  : ")
    return nestedFun   #return all data



def sayHello():
    print("print from sayHello ! ")


# Decoration method1:
afterDecoration = myDecorator(sayHello)
afterDecoration() 
print("#" *30)
# --------------- 
# before fun : 
# print from sayHello ! 
# After fun  : 


# Decoration method2:
@myDecorator
def sayHello():
    print("print from sayHello ! ")

sayHello()  
##############################
# before fun : 
# print from sayHello ! 
# After fun  : 



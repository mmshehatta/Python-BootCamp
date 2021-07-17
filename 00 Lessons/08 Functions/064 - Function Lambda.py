


# >> 00 Lesson
# >> 08 Functions
# >> 064 - Function Lambda.py
from icecream import ic
# -------------------------------------------------
# --- 064 - Function Lambda.py ----
#           anonymous function
# -------------------------------------------------
# [1] it has no name.
# [2] you can called it inline without defining it.
# [3] you can use it in return data from another function 
# [4] lambda used for simple function and def handel large tasks
# [5] lambda function is one single expression not block of code
# [6] lambda type is function
# -------------------------------------------------

# in past if we need to write function with one line of code:

def say_hello(name):return f"Hello {name}"
ic(say_hello("Mahmoud"))    #ic| say_hello("Mahmoud"): 'Hello Mahmoud'


def say_hello2(name,age):return f"Hello {name} your age is {age}"
ic(say_hello2("Mahmoud",25))    #ic| say_hello2("Mahmoud",25): 'Hello Mahmoud your age is 25'



# now we can user anonymous or lambda expression

hello = lambda name , age: f"Hello {name} age is {age}"

ic(hello("Ahmed",25))   #ic| hello("Ahmed",25): 'Hello Ahmed age is 25'



# to check name of lamda functions:
ic(say_hello.__name__)   #ic| say_hello.__name__: 'say_hello'
ic(hello.__name__)       #ic| hello.__name__: '<lambda>'


# to chek type of lambda fun:
ic(type(hello))   #ic| type(hello): <class 'function'>






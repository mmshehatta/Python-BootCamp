# >> 00 Lesson
# >> 08 Functions
# >> 057 - 057 - Function Parameters And Arguments.py
from icecream import ic
# ----------------------------------------
# ---Function Parameters And Arguments----
# ----------------------------------------

# Before function:
a, b, c = ("Mahmoud", "Ahmed", "Ali")
ic(f"Hello {a}")  # ic| f"Hello {a}": 'Hello Mahmoud'
ic(f"Hello {b}")  # ic| f"Hello {b}": 'Hello Ahmed'
ic(f"Hello {c}")  # ic| f"Hello {c}": 'Hello Ali'

# After function:


def say_hello(name):
    return f"Hello {name}"


ic(say_hello(a))  # ic| say_hello(a): 'Hello Mahmoud'
ic(say_hello(b))  # ic| say_hello(b): 'Hello Ahmed'
ic(say_hello(c))  # ic| say_hello(c): 'Hello Ali'


# example on finction:
# we will buld fun called sum takes 2 params and return some

def sum(n1, n2):
    return n1+n2


ic(sum(1, 2))  # ic| sum(1,2): 3
ic(sum(-100, 200))  # ic| sum(-100,200): 100
# ic(sum(1, 2, 3))          #TypeError: sum() takes 2 positional arguments but 3 were given
# ic(sum(1))                #TypeError: sum() missing 1 required positional argument: 'n2'
# ic(sum(1,"Mahmoud"))      #TypeError: unsupported operand type(s) for +: 'int' and 'str'
# ic(sum(1,"Mahmoud"))      #TypeError: unsupported operand type(s) for +: 'int' and 'str'
# ic(sum(1,int("Mahmoud"))) #ValueError: invalid literal for int() with base 10: 'Mahmoud'
ic(sum(1, int("5")))  # ic| sum(1,int("5")): 6


# from the a bove example we find some error and we will haned them here!
def correct_sum(n1, n2):
    if type(n1) == 'int' or type(n2) == 'int':
        return n1 + n2
    else:
        print("Onley integers are allowed!")


ic(correct_sum(1, 2))  # ic| correct_sum(1, 2): 3
ic(correct_sum(-100, 200))  # ic| correct_sum(-100, 200): 100
ic(correct_sum(1, "Mahmoud"))  # Onley integers are allowed!


# function to return full name as : Mahmoud S Muhammed

def get_full_name(fname, mname, lname):
    ic(f"{fname.strip().capitalize()} {mname.capitalize():.1s} {lname.capitalize()}")


get_full_name("mahmoud","shehata","muhammed")
#ic| f"{fname.strip().capitalize()} {mname.capitalize():.1s} {lname.capitalize()}": 'Mahmoud S Muhammed'
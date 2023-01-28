# -----------------------------------------------
# -- Installing And Use Pylint For Better Code --
# -----------------------------------------------

"""
This is My Module
To Create Function
To Say Hello
"""

def say_hello(name):
    '''This Function Only Say Hello To Someone'''
    msg = "Hello"
    return f"{msg} {name}"

say_hello("Ahmed")

# After Running : pylint main.py
# Your code has been rated at 10.00/10 (previous run: 7.50/10, +2.50)

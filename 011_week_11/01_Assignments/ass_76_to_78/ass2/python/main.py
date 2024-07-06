# import my_mod 
# print(dir(my_mod)) # ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'say_hello', 'say_welcom']

from my_mod import *

print(say_welcome("Mahmoud"))
print(say_hello("Mahmoud"))

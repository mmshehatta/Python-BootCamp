# ---------------------------------------------------------
# -- Object Oriented Programming => Multiple Inheritance --
# ---------------------------------------------------------
"""
Multiple Inheritance is a concept in Object-Oriented Programming where a class can inherit characteristics and behaviors from more than one parent class.

This means that a child class can have attributes and methods from multiple classes, making it more versatile and flexible in its functionality.

Multiple Inheritance allows for the creation of complex class structures with many levels of inheritance. It can be useful in situations where there are similar but distinct behaviors and attributes that need to be included in a class.

However, multiple inheritance can also lead to complications and conflicts, such as name collisions or issues with method resolution order. As a result, some programming languages do not support multiple inheritance or provide alternative ways to achieve similar functionality, such as mixins or interfaces.
    
"""

class BaseOne:

  def __init__(self):

    print("Base One")

  def func_one(self):

    print("One")

class BaseTwo:

  def __init__(self):

    print("Base Two")

  def func_two(self):

    print("Two")

class Derived(BaseOne, BaseTwo):

  pass

my_var = Derived()

# print(Derived.mro())

print(my_var.func_one)
print(my_var.func_two)

my_var.func_one()
my_var.func_two()

class Base:

  pass

class DerivedOne(Base):

  pass

class DerivedTwo(DerivedOne):

  pass
"""
In object-oriented programming, setters and getters are methods used to set and retrieve the values of private attributes of a class. They provide an interface to access and modify the internal state of an object while maintaining encapsulation.

The setter method, also known as a mutator method, is used to set the value of a private attribute. It typically takes a parameter representing the new value and updates the attribute accordingly. Setter methods often perform additional validation or processing before assigning the value.

The getter method, also known as an accessor method, is used to retrieve the value of a private attribute. It doesn't take any parameters and returns the current value of the attribute.

By using setters and getters, you can control access to the internal state of an object, enforce validation rules, and ensure proper encapsulation.
"""

# ------------------------------------------------------
# -- Object Oriented Programming => Getters & Setters --
# ------------------------------------------------------

class Member:

  def __init__(self, name):

    self.__name = name  # Private

  def say_hello(self):

    return f"Hello {self.__name}"

  def get_name(self):  # Getter

    return self.__name

  def set_name(self, new_name):

    self.__name = new_name

one = Member("Ahmed")

one._Member__name = "Sayed"
print(one._Member__name)

print(one.get_name())
one.set_name('Abbas')
print(one.get_name())
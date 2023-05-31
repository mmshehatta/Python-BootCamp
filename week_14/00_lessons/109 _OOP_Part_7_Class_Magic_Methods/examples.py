"""
    Class magic methods, also known as dunder methods (short for "double underscore"), are special methods in Python that have double underscores at the beginning and end of their names. These methods are called automatically by Python in response to certain operations or events and are used to define the behavior of the class and its objects. Some common class magic methods include __init__, __str__, __repr__, __add__, __len__, and __call__. Understanding and utilizing class magic methods is a key aspect of object-oriented programming in Python and allows you to define custom behavior for your classes and objects.
    
"""

# Some exammples : 
"""
__init__: This magic method is used to initialize an instance of the class. It is called automatically when an object of the class is created, and is used to set up the initial state of the object.

__str__: This magic method is used to define a string representation of an object. It is called when the built-in str() function is applied to an object of the class.

__repr__: This magic method is used to define a string representation of an object that can be used to recreate the object. It is called when the built-in repr() function is applied to an object of the class.

__len__: This magic method is used to define the length of an object. It is called when the built-in len() function is applied to an object of the class.

__add__: This magic method is used to define the addition operation for an object. It is called when the + operator is used with objects of the class.

__eq__: This magic method is used to define equality comparison for an object. It is called when the == operator is used to compare two objects of the class.

These are just a few examples of class magic methods in Python, there are many more. These methods allow you to customize the behavior of your classes and make them behave like built-in types.
"""

"""
The __str__ magic method: This method is used to define the string representation of an object. It is called when the built-in str function is used on an instance of a class. The __str__ method should return a string that describes the object.
Example:1
"""
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    def __str__(self):
        return f'{self.make} {self.model}'

my_car = Car('Toyota', 'Camry')
print(str(my_car)) # Toyota Camry


"""The __add__ magic method: This method is used to define the behavior of the + operator when it is used on instances of a class. It is called when the + operator is used on two instances of a class. The __add__ method should return a new instance of the class that represents the result of the addition operation.
Example: 2
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3.x, v3.y) # 4 6

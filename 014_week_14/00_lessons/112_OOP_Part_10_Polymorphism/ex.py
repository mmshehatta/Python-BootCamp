""" 
Sure, here are some examples of polymorphism in Python, starting from easier to more complex:
ex1:
----
Polymorphic functions: Functions in Python are polymorphic by default. This means that they can accept arguments of different types and perform different actions based on the type of the input. For example:
"""
import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Circle:
    def __init__(self, radius):
        self.radius = radius

def calculate_area(shape):
    if isinstance(shape, Rectangle):
        return shape.width * shape.height
    elif isinstance(shape, Circle):
        return math.pi * (shape.radius ** 2)

# Create a rectangle with width=4 and height=5
rectangle = Rectangle(4, 5)
# Calculate its area using the calculate_area() function
rectangle_area = calculate_area(rectangle)
# Expected result: 20
print(rectangle_area)

# Create a circle with radius=2
circle = Circle(2)
# Calculate its area using the calculate_area() function
circle_area = calculate_area(circle)
# Expected result: approximately 12.57
print(round(circle_area, 2))


""" 
ex2:
---
Polymorphic methods: In Python, methods can also be polymorphic, meaning that they can be implemented differently in different classes. For example:

Here, both Dog and Cat classes inherit from the Animal class and have their own implementation of the speak() method. This allows us to call the same method on different objects and get different behavior based on the object's type.
"""
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
cat = Cat()
print(dog.speak())  # Output: "Woof!"
print(cat.speak())  # Output: "Meow!"


""" 
ex3:
----
Polymorphic operators: Python also supports operator overloading, which allows us to define how operators behave for different types of objects. For example:

Here, we have defined how the + and * operators behave for instances of the Vector class. This allows us to use these operators on Vector objects and get the expected behavior.

In the given code, the polymorphism is demonstrated through the use of operator overloading methods __add__ and __mul__ in the Vector class. These methods allow instances of the Vector class to be added together using the + operator and multiplied by a scalar using the * operator.

The __add__ method enables the addition of two Vector objects, by defining the behavior of the + operator when applied to Vector instances. Similarly, the __mul__ method enables the multiplication of a Vector object with a scalar, by defining the behavior of the * operator when applied to a Vector instance and a scalar value.

This is an example of operator overloading, which is a form of polymorphism in Python that allows operators to behave differently depending on the data types of their operands.
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
v4 = v1 * 2

print(f"v3 = ({v3.x}, {v3.y})")  # expected output: v3 = (6, 8)
print(f"v4 = ({v4.x}, {v4.y})")  # expected output: v4 = (4, 6)


""" 
ex4:
---
Polymorphic interfaces: Finally, in Python, we can use abstract base classes to define interfaces that multiple classes can implement in their own way. For example:

Here, we have defined an abstract base class Shape that defines an interface for computing the area of a shape. Both Rectangle and Circle classes implement this interface in their own way. This allows us to treat objects of different classes that implement the Shape interface polymorphically.

NOTE:
In Python, an abstract method is defined using the @abstractmethod decorator and the pass keyword is used as a placeholder for the method body. The reason for using pass instead of NotImplementedError is that the latter is a runtime error that is raised when the method is called, indicating that the implementation is missing. On the other hand, pass indicates that the method has no implementation and serves as a placeholder to be overridden by the subclass. This allows the subclass to define its own implementation of the abstract method without being required to catch and handle the runtime error that would be raised if NotImplementedError were used. Additionally, using pass also makes it clear to other developers that the method is intended to be overridden and implemented in the subclass.
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

rectangle = Rectangle(4, 5)
rectangle_area = rectangle.area()
print(f"The area of the rectangle is: {rectangle_area}") # The area of the rectangle is: 20

circle = Circle(3)
circle_area = circle.area()
print(f"The area of the circle is: {circle_area}") # The area of the circle is: 28.274333882308138

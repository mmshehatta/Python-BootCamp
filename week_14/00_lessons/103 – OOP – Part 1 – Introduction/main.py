# ------------------------------------------
# -- Object Oriented Programming => Intro --
# ------------------------------------------
# [1] Python Support Object Oriented Programming
# [2] OOP Is A Paradigm Or Coding Style
#     OOP Paradigm =>
#       Means Structuring Program So The Methods[Functions] and Attributes[Data]
#       Are Bundled Into Objects
# [3] Methods => Act As Function That Use The Information Of The Object
# [4] Python Is Multi-Paradigm Programming Language [Procedural, OOP, Functional]
#     - Procedural => Structure App Like Recipe, Sets Of Steps To Make The Task
#     - Functional => Built On the Concept of Mathematical Functions
# [5] OOP Allow You To Organize Your Code and Make It Readable and Reusable
# [6] Everything in Python is Object
# [7] If Man Is Object
#     - Attributes => Name, Age, Address, Phone Number, Info [Can Be Differnet]
#     - Methods[Behaviors] => Walking, Eating, Singing, Playing
# [8] If Car Is Object
#     - Attributes => Model, Colour, Price
#     - Methods[Behaviors] => Walking, Stopping
# [9] Class Is The Template For Creating Objects [Object Constructor | Blueprint]
#     - Class Car Can Create Many Cars Object
# ---------------------------------------------

"""
In more detail, OOP in Python can be implemented by creating classes and objects. A class is a template or blueprint for creating objects, and it defines the properties and methods that the objects will have.

For example, you can create a class called "Car" that has properties like "make", "model", and "year", and methods like "start_engine" and "stop_engine". Then, you can create multiple objects of the class "Car" and give them specific values for the properties, such as "make" = "Toyota", "model" = "Camry", "year" = 2020.

Python classes are defined using the "class" keyword, followed by the name of the class. The properties and methods of the class are defined within the class using the "self" keyword, which refers to the current instance of the class.

For example:
"""


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print("Engine started.")

    def stop_engine(self):
        print("Engine stopped.")


"""
Inheritance is another important concept in OOP, it allows a class to inherit properties and methods from a parent class. This can be useful for creating a new class that is similar to an existing class, but with some additional or modified functionality. In python, classes can inherit from other classes using the parent class name in the parentheses after the child class name during the class definition.

For example:
"""

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 100


"""
In this example, ElectricCar class is inheriting all properties and methods from the Car class and in addition, it has a new property "battery_size".

Polymorphism is another OOP concept that allows objects of different classes to be used interchangeably. This can be achieved through inheritance, as well as through the use of interfaces and abstract classes.

Python uses the "duck-typing" approach for polymorphism, which means that an object's behavior is determined by its methods and properties, rather than its class. For example, if an object has a method called "quack", it can be considered a "duck", regardless of its actual class.

Overall, OOP in Python provides a powerful way to organize and structure code, making it more modular and easier to understand and maintain. It also allows for code reusability and encapsulation, which helps to protect the internal state of objects from external interference.
"""
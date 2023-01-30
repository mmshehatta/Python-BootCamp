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


"""The Lesson In Q and A"""
"""
Q: What is Python's support for object-oriented programming?
A: Python supports object-oriented programming.

Q: What is OOP and how is it different from other paradigms or coding styles?
A: OOP is a paradigm or coding style in which methods and attributes are bundled into objects. It is different from other paradigms such as procedural or functional, which structure programs in different ways.

Q: What are methods in OOP?
A: Methods in OOP act as functions that use the information of the object.

Q: Is Python a multi-paradigm programming language?
A: Yes, Python is a multi-paradigm programming language, supporting the paradigms of procedural, OOP, and functional.

Q: How does OOP help in organizing and making code readable and reusable?
A: OOP allows for organizing code by bundling methods and attributes into objects, making it more readable and reusable.

Q: Is everything in Python an object?
A: Yes, everything in Python is an object.

Q: Can you give an example of an object and its attributes and methods?
A: One example of an object is a "man," which may have attributes such as name, age, address, phone number, and additional information. Its methods, or behaviors, may include walking, eating, singing, and playing.

Q: Can you give another example of an object and its attributes and methods?
A: Another example of an object is a "car," which may have attributes such as model, color, and price. Its methods, or behaviors, may include starting and stopping.

Q: What is a class in OOP?
A: A class in OOP is a template or blueprint for creating objects. It is the object constructor and can be used to create multiple objects of the same type.

Q: How can a class be used to create multiple objects?
A: A class can be used to create multiple objects by utilizing the object constructor. For example, a class "Car" can be used to create multiple "Car" objects.
"""

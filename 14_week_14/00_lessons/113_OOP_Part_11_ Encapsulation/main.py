"""
In object-oriented programming, encapsulation refers to the concept of bundling data and methods within a class and controlling access to them. It is a way of organizing code and data together as a single unit, where the internal details of the implementation are hidden from the outside world.

Encapsulation provides several benefits:

1.Data Protection: Encapsulation allows data to be hidden from direct access outside the class. The internal state of an object can be protected and accessed only through defined methods, ensuring data integrity and preventing unauthorized modifications.

2.Abstraction: Encapsulation helps in creating abstractions by exposing only the necessary information to the outside world. It allows you to define a clear interface or API for interacting with objects, hiding the complex implementation details.

3.Code Modularity: Encapsulation enables code modularity by grouping related data and methods together in a class. This improves code organization, readability, and maintainability, as changes to the internal implementation of a class do not impact the external code that uses it.

4.Code Reusability: Encapsulated classes can be easily reused in different parts of an application. Since the implementation details are hidden, the same class can be used in different contexts without affecting its functionality.

To achieve encapsulation, the following principles are often applied:

1.Access Modifiers: In many object-oriented languages, access modifiers such as public, private, and protected are used to control the visibility of class members (variables and methods). Private members are only accessible within the class, while public members can be accessed from outside the class.

2.Getters and Setters: Encapsulation involves providing getter and setter methods to access and modify the internal state of an object. These methods allow controlled access to the private data members, enabling data validation and ensuring consistent access patterns.

3.Information Hiding: Encapsulation promotes the idea of information hiding, where the internal implementation details are hidden from the outside world. This prevents direct access to internal data and forces the use of defined methods to interact with the object.

Overall, encapsulation helps in achieving better code organization, data protection, and code reuse, leading to more maintainable and robust software systems.

# --------------------------------------------------
# -- Object Oriented Programming => Encapsulation --
# --------------------------------------------------
# Encapsulation
# - Restrict Access To The Data Stored in Attirbutes and Methods
# Public
# - Every Attribute and Method That We Used So Far Is Public
# - Attributes and Methods Can Be Modified and Run From Everywhere
# - Inside Our Outside The Class
# Protected
# - Attributes and Methods Can Be Accessed From Within The Class And Sub Classes
# - Attributes and Methods Prefixed With One Underscore _
# Private
# - Attributes and Methods Can Be Accessed From Within The Class Or Object Only
# - Attributes Cannot Be Modified From Outside The Class
# - Attributes and Methods Prefixed With Two Underscores __
# ---------------------------------------------------------
# - Attributes = Variables = Properties
# -------------------------------------


"""

class Member:

  def __init__(self, name):

    self.name = name  # Public

one = Member("Ahmed")
print(one.name)
one.name = "Sayed"
print(one.name)

class Member:

  def __init__(self, name):

    self._name = name  # Protected

one = Member("Ahmed")
print(one._name)
one._name = "Sayed"
print(one._name)

class Member:

  def __init__(self, name):

    self.__name = name  # Private

  def say_hello(self):

    return f"Hello {self.__name}"

one = Member("Ahmed")
# print(one.__name)
print(one.say_hello())
print(one._Member__name)

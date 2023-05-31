""" 
Polymorphism is one of the fundamental concepts of object-oriented programming (OOP). It refers to the ability of objects to take on different forms and behave differently in different contexts. In Python, polymorphism allows us to use a single interface to represent different types of objects.

There are two types of polymorphism in Python: compile-time polymorphism and run-time polymorphism.

Compile-time polymorphism is also known as method overloading. It allows us to define multiple methods with the same name but with different arguments or parameter types. Python does not support method overloading directly, but we can simulate it by using default arguments or variable-length argument lists.

Run-time polymorphism is also known as method overriding. It allows us to define a method in a subclass that overrides a method with the same name in the superclass. When we call the method on an object of the subclass, the overridden method is called instead of the original method in the superclass.

Polymorphism is a powerful tool that allows us to write more flexible and reusable code. By designing our classes to support polymorphism, we can write code that can work with different types of objects without having to know their specific type in advance.

In Python, there are two types of polymorphism:
--
1)Runtime Polymorphism (Dynamic Binding): This type of polymorphism is achieved during runtime, where the actual method called is resolved at runtime. This can be achieved through method overriding or method overloading.

2)Compile-time Polymorphism (Static Binding): This type of polymorphism is achieved during compilation, where the actual method called is resolved at compile time. This can be achieved through function overloading, where multiple functions with the same name are defined but with different parameter types or parameter count. However, Python does not support function overloading in the traditional sense, so this type of polymorphism is not used as often in Python.
"""

# -------------------------------------------------
# -- Object Oriented Programming => Polymorphism --
# -------------------------------------------------

n1 = 10
n2 = 20

print(n1 + n2)

s1 = "Hello"
s2 = "Python"

print(s1 + " " + s2)

print(len([1, 2, 3, 4, 5, 6]))
print(len("Osama Elzero"))
print(len({"Key_One": 1, "Key_Two": 2}))

class A:

  def do_something(self):

    print("From Class A")

    raise NotImplementedError("Derived Class Must Implement This Method")

class B(A):

  def do_something(self):

    print("From Class B")

class C(A):

  def do_something(self):

    print("From Class C")

my_instance = B()
my_instance.do_something()
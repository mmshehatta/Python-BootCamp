import math
# Give my a speed task about this info , to test my knowledge ?
"""
Sure, here is a speed task to test your knowledge about instance attributes and methods in object-oriented programming:
"""
# 1. Given the following code:


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self, sound):
        print(f"{self.name} barks {sound}")


dog1 = Dog("Max", "Labrador")
dog2 = Dog("Rocky", "Bulldog")

#########
# Q{1}:
"""What does "self" represent in the class Dog?
What are the instance attributes of the dog1 and dog2 objects?
Can the bark method access the instance attributes of the object it is called on?
"""
# A:
"""
. "Self" in the class Dog represents the instance created from the class.
. The instance attributes of the dog1 object are name = "Max" and breed = "Labrador". The instance attributes of the  dog2 object are name = "Rocky" and breed = "Bulldog".
. Yes, the bark method can access the instance attributes of the object it is called on
."""

# 2.Given the following code:


class Car:
    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def honk(self):
        print(f"{self.make} {self.model} says honk!")


car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

#########
# Q{2}:
"""
What is the value of the wheels attribute for the car1 and car2 objects?
Can the honk method access the wheels attribute?
Can the honk method access the make and model attributes of the object it is called on?
"""

# A:
"""
. The value of the wheels attribute for the car1 and car2 objects is 4.
. Yes, the honk method can access the wheels attribute.
. Yes, the honk method can access the make and model attributes of the object it is called on.
"""

#########
# Q{3}:

"""
Sure, here is a code task related to instance attributes and methods in object-oriented programming:

Problem: Create a class Person with instance attributes name and age, and two instance methods:

introduce() which prints a string introducing the person, including their name and age.
birthday() which increases the person's age by 1.
Here is an example of how the class should be used:
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

    def birthday(self):
        self.age += 1
        return self.age


person1 = Person("John Doe", 30)
person2 = Person("Jane Doe", 25)

person1.introduce()  # "Hi, my name is John Doe and I am 30 years old."
person2.introduce()  # "Hi, my name is Jane Doe and I am 25 years old."

person1.birthday()
person1.introduce()  # "Hi, my name is John Doe and I am 31 years old."


#########
# Q{4}:This task is at an intermediate to advanced level
"""
- Can you give my more difficult one?
Sure, here is a more advanced code task related to object-oriented programming:

Problem: Create a class BankAccount with instance attributes balance, and three instance methods:

deposit(amount) which adds amount to the account's balance.
withdraw(amount) which subtracts amount from the account's balance, and raises a ValueError if the withdrawal amount is greater than the balance.
check_balance() which returns the account's balance.
Here is an example of how the class should be used:
"""


class BankAccount:
    def __init__(self, balance: float):
        self.balance = balance

    def check_balance(self) -> float:
        return self.balance

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise ValueError(
                "the withdrawal amount is greater than the balance")
        self.balance -= amount


account = BankAccount(100)

account.deposit(50)
print(account.check_balance())  # 150

account.withdraw(75)
print(account.check_balance())  # 75

try:
    account.withdraw(100)
except ValueError as e:
    print(e)  # "Withdrawal amount is greater than the balance."


#########
# Q{5}: This task is at an advanced level
"""
Problem: Create a class Rectangle with instance attributes width and height, and the following methods:

- area() which returns the area of the rectangle.
- perimeter() which returns the perimeter of the rectangle.
- diagonal() which returns the length of the diagonal of the rectangle.
- is_square() which returns True if the rectangle is a square, and False otherwise.

Additionally, add a class method from_area(area) that takes the area of the rectangle and returns a new instance of the Rectangle class with width and height calculated such that the area of the rectangle is equal to area.


"""
# Here is an example of how the class should be used:

class Rectangle:
    
    def __init__(self, width: float, height:float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
       return self.width * self.height

    def perimeter(self) -> float:
        return (self.width + self.height) * 2

    def diagonal(self) -> float:
        """The diagonal function calculates the length of the diagonal of the rectangle by using the Pythagorean theorem. It takes the square root of the sum of the squares of the width and height attributes.
        """
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def is_square(self) -> bool:
        if self.width == self.height:
            return True
        return False 
    @classmethod
    def from_area(cls, area):
        width = math.sqrt(area)
        height = area / width
        return cls(width, height)



rect = Rectangle(10, 5)

print(rect.area()) # 50
print(rect.perimeter()) # 30
print(rect.diagonal()) # 11.180339887498949
print(rect.is_square()) # False

sq = Rectangle.from_area(25)
print(sq.width) # 5
print(sq.height) # 5
print(sq.is_square()) # True

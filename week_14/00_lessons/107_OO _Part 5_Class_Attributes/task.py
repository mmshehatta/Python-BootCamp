# example 1:
# =========
class Dog:
    """In this example, species is a class attribute, which is shared by all instances of the class Dog. The value of species can be accessed using the dot (.) operator, either on the class itself or on any instance of the class.
    """
    species = 'mammal'
    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog1 = Dog("Rocky", "Labrador")
dog2 = Dog("Buddy", "Golden Retriever")

print(dog1.species) # Output: mammal
print(dog2.species) # Output: mammal
print(Dog.species) # Output: mammal

# example 2:
# =========
class Car:
    """    
    In this example, the class Car has a class attribute wheels, which is set to 4. This attribute is shared by all instances of the class, and can be accessed using the dot (.) operator, either on the class itself or on any instance of the class. The value of wheels will be the same for all instances, since it is a class attribute and not an instance attribute.
    """
    wheels = 4
    
    def __init__(self, make, model):
        self.make = make
        self.model = model

car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

print(Car.wheels) # Output: 4
print(car1.wheels) # Output: 4
print(car2.wheels) # Output: 4


# example 3:
# =========
class Circle:
    """
    In this example, the class Circle has a class attribute pi which is set to the value of π. This value is used in the method area to calculate the area of a circle, given its radius. The method area can be called on any instance of the class Circle, and the value of π will always be the same, since it is a class attribute.
    This example demonstrates how class attributes can be used to store values that are shared by all instances of a class and can be used in methods to perform calculations.
    """
    pi = 3.14159265
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return Circle.pi * (self.radius ** 2)

circle1 = Circle(5)
circle2 = Circle(10)

print(Circle.pi) # Output: 3.14159265
print(circle1.area()) # Output: 78.53975
print(circle2.area()) # Output: 314.159265


# example 4:
# =========
class BankAccount:
    """In this example, the class BankAccount has a class attribute interest_rate, which is set to 1.03. This value is used in the method apply_interest to calculate the new balance after interest has been applied.
    This example demonstrates how class attributes can be used to store values that are shared by all instances of a class and can be used in methods to perform calculations. It also shows how methods can be used to modify instance attributes and how methods can interact with each other.
    """
    interest_rate = 1.03
    
    def __init__(self, balance):
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        self.balance -= amount
        
    def apply_interest(self):
        self.balance *= BankAccount.interest_rate

account1 = BankAccount(1000)
account2 = BankAccount(2000)

print("Initial balance:", account1.balance) # Output: Initial balance: 1000
print("Initial balance:", account2.balance) # Output: Initial balance: 2000

account1.deposit(500)
account2.withdraw(500)

print("Balance after deposit:", account1.balance) # Output: Balance after deposit: 1500
print("Balance after withdraw:", account2.balance) # Output: Balance after withdraw: 1500

account1.apply_interest()
account2.apply_interest()

print("Balance after interest:", account1.balance) # Output: Balance after interest: 1545.0
print("Balance after interest:", account2.balance) # Output: Balance after interest: 1545.0

# example 5:
# =========

class Employee:
    """
    In this example, the class Employee has two class attributes: raise_amount and num_of_emps. The raise_amount attribute is used in the method apply_raise to calculate the new pay for an employee after a raise has been applied. The num_of_emps attribute is used to keep track of the number of employees that have been created.

    This example demonstrates how class attributes can be used to store values that are shared by all instances of a class and how they can be used in methods to perform calculations. It also shows how class attributes can be accessed and modified directly, as well as through instances of the class.
    """
    raise_amount = 1.05
    num_of_emps = 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        Employee.num_of_emps += 1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

emp1 = Employee('John', 'Doe', 50000)
emp2 = Employee('Jane', 'Doe', 60000)

print(Employee.num_of_emps) # Output: 2

print(emp1.pay) # Output: 50000
emp1.apply_raise()
print(emp1.pay) # Output: 52500

print(Employee.raise_amount) # Output: 1.05
Employee.raise_amount = 1.10
print(Employee.raise_amount) # Output: 1.1

emp2.apply_raise()
print(emp2.pay) # Output: 66000


# example 6:
# =========
class Animal:
    """This example demonstrates inheritance and polymorphism by defining a base class Animal and two subclasses Dog and Cat that inherit from it. The Animal class has a class attribute num_of_animals that is used to keep track of the number of animal instances created.

    The Animal class also defines an abstract method make_sound that raises a NotImplementedError exception. This method must be implemented by subclasses in order to provide a unique implementation for each type of animal.

    The Dog and Cat classes each provide their own implementation of the make_sound method, as well as their own __str__ method to provide a custom string representation for instances of those classes.

    This example demonstrates how class attributes can be used to keep track of information about the class hierarchy, how inheritance can be used to create a hierarchy of classes, and how polymorphism can be used to provide unique implementations for each type of object in the hierarchy.
    """
    num_of_animals = 0
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        Animal.num_of_animals += 1
        
    def __str__(self):
        return '{} is a {}'.format(self.name, self.species)
        
    def make_sound(self):
        raise NotImplementedError("Subclass must implement this abstract method")
        
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def __str__(self):
        return '{} is a {} {}'.format(self.name, self.breed, self.species)
        
    def make_sound(self):
        return 'Woof!'
        
class Cat(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Cat")
        self.breed = breed
        
    def __str__(self):
        return '{} is a {} {}'.format(self.name, self.breed, self.species)
        
    def make_sound(self):
        return 'Meow!'

dog = Dog('Rufus', 'Labrador')
cat = Cat('Fluffy', 'Persian')

print(dog) # Output: Rufus is a Labrador Dog
print(cat) # Output: Fluffy is a Persian Cat

print(dog.make_sound()) # Output: Woof!
print(cat.make_sound()) # Output: Meow!

print(Animal.num_of_animals) # Output: 2


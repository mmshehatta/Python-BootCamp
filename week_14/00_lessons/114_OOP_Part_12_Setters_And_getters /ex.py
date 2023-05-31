""" 
Ex1:
In this example, the Person class has private attributes _name and _age. The class provides getters (get_name and get_age) and setters (set_name and set_age) for these attributes. The getters allow retrieving the values, and the setters allow updating the values with certain validation rules.

Using setters and getters allows controlled access to the attributes, as you can enforce rules and validations within the methods. This helps in maintaining the integrity and consistency of the object's state.
"""
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Getter for name attribute
    def get_name(self):
        return self._name

    # Setter for name attribute
    def set_name(self, name):
        self._name = name

    # Getter for age attribute
    def get_age(self):
        return self._age

    # Setter for age attribute
    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            raise ValueError("Age must be a non-negative value")

# Usage
person = Person("John", 25)

print(person.get_name())  # Output: John
print(person.get_age())   # Output: 25

person.set_name("Alice")
person.set_age(30)

print(person.get_name())  # Output: Alice
print(person.get_age())   # Output: 30


""" 
Ex2:
"""

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_width(self):
        return self._width

    def set_width(self, width):
        if width > 0:
            self._width = width
        else:
            raise ValueError("Width must be a positive value")

    def get_height(self):
        return self._height

    def set_height(self, height):
        if height > 0:
            self._height = height
        else:
            raise ValueError("Height must be a positive value")

    def get_area(self):
        return self._width * self._height

# Usage
rectangle = Rectangle(5, 3)

print(rectangle.get_width())   # Output: 5
print(rectangle.get_height())  # Output: 3
print(rectangle.get_area())    # Output: 15

rectangle.set_width(8)
rectangle.set_height(4)

print(rectangle.get_width())   # Output: 8
print(rectangle.get_height())  # Output: 4
print(rectangle.get_area())    # Output: 32


""" 
Ex3: BankAccount Class
"""
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Amount must be a positive value")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            raise ValueError("Insufficient balance")

# Usage
account = BankAccount("1234567890", 1000)

print(account.get_account_number())  # Output: 1234567890
print(account.get_balance())         # Output: 1000

account.deposit(500)
print(account.get_balance())         # Output: 1500

account.withdraw(800)
print(account.get_balance())         # Output: 700


""" 
Ex4: Employee Class
"""
class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def get_name(self):
        return self._name

    def get_salary(self):
        return self._salary

    def set_salary(self, salary):
        if salary >= 0:
            self._salary = salary
        else:
            raise ValueError("Salary must be a non-negative value")

# Usage
employee = Employee("John Doe", 5000)

print(employee.get_name())    # Output: John Doe
print(employee.get_salary())  # Output: 5000

employee.set_salary(6000)
print(employee.get_salary())  # Output: 6000


"""   
In each of these examples, the classes have private attributes and corresponding getters and setters to access and modify those attributes. The getters allow retrieving the values, while the setters allow updating the values with certain validation rules.

These examples demonstrate how encapsulation is achieved by providing controlled access to the internal state of an object through getters and setters.

"""





# Class Methods::
# ==========================

"""
example 1: 
============
Easy: Define a class method that returns the number of instances of the class that have been created:
"""
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1
    
    @classmethod
    def num_instances(cls):
        return cls.count
print(Counter.num_instances()) # Output: 0
c1 = Counter()                
print(Counter.num_instances()) # Output: 1


"""
example 2: 
============
Medium: Define a class method that takes a string and returns a new instance of the class, initialized with the values provided in the string:
"""
class Employee:
    def __init__(self, name, id_number, department):
        self.name = name
        self.id_number = id_number
        self.department = department
    
    @classmethod
    def from_string(cls, emp_str):
        name, id_number, department = emp_str.split(',')
        return cls(name, id_number, department)

print(Employee.from_string("Mahmoud,50,IT").name) # Output: Mahmoud



"""
example 3: 
============
Hard: Define a class method that returns the median salary of all instances of the class:

HINT >>:The median salary is the middle value of a set of numbers. In this case, the set of    numbers is the salaries of all instances of the class Employee. If the number of salaries is odd, the median is the middle value. If the number of salaries is even, the median is the average of the two middle values.

For example, if there are 5 employees with salaries [10, 20, 30, 40, 50], the median salary is 30. If there are 6 employees with salaries [10, 20, 30, 40, 50, 60], the median salary is (30 + 40) / 2 = 35.

Computing the median salary of all employees using a class method allows us to get a summary of the salary distribution of all employees, which can be useful information for business purposes.
"""

class Employee:
    employee_list = []
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_list.append(self)    
    
    @classmethod
    def median_salary(cls):
        n = len(cls.employee_list)
        s = sorted([emp.salary for emp in cls.employee_list])
        return (s[n//2-1] + s[n//2])/2 if n % 2 == 0 else s[n//2]

# Create instances of the Employee class
employee_one = Employee("John Doe", 5000)
employee_two = Employee("Jane Doe", 6000)
employee_three = Employee("Jim Smith", 7000)
employee_four = Employee("Emily Johnson", 8000)


# Call the median_salary class method
median = Employee.median_salary()

# Print the median salary
print("Median salary:", median) # Output: Median salary: 6500.0





# Static Methods::
# ==========================
"""Static methods are best used for utility functions that don't rely on instance-specific data. They are functions that are associated with a class rather than an instance of the class. Some common use cases for static methods include:

Creating utility functions that perform a calculation based solely on the arguments passed to the method and do not reference any class or instance data.

Creating methods that are relevant to the class as a whole, rather than to any specific instance of the class. For example, a method to create a random number based on a class-level seed value.

Implementing alternative constructors for a class, for example, by providing static methods that return instances of the class, but with different data.

Grouping related utility functions under a single class, which makes the code easier to understand and maintain.

In summary, static methods are best used for functions that don't modify class-level data, and don't depend on instance-level data."""


"""
example 1: 
Creating utility functions that perform a calculation based solely on the arguments passed to the method and do not reference any class or instance data:
============
"""
class Math:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b

result = Math.add(5, 3) # 8

"""
example 2: 
Creating methods that are relevant to the class as a whole, rather than to any specific instance of the class:
"""
import random

class RandomNumberGenerator:
    seed = 42
    
    @staticmethod
    def generate_random_number():
        return random.randint(0, RandomNumberGenerator.seed)

random_number = RandomNumberGenerator.generate_random_number()
print(random_number)

"""
example 3: 
Implementing alternative constructors for a class:
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, 2021 - birth_year)

person = Person.from_birth_year("John", 1990)
print(person) # Output: 


"""
example 4: 
Grouping related utility functions under a single class
"""
class StringUtils:
    @staticmethod
    def is_palindrome(word):
        return word == word[::-1]
    
    @staticmethod
    def to_lowercase(word):
        return word.lower()

is_palindrome = StringUtils.is_palindrome("Madam") # True
lowercase = StringUtils.to_lowercase("HELLO") # "hello"

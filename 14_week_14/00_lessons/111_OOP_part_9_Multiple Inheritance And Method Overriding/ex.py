""" 
ex1 : 
Create a class Vehicle with methods start() and stop(). Create another class Airplane with a method fly(). Then, create a class AirplaneVehicle that inherits from both Vehicle and Airplane and has a method takeoff().
"""
class Vechile:
    def start(self):
        print("Sarting...")
    def stop(self):
        print("Stoping...")
        
class Airplane:
    def fly(self):
        print("Flying...")
        
class AirplaneVechile(Vechile , Airplane):
    def takeoff(self):
        print("takeingoff....")
        

av = AirplaneVechile()
av.start()
av.stop()
av.fly()
av.takeoff()


""" 
ex2:
Create a class Person with a method introduce() that prints the person's name and age. Create another class Employee with a method work() that prints "I am working". Then, create a class EmployeePerson that inherits from both Person and Employee and has a method do_work() that calls both introduce() and work().
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def introduce(self):
        print(f"I am {self.name} , my age is {self.age}")

class Employee:
    def work(self):
        print("I am Working...")
        

class EmploeePerson(Person, Employee):
    def __init__(self, name, age):
        super().__init__(name, age)
    def do_work(self):
        self.introduce()
        self.work()
    
ep = EmploeePerson("Mahmoud", 27)  
ep.do_work()      


""" 
ex3:
Create a class Shape with methods area() and perimeter(). Create another class Color with a method colorize() that prints the color of the object. Then, create a class ColoredShape that inherits from both Shape and Color and has a method display() that calls both area() and colorize().
"""
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Color:
    def __init__(self, color):
        self.color = color

    def colorize(self):
        print(f"Color: {self.color}")


class ColoredShape(Shape, Color):
    def __init__(self, color):
        Shape.__init__(self)
        Color.__init__(self, color)

    def display(self):
        self.area()
        self.colorize()

# Test Data 
s1 = Shape()
c1 = Color("Red")
# cs1 = ColoredShape(s1, c1)
# Expected output of cs1.display(): "Area: 100, Color: Red"


""" 
ex4:
Create a class Database with methods connect() and query(). Create another class Cache with a method store() that stores data in cache. Then, create a class CachingDatabase that inherits from both Database and Cache and has a method run_query() that calls both query() and store().
"""
class Database:
    def connect(self):
        print("Connecting to database...")

    def query(self, query):
        print(f"Executing query: {query}")


class Cache:
    def store(self, data):
        print(f"Storing data in cache: {data}")


class CachingDatabase(Database, Cache):
    def run_query(self, query, data):
        self.connect()
        result = self.query(query)
        self.store(data)
        print(f"Query result: {result}")

# Test data for Database class
caching_db = CachingDatabase()
result = caching_db.run_query("SELECT * FROM users", {"username": "john.doe"})


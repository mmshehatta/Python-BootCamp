"""
Inheritance :
is a key concept in object-oriented programming that allows you to create a new class that is a modified version of an existing class. The new class is called the derived class, and the existing class is referred to as the base class. The derived class inherits all the attributes and behaviors of the base class and can add new attributes and behaviors or override existing ones.

Inheritance is useful because it allows you to create a new class that is a specialization of an existing class. For example, you might have a base class called "Animal" and a derived class called "Dog". The Dog class would inherit all the attributes and behaviors of the Animal class and could add new attributes and behaviors specific to dogs, such as "bark" or "fetch". This allows you to reuse code from the base class and avoid duplication, making your code more maintainable and easier to understand.

Inheritance also enables you to create a hierarchy of classes, where you can create a base class that is more general and derived classes that

"""
"""
Example:1
(Easy) Create a base class Animal that has a make_sound method. Then create a subclass Dog that inherits from Animal and overrides the make_sound method to return "Bark".
NOTE : 
The __init__ method is not necessary in this example because the base class Animal does not need to initialize any data when creating a new instance. In this simple example, the make_sound method is the only method that is relevant to the Animal class, and it doesn't rely on any instance-specific data.
In more complex examples, you may want to initialize instance data in the __init__ method, but in this case, it's not needed.
"""
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark"

dog = Dog()
print(dog.make_sound()) # Output: Bark


""" 
Example:2
(Easy) Create a base class Person with attributes first_name and last_name. Create a subclass Student that inherits from Person and adds an attribute student_id.
"""
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Student(Person):
    def __init__(self, first_name, last_name, student_id):
        super().__init__(first_name, last_name)
        self.student_id = student_id

# Test data:
student = Student("Jone", "Doe", "123456")
print(student.first_name) # Jone
print(student.last_name)  # Doe
print(student.student_id) # 123456


"""
Example:3
(Medium) Create a base class Shape with a calculate_area method. Create subclasses Rectangle and Circle that inherit from Shape and implement the calculate_area method specific to their shape.
"""
import math

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def calculate_area(self):
        """The best implementation is raise NotImplementedError("calculate_area method is not implemented") as it clearly communicates that the method has not been implemented and should be overridden in a subclass. It also allows the subclass to have a clear error message if they forget to implement it, rather than just silently failing or returning an incorrect result.
        """
        raise NotImplementedError("calculate_area method is not implemented")

class Rectangle(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def calculate_area(self):
        return (self.x + self.y) * 2

class Circle(Shape):
    def __int__(self, radius):
        self.radius = radius        
    
    def claculate_area(self):
        return math.pi * (self.radius ** 2)
    
# Test data
rect = Rectangle(10, 20)
print(rect.calculate_area()) # 200

circle = Circle(5)
print(circle.calculate_area()) # 78.53981633974483


"""
Example:4
(Hard) Create a base class Vehicle with attributes speed and num_of_wheels. Create subclasses Car and Motorcycle that inherit from Vehicle and add an attribute specific to each class (e.g. Car has num_of_doors and Motorcycle has type_of_engine). Override the __str__ method in each subclass to return a string representation of the object that includes all its attributes.
"""
class Vehicle:
    def __init__(self, speed, num_of_wheels):
        self.speed = speed
        self.num_of_wheels = num_of_wheels

    def __str__(self):
        return f"Vehicle with speed: {self.speed} and number of wheels: {self.num_of_wheels}"

class Car(Vehicle):
    def __init__(self, speed, num_of_wheels, num_of_doors):
        super().__init__(speed, num_of_wheels)
        self.num_of_doors = num_of_doors

    def __str__(self):
        return f"Car with speed: {self.speed}, number of wheels: {self.num_of_wheels}, and number of doors: {self.num_of_doors}"

class Motorcycle(Vehicle):
    def __init__(self, speed, num_of_wheels, type_of_engine):
        super().__init__(speed, num_of_wheels)
        self.type_of_engine = type_of_engine

    def __str__(self):
        return f"Motorcycle with speed: {self.speed}, number of wheels: {self.num_of_wheels}, and type of engine: {self.type_of_engine}"

# Test data
car = Car(100, 4, 4)
motorcycle = Motorcycle(120, 2, "V-Twin")

# Printing the objects
print(car)        # Car with speed: 100, number of wheels: 4, and number of doors: 4
print(motorcycle) # Motorcycle with speed: 120, number of wheels: 2, and type of engine: V-Twin

""" 
Example:5
(Hard) Create a class hierarchy for a simple game where there are Enemies that have different types (e.g. Zombie, Vampire, Werewolf). The base class Enemy has an attribute hit_points and a method take_damage that reduces the hit_points by a given amount. Each subclass should override the method to implement its own behavior (e.g. Zombies take double damage, Vampires have a chance to dodge the damage, Werewolves have regenerating hit points).
"""
class Enemy:
    def __init__(self, hit_points):
        self.hit_points = hit_points
        
    def take_damage(self, damage):
        self.hit_points -= damage
        
    def __str__(self):
        return f"Enemy with {self.hit_points} hit points"

class Zombie(Enemy):
    def take_damage(self, damage):
        self.hit_points -= 2 * damage
        
    def __str__(self):
        return f"Zombie with {self.hit_points} hit points"

class Vampire(Enemy):
    def take_damage(self, damage):
        import random
        if random.random() > 0.5:
            print("Vampire dodged the damage")
        else:
            self.hit_points -= damage
        
    def __str__(self):
        return f"Vampire with {self.hit_points} hit points"

class Werewolf(Enemy):
    def take_damage(self, damage):
        self.hit_points -= damage
        if self.hit_points < 0:
            self.hit_points = 0
        self.hit_points += 1
        
    def __str__(self):
        return f"Werewolf with {self.hit_points} hit points"

# Example usage:
zombie = Zombie(100)
zombie.take_damage(10)
print(zombie) # Zombie with 80 hit points

vampire = Vampire(100)
vampire.take_damage(10)
print(vampire) # Vampire with 90 or 100 hit points

werewolf = Werewolf(100)
werewolf.take_damage(110)
print(werewolf) # Werewolf with 1 hit points

# ----------------------------------------------------------
# -- Object Oriented Programming => Class Syntax and Info --
# ----------------------------------------------------------
# [01] Class is The Blueprint Or Construtor Of The Object
# [02] Class Instantiate Means Create Instance of A Class
# [03] Instance => Object Created From Class And Have Their Methods and Attributes
# [04] Class Defined With Keyword class
# [05] Class Name Written With PascalCase [UpperCamelCase] Style
# [06] Class May Contains Methods and Attributes
# [07] When Creating Object Python Look For The Built In __init__ Method
# [08] __init__ Method Called Every Time You Create Object From Class
# [09] __init__ Method Is Initialize The Data For The Object
# [10] Any Method With Two Underscore in The Start and End Called Dunder or Magic Method
# [11] self Refer To The Current Instance Created From The Class And Must Be First Param
# [12] self Can Be Named Anything
# [13] In Python You Dont Need To Call new() Keyword To Create Object
# -------------------------------------------------------------------

# Syntax
# class Name:
#     Constructor => Do Instantiation [ Create Instance From A Class ]
#     Each Instance Is Separate Object
#     def __init__(self, other_data)
#         Body Of Function


class Member:

  def __init__(self):

    print("A New Member Has Been Added")

member_one = Member()
member_two = Member()
member_three = Member()

print(member_one.__class__)

my_dictionary = {
  'name': "Osama",
  'age': 36,
  'monthly_salary': 5000,
  'yearly_salary': ''  # Something
}


"""Lessson in Q & A"""
"""
What is the purpose of a class in OOP?
Answer: A class is the blueprint or constructor of an object.

What does it mean to instantiate a class?
Answer: Instantiation means creating an instance of a class.

What is an instance in OOP?
Answer: An instance is an object created from a class, which has its own methods and attributes.

What keyword is used to define a class in Python?
Answer: The keyword "class" is used to define a class in Python.

What is the naming convention for a class in Python?
Answer: In Python, class names are written in PascalCase or UpperCamelCase style.

What can a class contain in OOP?
Answer: A class may contain methods and attributes.

What method does Python look for when creating an object from a class?
Answer: When creating an object from a class, Python looks for the built-in init method.

What is the purpose of the init method?
Answer: The init method is called every time an object is created from a class and it is used to initialize the data for the object.

What are "dunder" or "magic" methods in Python?
Answer: In Python, methods with two underscores at the start and end are called dunder or magic methods.

What does the self keyword refer to in a class method?
Answer: The self keyword refers to the current instance created from the class, and it must be the first parameter in a class method.

Can the self keyword be named something else?
Answer: Yes, the self keyword can be named anything, but it is conventionally named self.

Is the new() keyword required to create an object in Python?
Answer: No, in Python, you do not need to call the new() keyword to create an object.
"""
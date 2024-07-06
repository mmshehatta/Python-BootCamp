# --------------------------------------------------------------------
# -- Object Oriented Programming => Instance Attributes and Methods --
# --------------------------------------------------------------------
# Self: Point To Instance Created From Class
# Instance Attributes: Instance Attributes Defined Inside The Constructor
# -----------------------------------------------------------------------
# Instance Methods: Take Self Parameter Which Point To Instance Created From Class
# Instance Methods Can Have More Than One Parameter Like Any Function
# Instance Methods Can Freely Access Attributes And Methods On The Same Object
# Instance Methods Can Access The Class Itself
# -----------------------------------------------------------

class Member:
  def __init__(self, first_name, middle_name, last_name):
    self.fname = first_name
    self.mname = middle_name
    self.lname = last_name

member_one = Member("Osama", "Mohamed", "Elsayed")
member_two = Member("Ahmed", "Ali", "Mahmoud")
member_three = Member("Mona", "Ali", "Mahmoud")

# print(dir(member_one))

print(member_one.fname, member_one.mname, member_one.lname)
print(member_two.fname)
print(member_three.fname)


"""Lessson in Q & A"""
""" 
Sure, here is the list in question and answer format:

Q1: What does "self" represent in the context of instance attributes and methods?
A: "Self" represents the instance created from the class.

Q2: What are instance attributes and where are they defined in a class?
A: Instance attributes are attributes defined inside the constructor of a class.

Q3: What is the purpose of the self parameter in instance methods?
A: The self parameter in instance methods points to the instance created from the class.

Q4: Can instance methods have multiple parameters?
A: Yes, instance methods can have multiple parameters just like any other function.

Q5: Can instance methods access attributes and methods on the same object?
A: Yes, instance methods can freely access attributes and methods on the same object.

Q6: Can instance methods access the class itself?
A: Yes, instance methods can access the class itself.

Q7: How do instance attributes and methods relate to the object created from a class?
A: Instance attributes and methods are properties and behaviors specific to the instance created from a class, rather than the class itself.

"""
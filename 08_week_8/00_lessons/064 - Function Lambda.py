# ------------------------
# -- Function => lambda --
# -- Anonymous Function --
# ------------------------
# [1] It Has No Name
# [2] You Can Call It Inline Without Defining It
# [3] You Can Use It In Return Data From Another Function
# [4] Lambda Used For Simple Functions and Def Handle The Large Tasks
# [5] Lambda is One Single Expression not Block Of Code
# [6] Lambda Type is Function
# Reading list:
# [1] https://www.programiz.com/python-programming/anonymous-function (easy)
# [2] https://realpython.com/python-lambda/ (very detailed and very informative)
# -------------------------------------------------------------------

def say_hello(name, age): return f"Hello {name} your Age Is: {age}"


hello = lambda name, age: f"Hello {name} your Age Is: {age}"

print(say_hello("Ahmed", 36))
print(hello("Ahmed", 36))

print(say_hello.__name__)
print(hello.__name__)

print(type(hello))

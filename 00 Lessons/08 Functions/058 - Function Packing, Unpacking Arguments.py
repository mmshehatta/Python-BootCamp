# >> 00 Lesson
# >> 08 Functions
# >> 058 - Function Packing, Unpacking Arguments.py
from icecream import ic
# --------------------------------------------------
# ---058 - Function Packing, Unpacking Arguments *args
# -------------------------------------------------

# *args benfit:
# 1.unpack list items
myList = [1, 2, 3, 4]
print(myList)  #[1, 2, 3, 4]
print(*myList) #1 2 3 4 ..then * unpack list items

# 2. when i dont know the number of arguements the fun will takes 

def say_hello(n1,n2,n3,n4):
    peoples = [n1,n2,n3,n4]
    for name in peoples:
        ic(f"Hello {name}")


say_hello("Mahmoud" , "Sara" , "Ahmed", "Aziz")
# ic| f"Hello {name}": 'Hello Mahmoud'
# ic| f"Hello {name}": 'Hello Sara'
# ic| f"Hello {name}": 'Hello Ahmed'
# ic| f"Hello {name}": 'Hello Aziz'

# say_hello("Mahmoud" , "Sara" , "Ahmed", "Aziz" , "Ali") #TypeError: say_hello() takes 4 positional arguments but 5 were given

# enhance by *args
def say_hello2(*peoples):  #unbak peoples to n1,n2,n3, ,,,,, 
       for name in peoples:
        ic(f"Hello {name}")

say_hello2("Mahmoud" , "Sara" , "Ahmed", "Aziz") 


say_hello2("Mahmoud" , "Sara" , "Ahmed", "Aziz" , "Ali")
# ic| f"Hello {name}": 'Hello Mahmoud'
# ic| f"Hello {name}": 'Hello Sara'
# ic| f"Hello {name}": 'Hello Ahmed'
# ic| f"Hello {name}": 'Hello Aziz'
# ic| f"Hello {name}": 'Hello Ali'


# example2:

def show_details(name , *skills):
    print(f"Hello {name} Your skills are : ")
    for s in skills:
        print(s)


show_details("Mahmoud","Html","Css" , "Js","Python")

# Hello Mahmoud Your skills are : 
# Html
# Css
# Js
# Python
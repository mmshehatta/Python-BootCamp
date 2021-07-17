# >> 00 Lesson
# >> 08 Functions
# >> 059 - Function Default Parameters.py
from icecream import ic
# --------------------------------------------------
# ---059 - Function Default Parameters
# -------------------------------------------------

def say_hello(name , age="unknow" , city="unknow"):
    print(f"hello {name} your age  is  {age}  your country is {city} ")


# if we dont use default parametes results:
say_hello("Mahmoud", 25 , "Qena")   #hello Mahmoud your age  is  25  your country is Qena 
# say_hello("Ali", 25)            #TypeError: say_hello() missing 1 required positional argument: 'city'

# after we use default params in say_hello() fun: note that default parameter must be last parameter  
say_hello("Ali", 25) #hello Ali your age  is  25  your country is unknow 
say_hello("khaled") #hello khaled your age  is  unknow  your country is unknow 




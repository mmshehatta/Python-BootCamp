
# >> 00 Lesson
# >> 08 Functions
# >>061 - Function Packing Unpacking Arguments Training's.py
from icecream import ic
# ----------------------------------------------------------------
# ---061 - Function Packing Unpacking Arguments Training's.py----
# ---------------------------------------------------------------

myskilsinTuble=("CSS","Js") 
myskilsinDict={
    'CSS':'48%',
    'Angular':'60%',
} 

def show_skills(name="mahmoud" , *skills , **skillsWithProgress):
    print(f"Hello {name} \nYour skills:")
    for s in skills:
        print(f"- {s}")

    print("Your skills with progress are:")
    for key,value in skillsWithProgress.items():
        print(f"- {key} => {value}")



show_skills()
# Hello mahmoud 
# Your skills:
# Your skills with progress are:

show_skills("ali",*myskilsinTuble,**myskilsinDict)
# Hello ali 
# Your skills:
# - CSS
# - Js
# Your skills with progress are:
# - CSS => 48%
# - Angular => 60%


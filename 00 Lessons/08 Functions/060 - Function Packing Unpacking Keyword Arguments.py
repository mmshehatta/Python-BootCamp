

# >> 00 Lesson
# >> 08 Functions
# >> 060 - Function Packing Unpacking Keyword Arguments
from icecream import ic
# ---------------------------------------------------------
# ---060 - Function Packing Unpacking Keyword Arguments----
# ---------------------------------------------------------

myskils=("CSS","Js") 

def show_skills(*skills):
    print(type(skills))  #<class 'tuple'>
    for s in skills:
        print(s)


show_skills("CSS","Js")  
#CSS
# Js

show_skills(myskils)   #('CSS', 'Js')
show_skills(*myskils) 
#CSS
# Js


myDict={
    'html':"40%",
    'css':"50%",
    "go":"22%"
}
def show_skills2(**skills):
    print(type(skills))  #<class 'dict'>
    for s , value in skills.items():
        print(f"{s} = > {value}")



show_skills2(html="44%" , css="66%") 
# html = > 44%
# css = > 66%


# show_skills2(myDict)   #TypeError: show_skills2() takes 0 positional arguments but 1 was given
show_skills2(**myDict) 
# html = > 40%
# css = > 50%
# go = > 22%









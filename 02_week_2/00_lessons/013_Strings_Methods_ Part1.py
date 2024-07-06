# 00 Lesson 
# >> 03 Data Types
# >> 00_Strings 
# >> 013_Strings_methods_part1.py

from icecream import ic
# len built-in fun:return the length of string
mystring = "I love python"
ic(len(mystring)) # ic| len(mystring): 13

# strip(str) , lstrip(str) , rstrip(str)
# they do the same thing : remove str(ch or string) from string
# strip(): removes str(ch or str) from 2 sides
# lstrip():removes str(ch or str) from left side of string
# lstrip():removes str(ch or str) from right side of string
myStringTwo = "   I love Python   "
ic(myStringTwo.strip()) #ic| myStringTwo.strip(): 'I love Python'

mystringTree = "   I love python"
ic(mystringTree.lstrip()) #ic| mystringTree.lstrip(): 'I love python'

mystringFour = "I love python      "
ic(mystringFour.rstrip())  #ic| mystringFour.rstrip(): 'I love python'

# title():
# convert each first letter in all str text into Upper letter , also any char comes after a number
# syntax:str.title()
# Return-value: string with capital first letter words
# parameters:None
mystringFive = "i love techlogies as 2d graphics and 3g techno"
ic(mystringFive.title())#ic| mystringFive.title(): 'I Love Techlogies As 2D Graphics And 3G Techno'

# Capiatalize():
# convert first letter in the str into capital letter
# syntax:str.capitalize()
# Return value: first letter in the str into capital letter
# parameters:None
mystringSix = "i love python"
ic(mystringSix.capitalize()) #ic| mystringSix.capitalize(): 'I love python'

# zfill():
# method that returns a copy of string with '0' characters padding to the left
# it adding zeros(0) at the begging of the string until the lenfth of str speciped qidth parametres

# stynatx:str.zfull(width)
# parameters:width is required 
# return value: returns a copy of string with '0' characters padding to the left
# it add zerors after signs as (-,+), but before ($, # , ext)
# it works with mix str as (A1bc) not just numbers

mystringSiven = "100"
ic(mystringSiven.zfill(5)) #ic| mystringSiven.zfill(5): '00100'

# upper() and lower:
# they converts str from lower to uper and vice versa
# syntax:str.upper() and str.lower()
# return valuer:they converts str from lower to uper and vice versa
# paramaters:None
mystringEight="I Love Python"
ic(mystringEight.lower())#ic| mystringEight.lower(): 'i love python'
ic(mystringEight.upper())#ic| mystringEight.upper(): 'I LOVE PYTHON'








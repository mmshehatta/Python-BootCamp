# 00 Lesson 
# >> 03 Data Types
# >> 00_Strings 
# >> 014_Strings_methods_part2.py
from icecream import ic


# split(sep? == space if not , maxsplit?), rsplit(sep? == space if not , maxsplit?):
# it returns list of str parts based on 'sep' and list len based on maxsplit
# rsplit start splitting from rtl
# styntax:str.split(sep? , max?)
# reurn value:list with split parts
# parameters: sep(option and equal '' if not)
#             max(number of parts in list)

myStringOne = "I love Python and Php and Postegresql"
ic(myStringOne.split())#ic| myStringOne.split(): ['I', 'love', 'Python', 'and', 'Php', 'and', 'Postegresql']

myStringTwo = myStringOne.replace(' ','-')
ic(myStringTwo.split('-'))#ic| myStringTwo.split('-'): ['I', 'love', 'Python', 'and', 'Php', 'and', 'Postegresql']

myStringThree = myStringOne
ic(myStringThree.split(' ',2))#ic| myStringThree.split(' ',2): ['I', 'love', 'Python and Php and Postegresql']

myStringFour = myStringOne
ic(myStringFour.rsplit())#ic| myStringFour.rsplit(): ['I', 'love', 'Python', 'and', 'Php', 'and', 'Postegresql']

myStringFive = myStringOne
ic(myStringFive.rsplit(' ', 2))#ic| myStringFive.rsplit(' ', 2): ['I love Python and Php', 'and', 'Postegresql']


# center():
# adding new char at the start and end of string to complete length of specified number
# Synatx:str.center(num , char)
# returned value:new string with ledding and ends char
# params:|number| it is required .. |char| it is opt , is space if not   

myStringSix = "Mahmoud"
ic(myStringSix.center(9,'@'))#ic| myStringSix.center(9,'@'): '@Mahmoud@'

# count():
# return number of repeats substr in the string and starts search from 0 index to str.length this if don't specify start or end to search
# Syntax:str.count(substr , start , end)
# return value:number represents substrings in str.
# params:|substr|that searched for it..|start| search from |end| search to

myStringSiven = "I Love Python"
ic(myStringSiven.count('I'))#ic| myStringSiven.count('I'): 1
ic(myStringSiven.count('o'))#ic| myStringSiven.count('o'): 2
ic(myStringSiven.count('o',4))#ic| myStringSiven.count('o',4): 1
ic(myStringSiven.count('o',0,4))#ic| myStringSiven.count('o',0,4): 1
ic(myStringSiven.count('Love',0,6))#ic| myStringSiven.count('Love',0,6): 1

# swapcase(): convert str from lower to upper and vice versa
# synatx:str.swapcase()
# return value: string with toggeled case
# params:none
ic(myStringSiven.swapcase()) #ic| myStringSiven.swapcase(): 'i lOVE pYTHON'


# startswith(): return True or Fale if perfix is in the string or not 
# sytax:str.startswith(prefix , start , end)
# params: |prefix| is the substring you search for ..|start| from where start scannig ..|end| scanning to where
myStringEight = "I love Python"
ic(myStringEight.startswith('I'))#ic| myStringEight.startswith('I'): True
ic(myStringEight.startswith('I',1))#ic| myStringEight.startswith('I',1): False
ic(myStringEight.startswith('I love'))#ic| myStringEight.startswith('I love'): True
ic(myStringEight.startswith('I love',0,4))#ic| myStringEight.startswith('I love',0,4): False


# endsswith(): return True or Fale if postfix is in the string or not 
# sytax:str.startswith(postfix , start , end)
# params: |postfix| is the substring you search for ..|start| from where start scannig ..|end| scanning to where
myStringNign = "I love Python"
ic(myStringNign.endswith('I'))#ic| myStringNign.endswith('I'): False
ic(myStringNign.endswith('Python'))#ic| myStringNign.endswith('Python'): True











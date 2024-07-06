# 00 Lesson 
# >> 03 Data Types
# >> 00_Strings 
# >> 015_Strings_methods_part3.py
from icecream import ic

# index: return integer number that represents the position of substr in string , it starts from 0 if now start determind and end with string limit if no end determined
# returned value: integer number
# syntax: str.index(substr , start , end)
# params:|substr| that we need to grt it's index |start| from where i start
#|end| where i will stop.
myString="I Love Python"
ic(myString.index("P")) #ic| myString.index("P"): 7
# ic(myString.index("P", 8)) #ValueError: substring not found
ic(myString.index("o")) #ic| myString.index("o"): 3
ic(myString.index("o",4)) #ic| myString.index("o",4): 11
ic(myString.index("o",4,12)) #ic| myString.index("o",4,12): 11

# find:()
# --------
#  return integer number that represents the position of substr in string , it starts from 0 if now start determind and end with string limit if no end determined
# returned value: integer number if substr exist , -1 if not exists
# syntax: str.index(substr , start , end)
# params:|substr| that we need to grt it's index |start| from where i start
#|end| where i will stop.

ic(myString.find("P", 8)) #ic| myString.find("P", 8): -1

# ljust() and rjust():
# --------------------
# they returns new string filling with *fill char* in left or right side based on function and width params
# return value: new filled string
# syntax:str.ljust(width,char fill) , rjust(width , fill char)

myString2="Mahmoud"
ic(myString2.ljust(10)) #ic| myString2.ljust(10): 'Mahmoud   '
ic(myString2.ljust(10,'#')) #ic| myString2.ljust(10,'#'): 'Mahmoud###'

myString3="Mahmoud"
ic(myString3.rjust(10)) #ic| myString3.rjust(10): '   Mahmoud'
ic(myString3.rjust(10,'#')) #ic| myString3.rjust(10,'#'): '###Mahmoud'


# splitlines():
# ------------ 
# split string to line at some boundrys(\n , \r , ect) , if no boundry it return empty list , if you give it keepend param and set it to true ,thrn each list item will followed by boundry litter
# Return Value: list of lines
# syntax:mystr.splitlines(keepends)
# params:|keepends| if set to True or positve or negative , then each item element will followd by (\n \r or any boundry) , and if keepends set to false or zero ..will remove boundry from list items.

myString4="""first line
second line
third line
"""
ic(myString4.splitlines()) #ic| myString4.splitlines(): ['first line', 'second line', 'third line']

myString5="first line\rsecond line\rthird line"
ic(myString5.splitlines(1))#ic| myString5.splitlines(1): ['first line\r', 'second line\r', 'third line']


# expandtabs():
# ------------
# Return Value: new string with all tab char \t replaced with one or more space based on num of char before \t and specified tab size
# styntax: mystr.expandtabs(tabsize)
# params: |tabsize| specipes num of spaces

myString6=" Hello\tI\tlove\tPython"
ic(myString6.expandtabs()) #ic| myString6.expandtabs(): ' Hello  I       love    Python'
ic(myString6.expandtabs(2)) #ic| myString6.expandtabs(2): ' Hello12I12love12Python' ..i put num to explanation


# ##### string check function ####
# 1.istitle():
str1 = 'I love python and 2d graphics' #ic| one.istitle(): False
ic(str1.istitle())

str2 = "I Love Python And 2D Graphics"
ic(str2.istitle()) #ic| str2.istitle(): True
# 2.isspace():
str3 = " "
str4 = "A"
ic(str3.isspace()) #ic| str3.isspace(): True
ic(str4.isspace()) #ic| str3.isspace(): False


# 3.islower():
str5 = "mahmoud"
str6 = "Mahmoud"
ic(str5.islower()) #ic| str6.islower(): True
ic(str6.islower()) #ic| str6.islower(): False
# 4.isidentifier(): to check if var name be idetifer or not
str7=" 111_var1"
str8="var1"
ic(str7.isidentifier()) #ic| str7.isidentifier(): False
ic(str8.isidentifier()) #ic| str8.isidentifier(): True

# isalpha():is string alphabetic only or has num(aA-zZ)
mystr1="AAAAb"
mystr2="AAAA123"
ic(mystr1.isalpha())#ic| mystr1.isalpha(): True
ic(mystr2.isalpha())#Falsemystr2.isalpha(): False
# isalnum():is str mix of (aA-zZ) and digits(0-9)
mystr3 ="AAAAAB"
mystr4 ="AAAAA123"
ic(mystr3.isalnum()) #ic| mystr3.isalnum(): True
ic(mystr4.isalnum()) #ic| mystr4.isalnum(): True

# ------ Finally The End heeeeh----------


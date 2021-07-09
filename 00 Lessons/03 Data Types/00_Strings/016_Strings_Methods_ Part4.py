# 00 Lesson 
# >> 03 Data Types
# >> 00_Strings 
# >> 016_Strings_methods_part4.py
from icecream import ic

# replace(old vlaue , new value , count):
# return value : new string replaced with new value
# syntax:repalce(old vlaue , new value , count)
# params:|old value|need to replaced..|new value| str need to be in text..|count| do need to replace all occournces or just count?

mystr1="one two three one one"
ic(mystr1.replace("one","1")) #ic| mystr1.replace("one","1"): '1 two three 1 1'
ic(mystr1.replace("one","1",1)) #ic| mystr1.replace("one","1",1): '1 two three one one'
ic(mystr1.replace("one","1",2)) #ic| mystr1.replace("one","1",2): '1 two three 1 one'


# (sep).join(iteratable):
# return value():new string consist of iteratable items separated with new join params
# syntax: (sep).join(iteratable)
# params:|sep| separate new string 
mylist=["mahmoud" , "shehata" ,"muhammed"]
ic((" ").join(mylist)) #ic| (" ").join(mylist): 'mahmoud shehata muhammed'
ic(('-'.join(mylist))) #ic| '-'.join(mylist): 'mahmoud-shehata-muhammed'


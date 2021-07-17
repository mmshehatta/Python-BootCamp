# >> 00 Lesson
# >> 08 Functions
# >> 086 - Practical Loop On Many Iterators With Zip.py
from icecream import ic
from time import time

#############################################################
# >> 086 - Practical Loop On Many Iterators With Zip.py
#############################################################
# zip() return A zip object conatins all object
# zip() zip length is length of lowest object
#############################################################


list1 = [1, 2, 3, 4]
list2 = ["A", "B", "C"]
tuple1 = ("Man", "Woman", "Boy", "Girl")
dict1 = {"name": "Mahmoud", "age": 25, "city": "qena"}

for item1, item2 ,item3 , item4 in zip(list1 , list2 , tuple1 , dict1):
    ic("item1 => " , item1)
    ic("item2 => " , item2)
    ic("item3 => " , item3)
    ic("item4 => " , item4)

# ic| 'item1 => ', item1: 1
# ic| 'item2 => ', item2: 'A'
# ic| 'item3 => ', item3: 'Man'
# ic| 'item4 => ', item4: 'name'
# ic| 'item1 => ', item1: 2
# ic| 'item2 => ', item2: 'B'
# ic| 'item3 => ', item3: 'Woman'
# ic| 'item4 => ', item4: 'age'
# ic| 'item1 => ', item1: 3
# ic| 'item2 => ', item2: 'C'
# ic| 'item3 => ', item3: 'Boy'
# ic| 'item4 => ', item4: 'city'
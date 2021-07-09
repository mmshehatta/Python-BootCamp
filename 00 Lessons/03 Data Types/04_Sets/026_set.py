# 00 Lesson
# >> 03 Data Types
# >> 03 Sets
# >> 026_set.py

from icecream import ic

# -----------------------------
# [1] set items enclosed in Curly Braces
# [2] set items not ordered and not indexed
# [3] set indexing and slicing can not be done
# [4] set has onley immutable data types (Numbers , strings , tubles ) list and dict are not
# [5] set items are unique
# []
# -----------------------------

# [1] set items enclosed in Curly Braces
# [2] set items not ordered and not indexed
mySet1 = {1, "Mahmoud", "Ahmed"}
ic(mySet1)  # ic| mySet1: {1, 'Ahmed', 'Mahmoud'}
ic(mySet1)  # ic| mySet1: {'Mahmoud', 1, 'Ahmed'}
ic(mySet1)  # ic| mySet1: {1, 'Ahmed', 'Mahmoud'}

# ic(mySet1[1])  # TypeError: 'set' object is not subscriptable


# [3] set indexing and slicing can not be done
mySet2 = {1, 2, 3, 4, 5}
# ic(mySet2[1:3])   # TypeError: 'set' object is not subscriptable


# [4] set has onley immutable data types (Numbers , strings , tubles ) list and dict are not
# mySet3={1,2,"A", 100.34 , True ,[1,2]}
# ic(mySet3)   #TypeError: unhashable type: 'list'

mySet4={1,2,"A", 100.34 , True ,(1,2)}
ic(mySet4)   #ic| mySet4: {1, 2, (1, 2), 100.34, 'A'}


# [5] set items are unique
mySet5 = {1,2,"Mahmoud", 3,"Mahmoud"}
ic(mySet5)  #ic| mySet5: {1, 2, 3, 'Mahmoud'} -- remove dublicate



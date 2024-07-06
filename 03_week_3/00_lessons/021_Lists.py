
# 00 Lesson 
# >> 03 Data Types
# >> 01_Lists
# >> 021_Lists.py

from icecream import ic
# --------------
# Lists:
# [1] List Items are enclosed in square brackets
# [2] Lists are ordered , use index to access item 
# [3] Lists are mutable => you can Add , update and delete   
# [4] Lists Items is not unique
# [5] List can have different data types
# [6] List mutable not replace , so i can remove or than one item and put empty or one or as i like
# --------------

myList=["one", "two" , "one" , 1 , 1.400 ,True , 1+2j]

ic(myList) #ic| myList: ['one', 'two', 'one', 1, 1.4, True, (1+2j)]
ic(myList[0]) #ic| myList[0]: 'one'
ic(myList[-1]) #ic| myList[-1]: (1+2j)
ic(myList[-3]) #ic| myList[-3]: 1.4
ic(myList[1:4])#ic| myList[1:4]: ['two', 'one', 1]
ic(myList[1:])#ic| myList[1:]: ['two', 'one', 1, 1.4, True, (1+2j)]
ic(myList[:4])#ic| myList[:4]: ['one', 'two', 'one', 1]

ic(myList[::1])  #ic| myList[::1]: ['one', 'two', 'one', 1, 1.4, True, (1+2j)]
ic(myList[::2])  #ic| myList[::2]: ['one', 'one', 1.4, (1+2j)]
# ic(myList[180])  #IndexError: list index out of range

ic(myList) #ic| myList: ['one', 'two', 'one', 1, 1.4, True, (1+2j)]
myList[1]=2
ic(myList) #ic| myList: ['one', 2, 'one', 1, 1.4, True, (1+2j)]
myList[-2]=False
ic(myList) #ic| myList: ['one', 2, 'one', 1, 1.4, False, (1+2j)]

myList[0:3]=[]
ic(myList) #ic| myList: [1, 1.4, False, (1+2j)]

myList[0:3]=["A","B","C"]
ic(myList) #ic| myList: ['A', 'B', 'C', (1+2j)]
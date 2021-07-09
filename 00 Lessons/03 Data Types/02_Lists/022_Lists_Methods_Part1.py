# 00 Lesson
# >> 03 Data Types
# >> 01_Lists
# >> 022_Lists_methods_part1.py

from icecream import ic

# List Methods:
# -((((append() )))-:
myFriends = ["Khaled", "Mahmoud", "Mustafa"]
myOldFriends = ["Amr", "Ahmed", "Hossam"]

myFriends.append("Alaa")
ic(myFriends)  # ic| myFriends: ['Khaled', 'Mahmoud', 'Mustafa', 'Alaa']

myFriends.append(100)
ic(myFriends)  # ic| myFriends: ['Khaled', 'Mahmoud', 'Mustafa', 'Alaa', 100]

myFriends.append(100.500)
# ic| myFriends: ['Khaled', 'Mahmoud', 'Mustafa', 'Alaa', 100, 100.5]
ic(myFriends)

myFriends.append(True)
# ic| myFriends: ['Khaled', 'Mahmoud', 'Mustafa', 'Alaa', 100, 100.5, True]
ic(myFriends)

myFriends.append(myOldFriends)
# ic| myFriends: ['Khaled', 'Mahmoud', 'Mustafa', 'Alaa', 100, 100.5, True,['Amr', 'Ahmed', 'Hossam']]
ic(myFriends)

# Accessing list items:
ic(myFriends[2])  # ic| myFriends[2]: 'Mustafa'
ic(myFriends[6])  # ic| myFriends[6]: True
ic(myFriends[7])  # ic| myFriends[7]: ['Amr', 'Ahmed', 'Hossam']
ic(myFriends[7][2])  # ic| myFriends[7][2]: 'Hossam'
ic(myFriends[7][-2])  # ic| myFriends[7][-2]: 'Ahmed'


# -((((extend() )))-:(__iterable: Iterable[int]) -> None Extend list by appending elements from the iterable.


listA = [1, 2, 3, 4]
listB = ["A", "B", "c", "D"]
listC = ["One", "Two"]

listA.extend(listB)
ic(listA)  # ic| listA: [1, 2, 3, 4, 'A', 'B', 'c', 'D']

listA.extend(listC)
ic(listA)  # ic| listA: [1, 2, 3, 4, 'A', 'B', 'c', 'D', 'One', 'Two']

# -((((remove() )))-:Remove first occurrence of value.Raises ValueError if the value is not present.

listX = [1, 2, 3, 4, "Mahmoud", True, "Mahmoud", "Mahmoud"]
listX.remove("Mahmoud")
ic(listX)  # ic| listX: [1, 2, 3, 4, True, 'Mahmoud', 'Mahmoud']

# -((((sort(reverse=True or False(default)) ))):(*, key: None = ..., reverse: bool = ...) -> None
'''
Sort the list in ascending order and return None.
The sort is in-place (i.e. the list itself is modified) and stable (i.e. the order of two equal elements is maintained).
If a key function is given, apply it once to each list item and sort them, ascending or descending, according to their function values.
'''


listY = [1, 2, 100, 120, -10, 17, 29]
listY.sort()
ic(listY)     #ic| listY: [-10, 1, 2, 17, 29, 100, 120]
listY.sort(reverse=True)
ic(listY)     #ic| listY: [120, 100, 29, 17, 2, 1, -10]
listYY = ["A","B","C"]
listYY.sort(reverse=True)
ic(listYY)   #ic| listYY: ['C', 'B', 'A']




# -((((reverse() )))-: () -> None Reverse *IN PLACE*.| more than one type in list , but sort must in same datatype
listZ = [1, 2,"Mahmoud", 120, -10]
listZ.reverse()
ic(listZ)      #ic| listZ: [-10, 120, 'Mahmoud', 2, 1]



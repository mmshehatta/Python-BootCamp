# 00 Lesson
# >> 03 Data Types
# >> 01_Lists
# >> 023_Lists_methods_part2.py

from icecream import ic

# List Methods Part2:

# -((((clear() )))-: () -> None Remove all items from list.
listA = [1, 2, 3]
listA.clear()
ic(listA)  # ic| listA: []


# -((((copy() )))-:  () -> List[int] Return a shallow(new don't affect on(osma-elzero)) copy of the list.
listB = [1, 2, 3]
listC = listB.copy()
ic(listC)  # ic| listC: [1, 2, 3]

listB.append(5)
ic(listB)  # ic| listB: [1, 2, 3, 5]
ic(listC)  # ic| listC: [1, 2, 3] do not affected


# -((((count() )))-:   (__value: int) -> int Return number of occurrences of value.
listE = [1, 2, 3, 4, 5, 6, 6, 7, 8]
ic(listE.count(6))  # ic| listE.count(6): 2


# -((((index() )))-: (__value: str, __start: int = ..., __stop: int = ...) -> int Return first index of value.
#  Raises ValueError if the value is not present.
myFriends = ["Khaled", "Mahmoud", "Mustafa"]
ic(myFriends.index("Khaled"))  # ic| myFriends.index("Khaled"): 0
# ic(myFriends.index("Khale"))   #ValueError: 'Khale' is not in list


# -((((insert() )))-:  (__index: int, __object: Any) -> NoneInsert object before index.
listF = [1, 2, 3, "A", "B"]
listF.insert(0,0)
ic(listF)       #ic| listF: [0, 1, 2, 3, 'A', 'B']
listF.insert(6,"c")
ic(listF)       #ic| listF: [0, 1, 2, 3, 'A', 'B', 'c']


# -((((pop() )))-: (__index: int = ...) -> Any Remove and return item at index (default last).
#  Raises IndexError if list is empty or index is out of range.
listG = [1, 2, 3, "A", "B"]
ic(listG.pop())     #ic| listG.pop(): 'B'
ic(listG.pop(2))    #ic| listG.pop(2): 3
ic(listG.pop(-3))   #ic| listG.pop(-3): 2
# ic(listG.pop(10))   #IndexError: pop index out of range
  
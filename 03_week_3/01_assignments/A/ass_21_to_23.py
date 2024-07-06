"""
Assignments on Lessons From 21 to 23
"""

from icecream import ic
"""

Ass 1:
-----

"""

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
ic(friends[0])
ic(friends.pop(0))

# Output:
# ic| friends[0]: 'Osama'     --->[1]
# ic| friends.pop(0): 'Osama '--->[2]


ic(friends[-1])
ic(friends.pop(-1))

# Output:
# c| friends[-1]: 'Mahmoud'      --->[1]
# ic| friends.pop(-1): 'Mahmoud' --->[2]


"""

Ass 2:
-----

"""
friends2 = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(*friends2[::2], sep=", ")
print(*friends2[1::2], sep=", ")
# Or
print(" ".join(friends2[::2]), sep=", ")
print(" ".join(friends2[1::2]), sep=", ")

# Output:
# Osama, Sayed, Mahmoud
# Ahmed, Ali
# Osama Sayed Mahmoud
# Ahmed Ali


"""

Ass 3:
-----

"""
friends3 = ["Osama", "Ahmed", "Sayed", "Ali", "Khaled", "Mahmoud"]

print(*friends3[1:4], sep=", ")
print(*friends3[-2:], sep=", ")

# Output:
# Ahmed, Sayed, Ali
# Khaled, Mahmoud


"""

Ass 4:
-----

"""

friends4 = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
friends4[-2:] = ["ElZero", "ElZero"]
print(friends4)

# Output:
# ['Osama', 'Ahmed', 'Sayed', 'ElZero', 'ElZero']


"""

Ass 5:
-----

"""
friends5 = ["Osama", "Ahmed", "Sayed"]
friends5.insert(0, "Nasser")
friends5.insert(len(friends5), "Salem")
print("friends5 : ", friends5)

# Output:
# friends5 :  ['Nasser', 'Osama', 'Ahmed', 'Sayed', 'Salem']


"""

Ass 6:
-----

"""
friends6 = ['Nasser', 'Osama', 'Ahmed', 'Sayed', 'Salem']
friends6[:2] = []
print("friends6 : ", friends6)
friends6[-1:] = []
print("friends6 : ", friends6)

# Output:
# friends6 :  ['Ahmed', 'Sayed', 'Salem']
# friends6 :  ['Ahmed', 'Sayed']


"""

Ass 7:
-----

"""
friends = ['Ahmed', 'Sayed']
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
friends.extend(employees+school)
ic(friends)


# Output:
# ic| friends: ['Ahmed', 'Sayed', 'Samah', 'Eman', 'Ramy', 'Shady']


"""

Ass 8:
-----

"""
friends = ['Ahmed', 'Sayed', 'Samah', 'Eman', 'Ramy', 'Shady']
friends.sort()
# or
# sorted(friends)
ic(friends)
friends.sort(reverse=True)
# or
# sorted(friends , reverse=True)
ic(friends)

# output
# ic| friends: ['Ahmed', 'Eman', 'Ramy', 'Samah', 'Sayed', 'Shady']
# ic| friends: ['Shady', 'Sayed', 'Samah', 'Ramy', 'Eman', 'Ahmed']


"""

Ass 9:
-----

"""
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
ic("Num Of Friends = ", len(friends))

# Output
# ic| 'Num Of Friends = ', len(friends): 6


"""

Ass 10:
-----

"""
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

ic(technologies[4][0])
ic(technologies[4][-1])
#  Output
# ic| technologies[4][0]: 'Django'
# ic| technologies[4][-1]: 'Web'

"""
Assignments on Lessons From 26 to 32
"""

from xml.etree.ElementPath import find
from icecream import ic

"""

Ass 1:
-----

"""
# Sol1:
my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = set(my_list)
unique_list = list(unique_list)
ic(unique_list)
ic(type(unique_list))
unique_list.pop()
ic(unique_list)

# Sol2:Remove Duplicates from a list using the Temporary List
my_list = [1, 2, 3, 3, 4, 5, 1]
print("List Before ", my_list)
temp_list = []

for i in my_list:
    if i not in temp_list:
        temp_list.append(i)

my_list = temp_list

print("List After removing duplicates ", my_list)

# Sol3:
my_list = [1, 2, 3, 3, 4, 5, 1]
my_final_list = dict.fromkeys(my_list)
print(list(my_final_list))

# Needed Output
# ic| unique_list: [1, 2, 3, 4, 5]
# ic| type(unique_list): <class 'list'>
# ic| unique_list: [1, 2, 3, 4]


"""

Ass 2:
-----

"""

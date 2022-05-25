"""
Assignments on Lessons From 26 to 32
"""

from xml.etree.ElementPath import find
from icecream import ic

"""

Ass 1:
-----

"""

my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = set(my_list)
unique_list = list(unique_list)
ic(unique_list)
ic(type(unique_list))
unique_list.pop()
ic(unique_list)

# Needed Output
# ic| unique_list: [1, 2, 3, 4, 5]
# ic| type(unique_list): <class 'list'>
# ic| unique_list: [1, 2, 3, 4]
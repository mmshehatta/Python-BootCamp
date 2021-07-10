
# 00 Lesson
# >> 03 Data Types
# >> 05 dictionary
# >> 032_dictionary_methods_p2.py

from icecream import ic
# ####### Methods part1 #####:
# 1.setdefualt():
# (__key: str, __default: str = ...) -> str
# Insert key with a value of default if key is not in the dictionary.
# Return the value for key if key is in the dictionary, else default.

user = {
    'name': 'Mahmoud'
}

ic(user)  # ic| user: {'name': 'Mahmoud'}
# ic| user.setdefault('name','ali'): 'Mahmoud'..it will ali if name not exists
ic(user.setdefault('name', 'ali'))
ic(user)  # ic| user: {'name': 'Mahmoud'}


user2 = {

}
ic(user2)  # ic| user2: {}
# ic| user2.setdefault('name','mahmoud'): 'mahmoud'
ic(user2.setdefault('name', 'mahmoud'))
ic(user2)  # ic| user2: {'name': 'mahmoud'}


# 3.popitem():it will return last added item in dict
# () -> Tuple[str, str]
# Remove and return a (key, value) pair as a 2-tuple.
# Pairs are returned in LIFO (last-in, first-out) order. Raises KeyError if the dict is empty.

member = {
    'name': 'mahmoud',
    'skills': 'Js'
}

ic(member)  # ic| member: {'name': 'mahmoud', 'skills': 'Js'}
ic(member.popitem())  # ic| member.popitem(): ('skills', 'Js')
ic(member)  # ic| member: {'name': 'mahmoud'}

member2 = {}
ic(member2)  # ic| member2: {}
# ic(member2.popitem())   #KeyError: 'popitem(): dictionary is empty'

# 4.items():
# () -> ItemsView[str, str]
# D.items() -> a set-like object providing a view on D's items

view = {
    'name': 'Mahmoud',
    'skills': 'js'
}

# ic| view.items(): dict_items([('name', 'Mahmoud'), ('skills', 'js')])
ic(view.items())
view['age'] = 25    #
# ic| view.items(): dict_items([('name', 'Mahmoud'), ('skills', 'js'), ('age', 25)])
ic(view.items())


# 5.fromkeys():
# (__iterable: Iterable[_T@fromkeys], __value: None = ...) -> dict[_T@fromkeys, Any | None]
# Create a new dictionary with keys from iterable and values set to value.
A = ("key1", "key2", "key3")

b = "value"

myDict = dict.fromkeys(A, b)

ic(myDict)     #ic| myDict: {'key1': 'value', 'key2': 'value', 'key3': 'value'}




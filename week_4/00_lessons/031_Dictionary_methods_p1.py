
# 00 Lesson
# >> 03 Data Types
# >> 05 dictionary
# >> 031_dictionary_methods_p1.py

from icecream import ic
# ####### Methods part1 #####:
# 1.clear():
# () -> None
# D.clear() -> None. Remove all items from D.

user = {
    'name': 'Mahmoud',
    'age': 35,
    'country': 'Egypt'
}

ic(user)     #ic| user: {'age': 35, 'country': 'Egypt', 'name': 'Mahmoud'}
user.clear()
ic(user)     #ic| user: {}


# 2.update(): to add new item to your dict .. And you can update it without this function 
# (__m: Mapping[str, Any], **kwargs: Any) -> None
# D.update([E, ]**F) -> None. Update D from dict/iterable E and F. If E is present and has a .keys() method, then does: for k in E: D[k] = E[k] If E is present and lacks a .keys() method, then does: for k, v in E: D[k] = v In either case, this is followed by: for k in F: D[k] = F[k]


member={
    'name':'ali'
}
ic(member)          #ic| member: {'name': 'ali'}
member['age'] = 25
ic(member)          #ic| member: {'age': 25, 'name': 'ali'}

member.update({'country':'Egypt'})
ic(member)         #ic| member: {'age': 25, 'country': 'Egypt', 'name': 'ali'} 


# 3.copy():
# () -> Dict[str, str]
# D.copy() -> a shallow copy of D
dictA ={
    'name' : 'mahmoud'
}
ic(dictA)            #ic| dictA: {'name': 'mahmoud'}
dictB = dictA.copy()
ic(dictB)           #ic| dictB: {'name': 'mahmoud'}
dictA['age'] = 25
ic(dictA)            #ic| dictA: {'age': 25, 'name': 'mahmoud'}
ic(dictB)            #ic| dictB: {'name': 'mahmoud'}..dont affected









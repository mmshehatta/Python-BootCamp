# التكليف 04
#  ============
from icecream import ic

#my_all
def my_all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

print(my_all([1, 2, 3]))
print(my_all([1, 2, 3, []]))

# my_any:
def my_any(iterable):
    for element in iterable:
        if element:
            return True
    return False

print(my_any([0, 1, [], False])) #True
print(my_any([(), 0, False])) # False


# my_min
def my_min(iterable):
    if type(iterable) in [list , tuple]:
        iterable = sorted(iterable)
        return iterable[0]
    else:
        return f"{type(iterable) } is not list or tuble"


# print(my_min([10, 100, -20, -100, 50])) # -100
# print(my_min((10, 100, -20, -100, 50))) # -100
# print(my_min({1,2})) # <class 'set'> is not list or tuble


# my_min2
def my_min2(iterable):
     if type(iterable) in [list , tuple]:
        min_elem = iterable[0]
        for elem in iterable:
            if elem < min_elem:
                min_elem = elem
                continue
        return min_elem

     else:
        return f"{type(iterable) } is not list or tuble"


ic(my_min2([10, 100, -20, -100, 50])) # -100
ic(my_min2((10, 100, -20, -100, 50))) # -100
ic(my_min2({1,2})) # <class 'set'> is not list or tuble


# my_max
def my_max(iterable):
     if type(iterable) in [list , tuple]:
        iterable = sorted(iterable)
        return iterable[len(iterable) - 1]
     else:
        return f"{type(iterable) } is not list or tuble"
    


# print(my_max([10, 100, -20, -100, 50, 700])) # 700
# print(my_max((10, 100, -20, -100, 50, 700))) # 700
# print(my_max({1,2})) # <class 'set'> is not list or tuble


# my_min2
def my_max2(iterable):
     if type(iterable) in [list , tuple]:
        max_elem = iterable[0]
        for elem in iterable:
            if elem > max_elem:
                max_elem = elem
                continue
        return max_elem

     else:
        return f"{type(iterable) } is not list or tuble"


ic(my_max2([10, 100, -20, -100, 50, 700])) # 700
ic(my_max2((10, 100, -20, -100, 50, 700))) # 700
ic(my_max2({1,2})) # <class 'set'> is not list or tuble
"""
Ass3
-----
قم بإنشاء Set تحتوي على العناصر 1, 2, 3
في السطر الأول قم بطباعة محتوى ال Set
قم بإفراغ محتوى ال Set كاملا بسطر واحد فقط ثم قم بطباعة المحتوى في السطر الثاني لتتأكد من أنها فارغة تماما
قم بإضافة عنصرين “A”, “B” لهذه ال Set ثم إطبع محتواها في السطر الثالث
قم بمحاولة إزالة العنصر “C” طبعا العنصر غير موجود تأكد أنه لن يخرج لك خطأ عندما تحاول إزالة العنصر الغير موجود

Refs:
https://www.programiz.com/python-programming/set#:~:text=Removing%20elements%20from%20a%20set,not%20present%20in%20the%20set.
"""
my_set = {1, 2, 3}
letters = {"A", "B", "C"}
# TODO:
# . print set
# . make it empty
# . print it to ensure it is empty
# . remove not found c from the set and ensure no error will appear
print(my_set)
my_set.clear()
print(my_set)

my_set.add("A")
my_set.add("B")
print(my_set)

my_set.discard("C")

# Needed Output
# {1, 2, 3}
# set()
# {"A", "B"}

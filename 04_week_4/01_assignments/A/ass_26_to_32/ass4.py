"""
Ass4
-----
قم بإنشاء Set تحتوي على العناصر 1, 2, 3
قم بإنشاء Set ثانية تحتوي على 1, 2, 3, 4, 5, 6
تأكد ان جميع محتويات ال Set الأولى موجود في الثانية أم لا

Refs:https://www.programiz.com/python-programming/set#:~:text=Removing%20elements%20from%20a%20set,not%20present%20in%20the%20set.
"""

set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_one.issubset(set_two))

# Needed Output
# True


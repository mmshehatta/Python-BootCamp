"""
التكليف 01
قم بعمل متغير بإسم name يحتوي على ال Input الخاص بإسم الشخص
قم بالتأكد من أن أي مسافات قبل وبعد إسم الشخص سوف يتم إزالتها
قم بالتأكد من أن إسم الشخص سوف يكون أول حرف Capital وجميع احروف الأخرى Small
قم بطباعة الإسم مع رسالة ترحيبية

"""
from icecream import ic

name = input('What\'s Is Your First Name?')
name = name.strip().capitalize()
ic(f" Hello {name} Happy To See You Here.")

# Output : ic| f" Hello {name} Happy To See You Here.": ' Hello Osama Happy To See You Here.'

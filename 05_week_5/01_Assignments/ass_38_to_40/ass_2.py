"""
التكليف 02
قم بعمل متغير بإسم age يحتوي على ال Input الخاص بعمر الشخص
قم بالتأكد من أن المدخل سوف يكون Integer وليس String
إذا كان العمر أصغر من 16 قم بطباعة رسالة تعبر عن أن الموقع يحتوي على مقالات غير مناسبة لسن تحت ال 16
إذا كان العمر 16 أو أكثر قم بطباعة رسالة ترحيبية تحتوي على العمر وأن الموقع مناسب للشخص
"""
from icecream import ic

age = int(input("Enter Your Age : "))
if age < 16:
    ic("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
else:
    ic(f"Hello Your Age Is {age}, All Articles Is Suitable For You")

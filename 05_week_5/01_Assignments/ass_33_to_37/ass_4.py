"""
التكليف 04
هذا التكليف يفيدك في تطوير مستواك في إستخدام ال Methods داخل بعضها وفصل العمليات الحسابية وإستخدام الأقواس بشكل سليم ومنظم
قم بإنشاء متغير باسم num_one والقيمة الخاصة به هي رقم 10
قم بإنشاء متغير بإسم num_two والقيمة الخاصة به هي رقم 20
قم بتخزين نتيجة جمع المتغيريين في متغير جديد بإسم result وقم بطباعته في السطر الأول
في السطر الثاني قم بإيجاد نتيجة رفع الرقم لل Exponent 3
في السطر الثالث قم بإيجاد باقي قسمة الرقم الناتج من الطلب السابق على 26000
في السطر الرابع قم بطباعة نتيجة قسمة الرقم الناتج على 5
تأكد أن الرقم السابق عبارة عن Float لتعرف أنك وصلت للحل بشكل سليم
في السطر الخامس قم بطباعة النوع بعد تحويله ل String للتأكد من أنه String
"""
from icecream import ic
import math

num_one = 10
num_two = 20
result = num_one + num_two

ic(result)
ic(math.pow(result, 3))
ic((math.pow(result, 3)) % 26000)
ic(((math.pow(result, 3)) % 26000) / 5)
ic(type((math.pow(result, 3)) / 26000))
res = str((math.pow(result, 3)) % 26000 / 5)
ic(type(res))
# Output:
# ic| result: 30
# ic| math.pow(result, 3): 27000.0
# ic| (math.pow(result, 3)) % 26000: 1000.0
# ic| ((math.pow(result, 3)) % 26000)/5: 200.0
# ic| type((math.pow(result, 3)) / 26000): <class 'float'>
# ic| type(res): <class 'str'>

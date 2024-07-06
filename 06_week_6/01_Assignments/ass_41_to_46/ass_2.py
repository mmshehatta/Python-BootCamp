"""
التكليف 02
قم بعمل متغير فيه سن الشخص والقيمة الخاصة به 17
قم بعمل دالة شرطية مختصرة If Condition في سطر واحد فقط بإستخدام Ternary Conditional Operator
في حالة كان العمر أكبر من 16 تظهر رسالة أن التطبيق مناسب لك وغير ذلك التطبيق غير مناسب لك
"""
from icecream import ic
# Does Python have a ternary conditional operator?
# Yes, it was added in version 2.5. The expression syntax is:
# a if condition else b
# ref:https://stackoverflow.com/questions/394809/does-python-have-a-ternary-conditional-operator

age = 18
ic("App Is Suitable For You" if age > 17 else "App Is Not Suitable For You")

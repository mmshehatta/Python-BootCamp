"""
التكليف 02
قم بإنشاء 3 متغيرات فيهم أسماء أي مهارات برمجية تمتلكها والقيمة الخاصة بهم هي نسبة تعلمك لهذه المهارات وتكون كلها فوق 50%
في سطر واحد فقط وبواسطة ال Boolean Operators قم بالتأكد أن نسبة تعلمك في جميع المهارات أكبر من 50%
يجب عدم إستخدام If Condition هنا ويجب إرجاع النتيجة Trur
"""
from icecream import ic

html = 80
css = 60
javascript = 70
ic(html > 50 and css > 50 and javascript > 50)
# output: ic| html > 50 and css > 50 and javascript > 50: True

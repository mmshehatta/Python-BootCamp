
"""
التكليف 04
قم بعمل متغير باسم email يحتوي على ال Input الخاص بالبريد الإلكتروني للشخص
قم بالتأكد من إزالة المسافات قبل وبعد البريد الإلكتروني
قم بالتأكد من أن جميع الحروف سوف تكون صغيرة Lower Letters
قم بطباعة رسالة في السطر الأول تحتوي على إسم الشخص فقط الموجود قبل علامة @ مع تحويل أول حرف لحرف كبير Capital
قم بطباعة رسالة في السطر الثاني تحتوي على الموقع الموجود عليه البريد الإلكتروني فقط بدون ال Domain
في السطر الثالث قم بطباعة ال Top Level Domain الموجود بعد ال "Dot
"""
from icecream import ic
mail = input("Entre your mail : ").lower()
username = mail[:mail.index('@')]
domain = mail[mail.index('@')+1:mail.index('.')]
top_level = mail[mail.index('.')+1:]
ic(username.capitalize())
ic(domain)
ic(top_level)

# Entre your mail : Osama@Nn.Sa
# ic| username.capitalize(): 'Osama'
# ic| domain: 'nn'
# ic| top_level: 'sa'

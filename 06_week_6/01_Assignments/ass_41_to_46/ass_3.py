"""
التكليف 03
قم بعمل Input يقبل منك العمر الخاص بالشخص
تأكد أن المدخل عبارة عن Integer
المطلوب طباعة عمرك بالشهور والأسابيع والأيام والساعات والدقائق والثواني
المطلوب طباعة كل وحدة من وحدات الوقت في سطر منفصل
يجب التأكد من أن العمر أكبر من 10 وأقل من 100 وفي حالة غير ذلك إطبع رسالة تفيد أن العمر خارج النطاق.
"""
from icecream import ic


age = int(input("Enter age : ").strip())

if age in range(11,100):
    print(f"Your Age In Months Is {age * 12} Months")
    print(f"Your Age In Weeks Is {(age * 12) * 4}  Weeks")
    print(f"Your Age In Days Is {((age * 12) * 4)*7}  Days")
    print(f"Your Age In Hours Is {(((age * 12) * 7)*24)}  Hours")
    print(f"Your Age In Minutes Is {((((age * 12) * 7)*24)*60)}  Minutes")
    print(f"Your Age In Seconds Is {(((((age * 12) * 7)*24)*60)*60)}  Seconds")
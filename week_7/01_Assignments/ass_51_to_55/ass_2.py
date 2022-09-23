"""
التكليف 02
قم بعمل Loop يطبع الأرقام من 1 إلى 20
إذا كان الرقم أقل من 10 ضع قبله صفر
قم بإستثناء الأرقام 6 و 8 و 12
قم بطباعة رسالة تفيد إنتهاء ال Loop بنجاح
"""
for num in range(1, 21):
    if num < 10 and (num not in [6, 8]):
        print(f"{str(num).zfill(2)}")
    elif num not in [6, 8, 12]:
        print(num)
else:
    print("All Numbers Printed")

# Needed Output
"01"
"02"
"03"
"04"
"05"
"07"
"09"
"10"
"11"
"13"
"14"
"15"
"16"
"17"
"18"
"19"
"20"
"All Numbers Printed"

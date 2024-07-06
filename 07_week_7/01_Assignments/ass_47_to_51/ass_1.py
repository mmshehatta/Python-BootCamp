"""
التكليف 01
قم بعمل متغير بإسم num عبارة عن Input يقبل من الشخص رقم معين
تأكد أن الرقم نوعه Int وأنه أكبر من 0 وإذا لم يكن أكبر من 0 قم بطباعة رسالة تفيد ذلك
بعد إدخال الرقم قم بطباعة الرقم الأصغر منه مباشرة فالأصغر فالأصغر حتى تصل لرقم 1
يجب عدم طباعة الرقم نفسه وعدم طباعة رقم 0
إذا كانت الأرقام تحتوي على رقم 6 لا تطبعه من ضمن الأرقام
بعد الإنتهاء من طباعة الأرقام قم بطباعة رسالة تفيد أن طباعة جميع الأرقام تمت بنجاح مع كتابة كم عدد الأرقام التي تم طباعتها

"""

num = int(input("Enter number : "))

# be sure that num is int
if type(num) == int:
    print("num is integer number")

# be sure that number is more than 0
if num == 0:
    print(f"Number {num} Is Not Lager Than 0")

else:
    counter = 0
    while num > 1:  # this condition not print num 0
        num -= 1  # here num impossible to equal the original num after sub opt
        if not (num == 6):
            print(num)
            counter += 1
    else:
        print(f"[{counter}] Numbers Printed Successfully.")

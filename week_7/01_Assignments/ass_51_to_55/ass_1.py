"""
التكليف 01
دينا قائمة List من الأرقام
نريد عمل Loop عليهم لنستخرج الأرقام التي تقبل القسمة على رقم 5 ويرجع عدد صحيح
نريد طباعة ترتيب الأرقام تلقائيا قبل كل رقم فيهم
نريد طباعة الارقام من الأكبر للأصغر
قم بطباعة رسالة تفيد إنتهاء ال Loop بنجاح

"""

# Input
my_nums = [15, 81, 5, 17, 20, 21, 13]
my_nums.sort()
my_nums.reverse()
# print(my_nums)
c = 1
for num in my_nums:
    if num % 5 == 0:
        print(f"{c} = > {num}")
        c += 1
else:
    print("All Numbers Printed")

# Needed Output
# "1 => 20"
# "2 => 15"
# "3 => 5"
# "All Numbers Printed"

"""
التكليف 04
قم بعمل Input يطلب منك إسم الشخص الذي تريد إضافته للقائمة
إذا كان إسم الشخص كاملا عبارة عن حروف كبيرة Uppercase قم برفض الشخص وإظهار رسالة تفيد أن الإسم غير صالح
إذا كان الإسم كله حروف صغيرة قم بتحويل أول حرف فقط لحرف كبير ثم قم بإضافته للقائمة
بعد إضافة الإسم تطبع معه رسالة تفيد أنك قمت بتحويل أول حرف لحرف كبير
يجب طباعة إسم الشخص مع الرسالة الخاصة بالإضافة
في حالة قام الشخص بكتابة إسم وأول حرف فيه كبير قم بإضافته مباشرة وإطبع رسالة تفيد الإضافة
في حالة تم إضافة الإسم ومازال هناك مكان آخر في القائمة قم بإظهار ال Input ليقوم بإضافة إسم آخر حتى تمتليء القائمة
مع كل إضافة قم بكتابة رسالة تفيد كم عدد الأسماء المتبقية في القائمة قبل أن تمتليء
كل إسم يتم إضافته يجب أن يتم إزالة المسافات من قبله وبعده إن وجدت

"""
my_friends = []
max_num_of_friends = 4
# Input
while max_num_of_friends > 0:
    name = input("Enter Name : ").strip()
    if name.isupper():
        print("Invalid Name")
    elif name.islower():
        name = name.title()
        my_friends.append(name)
        print("We change the name to be first letter in upper case")
        max_num_of_friends -= 1
        print(f"{name} is added to my friends , {max_num_of_friends} place left")
    elif name.istitle():
        my_friends.append(name)
        max_num_of_friends -= 1
        print(f"{name} is added to my friends , {max_num_of_friends} place left")
else:
    print(my_friends)

# Needed Output
# Enter Name : OSama
# Enter Name : OSAMA
# Invalid Name
# Enter Name : mahmoud
# We change the name to be first letter in upper case
# Mahmoud is added to my friends , 3 place left
# Enter Name : eman
# We change the name to be first letter in upper case
# Eman is added to my friends , 2 place left
# Enter Name : habeba
# We change the name to be first letter in upper case
# Habeba is added to my friends , 1 place left
# Enter Name : ali
# We change the name to be first letter in upper case
# Ali is added to my friends , 0 place left
# ['Mahmoud', 'Eman', 'Habeba', 'Ali']
#
# Process finished with exit code 0

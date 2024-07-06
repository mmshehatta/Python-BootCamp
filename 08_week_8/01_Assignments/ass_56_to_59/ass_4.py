# التكليف 04
# قم بعمل Function تقوم بطباعة رسالة ترحيب للشخص
# ال Function تطلب منك ثلاثة Parameters وهم إسم الشخص وسنه وبلده
# إذا لم يكتب الشخص أي بيانات تظهر رسالة إفتراضية

def say_hello(name="Unkwon", age="Unknown",country="Unknown"):
    return (f"Hello {name} Your age  is {age} and your country is {country}")


print(say_hello("Osama", 38, "Egypt"))
print(say_hello())

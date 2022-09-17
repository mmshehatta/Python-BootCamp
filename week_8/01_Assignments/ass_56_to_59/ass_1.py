# التكليف 01
# قم بعمل Function تقوم بعمل عمليات حسابية بإسم calculate
# العمليات الحسابية هي الجمع والطرح والقسمة
# ال Function تقبل ثلاثة Parameters الرقم الأول والرقم الثاني ونوع العملية الحسابية وقم بتسميتهم كما تريد
# كل ما عليك هو تنفيذ العملية الحسابية بناء على المدخلات
# في حالة قام الشخص بكتابة نوع العملية الحسابية خطأ تظهر له رسالة أنه لا توجد هذه العملية
# العمليات الحسابية المتاحة هي add, subtract, multiply
# يمكن للشخص أن يكتب العملية الحسابية بحروف كبيرة أو صغيرة او Mix بدون مشكلة. مثلا add, ADD, aDd
# يمكن للشخص كتابة أول حرف فقط من العملية الحسابية فمثلا subtract يمكن أن يكتب S أو s
# إذا لم يكتب الشخص العملية الحسابية نهائيا قم بعمل العملية الإفتراضية وهي الجمع

def calculate(n1, n2, opt="add"):
    if opt.lower() in ("add", "a"):
        return n1 + n2
    elif opt.lower() in ("subtract", "s"):
        return n1 - n2
    elif opt.lower() in ("multiply", "m"):
        return n1 * n2
    else:
        print("This operation not found")
        return n1 + n2


# Tests
print(calculate(10, 20))  # 30
print(calculate(10, 20, "AdD"))  # 30
print(calculate(10, 20, "a"))  # 30
print(calculate(10, 20, "A"))  # 30
#
print(calculate(10, 20, "S"))  # -10
print(calculate(10, 20, "subTRACT"))  # -10
#
print(calculate(10, 20, "Multiply"))  # 200
print(calculate(10, 20, "m"))  # 200

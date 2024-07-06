# التكليف 02
# قم بعمل ال Function المناسبة التي تخرج جميع المخرجات الموجودة في الأمثلة التالية
# لدينا بيانات جديدة وهي إسم الشخص
# البيانات يمكن أن تزيد أو تنقص
# إذا لم يتم كتابة الإسم لا تظهر السطر الترحيبي الأول
# إذا لم يكن لديه مهارات قم بإظهار رسالة تفيد أنه لا يوجد لديه Score كما في المثال


def get_people_scores(name=None , **kwargs):
    if name and kwargs:
        print(f"Hello {name} This Is Your Score Table:")
        for k,v in kwargs.items():
            print(f"{k} => {v}")
    elif not name and kwargs:
        for k,v in kwargs.items():
            print(f"{k} => {v}")
    else:
        print(f"Hello {name} You Have No Scores To Show")

# Test1
get_people_scores("Osama", Math=90, Science=80, Language=70)

# Test 2
get_people_scores("Mahmoud", Logic=70, Problems=60)

# Test 3
get_people_scores(Logic=70, Problems=60)

# Test 4
get_people_scores("Ahmed")
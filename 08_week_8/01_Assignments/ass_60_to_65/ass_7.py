# التكليف 03
# قم بعمل ال Dictionary الذي يحتوي على البيانات التالية
# قم بعمل ال Function المناسبة التي تخرج جميع المخرجات الموجودة في الأمثلة التالية
# إذا لم يتم كتابة الإسم لا تظهر السطر الترحيبي الأول
# إذا لم يكن لديه مهارات قم بإظهار رسالة تفيد أنه لا يوجد لديه Score كما في المثال
from ass_6 import get_people_scores
scores_list={
    "Math" : 90,
    "Science":80,
    "Language" : 70
}
print("^"*10)
# Test 1
get_people_scores("Osama", **scores_list)

# Test 2
get_people_scores("Osama")

# Test 3
get_people_scores(**scores_list)
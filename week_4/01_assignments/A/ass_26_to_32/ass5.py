"""
Ass5
-----
قم بإنشاء Dictionary يحتوي على ثلاث مهارات برمجية مع النسبة المئوية لمستواك فيهم
بدون إستخدام ال Loop قم بطباعة كل مهارة في سطر وبجانبها المستوى المكتوب بالنسبة المئوية
قم بإضافة مهارة جديدة لل Dictionary مع النسبة المئوية الخاصة بها ثم قم بطباعتها في السطر الخامس

Refs:
"""
my_skills = {
    1: ("HTML", "50%"),
    2: ("CC", "60%"),
    3: ("Js", "70%"),
}
print(f"{my_skills.get(1)[0]} Progress Is {my_skills.get(1)[1]}")
print(f"{my_skills.get(2)[0]} Progress Is {my_skills.get(1)[1]}")
print(f"{my_skills.get(3)[0]} Progress Is {my_skills.get(1)[1]}")
my_skills[4] = ("Django", "80%")
print(f"{my_skills.get(4)[0]} Progress Is {my_skills.get(1)[1]}")
# Needed Output
# HTML Progress Is 50%
# CC Progress Is 50%
# Js Progress Is 50%
# Django Progress Is 50%

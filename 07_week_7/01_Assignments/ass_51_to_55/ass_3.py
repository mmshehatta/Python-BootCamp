"""
التكليف 03
لديك قاموس يحتوي على المواد العلمية الخاصة بك وال Rank الذي حصلت عليه
كل قيمة من القيم في ال Rank تساوي نقاط معينة
ال A تساوي 100 وال B تساوي 80 وال C تساوي 40
قم بإستخدام ما تعلمته سابقا لتخرج بالنتيجة التالية بدون التعديل على القاموس الأصلي
قم بطباعة مجموع النقاط في النهاية بعد إنتهاء ال Loop
"""

# Input
my_ranks = {
    'Math': 'A',
    "Science": 'B',
    'Drawing': 'A',
    'Sports': 'C'
}
a_points, b_points, c_points = 0, 0, 0

for k, v in my_ranks.items():
    if v == "A":
        a_points += 100
        if a_points > 100:
            a_points = 100
        print(f"My Rank in {k} Is A And This Equal {a_points} Points")
    elif v == "B":
        if b_points > 80:
            b_points += 80
        print(f"My Rank in {k} Is B And This Equal {b_points} Points")
    elif v == "C":
        if c_points > 40:
            c_points += 40
        print(f"My Rank in {k} Is C And This Equal {c_points} Points")
else:
    print(f"Total Points Is {a_points + b_points + c_points}")
# Needed Output
"My Rank in Math Is A And This Equal 100 Points"
"My Rank in Science Is B And This Equal 80 Points"
"My Rank in Drawing Is A And This Equal 100 Points"
"My Rank in Sports Is C And This Equal 40 Points"
"Total Points Is 320"

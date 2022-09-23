"""
التكليف04
لديك قاموس يحتوي على أسماء الطلبة وكل طالب لديه مجموعة من المواد العلمية ودرجاته فيها
كل قيمة من القيم في ال Rank تساوي نقاط معينة
ال A تساوي 100 وال B تساوي 80 وال C تساوي 40 وال D تساوي 20
قم بإستخدام ما تعلمته سابقا لتخرج بالنتيجة التالية بدون التعديل على القاموس الأصلي
يجب عليك طباعة المخرجات كما هي بالعلامات بكل شيء
قم بعمل الحل مرة بطريقة عادية ومرة أخرى بإستخدام ال items()
"""

# Input
students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}
a_points, b_points, c_points, d_points = 0, 0, 0, 0
for k, v in students.items():
  print("------------------------------")
  print(f"-- Student Name => {k}")
  for k2, v2 in v.items():
    if v2 == "A":
      a_points += 100
      if a_points > 100:
        a_points = 100
      print(f"- {k2} => {a_points} Points")
    if v2 == "B":
      b_points += 80
      if b_points > 80:
        b_points = 80
      print(f"- {k2} => {b_points} Points")
    if v2 == "C":
      c_points += 60
      if c_points > 60:
        c_points = 60
      print(f"- {k2} => {c_points} Points")
    if v2 == "D":
      d_points += 20
      if d_points > 20:
        d_points = 20
      print(f"- {k2} => {d_points} Points")
  else:
    if k == "Mahmoud":
      print(f"Total Points For Mahmoud Is {a_points + b_points + c_points + d_points}")

# Needed Output
"------------------------------"
"-- Student Name => Ahmed"
"------------------------------"
"- Math => 100 Points"
"- Science => 20 Points"
"- Draw => 80 Points"
"- Sports => 40 Points"
"- Thinking => 100 Points"
"Total Points For Ahmed Is 340"
"------------------------------"
"-- Student Name => Sayed"
"------------------------------"
"- Math => 80 Points"
"- Science => 80 Points"
"- Draw => 80 Points"
"- Sports => 20 Points"
"- Thinking => 100 Points"
"Total Points For Sayed Is 360"
"------------------------------"
"-- Student Name => Mahmoud"
"------------------------------"
"- Math => 20 Points"
"- Science => 100 Points"
"- Draw => 100 Points"
"- Sports => 80 Points"
"- Thinking => 80 Points"
"Total Points For Mahmoud Is 380"

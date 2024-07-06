"""
التكليف 02
قم بإنشاء قائمة فيها خمس من أصدقائك ثم تأكد أن فيهم إسمين على الأقل مكتوبين بحروف صغيرة والباقي أول حرف من الإسم Capital
قم بإستخدام While Loop لطباعة الأسماء كلها مع تجاهل الأسماء التي تبدأ بحروف صغيرة
قم بطباعة عدد الأسماء التي تم تجاهلها ويجب أن تكون بطريقة برمجية وليست يدوية
"""

# Input
friends = ["Mohamed", "Shady", "ahmed", "eman", "Ali"]
counter = 0
for name in friends:
    if name.islower():
        counter += 1
else:
    if counter >= 2:
        print("This list has min 2 name in lower cases")
    else:
        print("This list has less than  2 names in lower cases")
print("*" * 50)
index, ignored = (0, 0)
while index < len(friends):
    if friends[index].istitle():
        print(friends[index])
    else:
        ignored += 1
    index += 1
else:
    print(f"Friends Printed And Ignored Names Count Is {ignored}")

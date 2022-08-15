"""
التكليف 01
قم بعمل متغيرين بإسم num1, num2 ويكونوا Input يحتوي على الرقم الأول والثاني
قم بعمل متغير ثالث بإسم operation يكون عبارة عن Input يحتوي على نوع العملية الحسابية
قم بالتأكد من أن متغيرات الأرقام عبارة عن Integer ولا يوجد مسافات قبلهم ولا بعدهم
قم بالتأكد أن المتغير الخاص بالعملية الحسابية لا توجد مسافات قبله ولا بعده
قم بجلب الرقم الأول والثاني والعملية الحسابية من المدخلات ثم قم بالعملية بناء على الأرقام والعملية الحسابية سواء كانت + – * / %
"""

from icecream import ic

# Inputs

num1 = 20
num2 = 40
# operation = "+" Or "-" Or "*" Or "/" Or "%"

num1 = int(input("enter num1: ").strip())
num2 = int(input("enter num2: ").strip())
opt = input("enter opt: ").strip()

if opt=="+":
    print(f"[num1 {num1}] [operation {opt}] [num2 {num2}]")
    print(f"{num1}{opt}{num2} = {num1+num2}")
elif opt=="-":
    print(f"[num1 {num1}] [operation {opt}] [num2 {num2}]")
    print(f"{num1}{opt}{num2} = {num1-num2}")
elif opt=="*":
    print(f"[num1 {num1}] [operation {opt}] [num2 {num2}]")
    print(f"{num1}{opt}{num2} = {num1*num2}")
elif opt=="/":
        print(f"[num1 {num1}] [operation {opt}] [num2 {num2}]")
        print(f"{num1}{opt}{num2} = {num1/num2}")
else:
    print(f"[num1 {num1}] [operation {opt}] [num2 {num2}]")
    print(f"{num1}{opt}{num2} = {num1%num2}")
# Needed Output

# [num1 20] [operation +] [num2]
# Example One 20 + 40 = 60
# Example Two 20 * 40 = 800

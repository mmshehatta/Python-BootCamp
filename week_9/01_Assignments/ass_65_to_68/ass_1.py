# التكليف 01
# قم بإنشاء مجلد بإسم Python على سطح المكتب ثم إنشيء بداخله ملف بإسم assign.py ثم قم بفتحه
# قم بإنشاء 50 Text بإسم txt1 و txt2 و txt3 حتى txt50 داخل المجلد Python بطريقة برمجية
# قم بكتابة جملة Elzero Web School => {File Number} ومكان File Number أكتب رقم الملف
# تأكد أن الملف رقم 25 بإسم تقوم بتسميته special-text ويكون فارغ بدون أي كتابة داخله
# في السطر الأول قم بطباعة ال Current Working Directory
# في السطر الثاني قم بطباعة المسار الموجود فيه الملف حاليا
# في السطر الثالث قم بطباعة إسم الملف المفتوح حاليا
# في السطر الرابع قم بطباعة مجموع الملفات الموجودة داخل المجلد Python
import os

for i in range(1, 4):
    if i == 2:
        with open(f"file_{i}_sp-text.txt", "w") as f:
            f.write(f"cwd: {os.getcwd()}\n")
            f.write(f"file path: {os.path.abspath(__file__)}\n")
            f.write(f"open file name: {os.path.basename(os.path.abspath(__file__))}\n")
            f.write(f"#files: {len([name for name in os.listdir('.') if os.path.isfile(name)])}\n")
    else:
        with open(f"file_{i}.txt", "w") as f:
            f.write(f"Elzero Web School => {i}\n")

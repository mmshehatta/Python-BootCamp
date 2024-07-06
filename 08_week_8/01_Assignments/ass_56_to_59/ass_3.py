# التكليف 03
# قم بعمل Function تقوم بطباعة بيانات عن الشخص ومهاراته
# ال Function تقبل منك إسم الشخص وبعده عدد غير معلوم من المهارات
# كل ما عليك هو طباعة رسالة ترحيبية بالشخص ثم طباعة مهاراته تحت الإسم
# إذا لم يكن لديه مهارات يجب عليك إظهار رسالة تفيد أنه ليس لديه مهارات حتى الآن

def show_skills(name, *skills):
    if skills:
        print(f'Hello {name} Your Skills Is:')
        for s in skills:
            print(f" - {s} ")
    else:
        print(f"Hello {name} You Have No Skills To Show")


# show_skills("Osama", "HTML", "CSS", "JS", "Python")
# show_skills("Ahmed")


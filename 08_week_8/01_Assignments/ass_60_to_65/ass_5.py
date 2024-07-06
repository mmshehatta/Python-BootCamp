# التكليف 01
# قم بعمل ال Function المناسبة التي تخرج جميع المخرجات الموجودة في الأمثلة التالية
# البيانات يمكن أن تزيد أو تنقص

def get_score(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} => {v}")

get_score(Math=90, Science=80, Language=70)
get_score(Logic=70, Problems=60)

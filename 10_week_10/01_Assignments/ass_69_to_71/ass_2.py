# التكليف 02
# ما هي قيمة v التي تجعل الطباعة تخرج الرقم 820
from icecream import ic
v = 40

my_range = list(range(v))
ic(my_range)
ic(sum(my_range, v) ) #ic| sum(my_range, v): 820
ic(pow(v,v,v)) #ic| pow(v,v,v): 0

print(sum(my_range, v) + pow(v, v, v))  # 820
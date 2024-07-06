# التكليف 03
# =================
from icecream import ic
n = 20

l = list(range(n))
ic(l)
ic(sum(l))
ic( max(0, 3, 10, 2, -100, -23, 9))
ic((sum(l) / n)) #ic| sum(l) / n: 9.5
ic(round(sum(l) / n))

if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

  print("Gooood")

# Output => Good

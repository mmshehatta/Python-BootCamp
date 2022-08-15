# 00 Lesson
# >> 03 Data Types
# >> 06 Boolean
# >> 034_boolean_operators.py

from icecream import ic

# -----------------
# --- Boolean----
# -----------------

# and operator:
age, country, rank = (25, "Egypt", 10)

ic(age == 25 and country == "Egypt" and rank == 10)
# ic| age == 25 and country == "Egypt" and rank==10: True


# or operator:
ic(age == 25 and country == "KSA" and rank == 20)
# ic| age == 25 and country == "KSA" and rank==20: False
ic(age == 25 or country == "KSA" or rank == 20)
# ic| age == 25 or country == "KSA" or rank==20: True


# not operator:
ic(age > 20)  # ic| age > 20: True
ic(not age > 20)  # ic| not age > 20: False

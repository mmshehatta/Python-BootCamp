# التكليف 01
# ============

values = (0, 1, 2)

if any(values):
    my_var = 0

my_list = [True, 1, 1, ["A", "B"], 10.5, my_var]

if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

    print("Good")

else:

    print("Bad")

# Output:
# Good

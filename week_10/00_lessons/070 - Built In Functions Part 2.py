# ------------------------
# -- Built In Functions --
# ------------------------
# all()
# any()
# bin()
# id()
# ------------------------

x = [1, 2, 3, 4, []]
print("*" * 30)
if all(x):

    print("All Elements Is True")

else:

    print("Theres At Least One Element Is False")

x = [0, 0, []]

if any(x):

    print("There's At Least One Element is True")

else:

    print("Theres No Any True Elements")

print(bin(100))

a = 1
b = 2

print(id(a))
print(id(b))

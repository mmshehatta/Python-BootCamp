
# variables
num = "1200"

# Processing


def zfil_string(num):
    return f"{num.zfill(4)}"


print(zfil_string("9"))
print(zfil_string("15"))
print(zfil_string("130"))
print(zfil_string("950"))
print(zfil_string("1500"))

# output
# 0009
# 0015
# 0130
# 0950
# 1500

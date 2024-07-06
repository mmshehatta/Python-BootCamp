# التكليف 06
# ==========

friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]


def get_names(name):
    return True if name.endswith("m") else False

names = list(filter(get_names, friends_filter))

# for name in names:
#     print(name)

# Output
"Wessam"
"Essam"


# with lambda function:
names2 = filter(lambda name : name.endswith("m"),friends_filter)
for name in names2:
    print(name)



# Output
"Wessam"
"Essam"
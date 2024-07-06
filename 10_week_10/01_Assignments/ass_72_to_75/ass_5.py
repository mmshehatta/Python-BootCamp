# التكليف 05
# ==========

def remove_chars(str):
    return str[1:len(str) - 1]

friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

cleaned_list = map(remove_chars,friends_map)

for name in cleaned_list:
    print(name)


# with lambda function:
cleaned_list2 = map(lambda str: str[1:len(str)-1] ,friends_map)
for name in cleaned_list2:
    print(name)

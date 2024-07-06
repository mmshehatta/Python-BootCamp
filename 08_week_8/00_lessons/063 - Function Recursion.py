# ------------------------
# -- Function Recursion --
# ------------------------
# ---------------------------------------------------------------------
# -- To Understand Recursion, You Need to First Understand Recursion --
# ---------------------------------------------------------------------
# Reading list:
# 1.https://www.w3schools.com/python/gloss_python_function_recursion.asp `easy`
# 2.https://www.programiz.com/python-programming/recursion `medium`
# 3.https://realpython.com/python-recursion/(hard or detailed)

# Test Word [ WWWoooorrrldd ] # print(x[1:])

def clean_word(word):
    if len(word) == 1:
        return word

    print(f"Print Start Function {word}")

    if word[0] == word[1]:
        print(f"Print Before Condition {word}")

        return clean_word(word[1:])

    print(f"Print Before Return {word}")

    return word[0] + clean_word(word[1:])

    # Stash [ World ]


print(clean_word("WWWoooorrrldd"))

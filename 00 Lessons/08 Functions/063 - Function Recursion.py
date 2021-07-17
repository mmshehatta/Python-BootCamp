

# >> 00 Lesson
# >> 08 Functions
# >>063 - Function Recursion.py
from icecream import ic
# ----------------------------------------------------------------
# --- 063 - Function Recursion.py ----
# ---------------------------------------------------------------
# ----------------------------------------------------------------
# ---  TO understand Recuresion , Understand Recuresion ...hahahhah  دور بنفسك جو نفسك
# ---------------------------------------------------------------
# explain by example:

def clean_word(word):
    if len(word) == 1:
        return word
    print(f" print start fun: {word}")

    if(word[0] == word[1]):
        print(f" print after conditon: {word}")
        return clean_word(word[1:])

    print(f"print before return {word}")

    return word[0]+clean_word(word[1:])


ic(clean_word("wwwoorrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrld"))

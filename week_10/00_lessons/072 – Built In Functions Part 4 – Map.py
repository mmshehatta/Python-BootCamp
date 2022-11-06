# -------------------------------
# -- Built In Functions => Map --
# -------------------------------
# [1] Map Take A Function + Iterator
# [2] Map Called Map Because It Map The Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function
# ---------------------------------------------------------------

# Use Map With Predefined Function

def formatText(text):
    return f"- {text.strip().capitalize()} -"


myTexts = [" OSama ", "AHMED", "  sAYed  "]

myFormatedData = map(formatText, myTexts)

print(myFormatedData)

for name in list(map(formatText, myTexts)):
    print(name)

print("#" * 50)


# Use Map With Lambda Function

def formatText(text):
    return f"- {text.strip().capitalize()} -"


myTexts = [" OSama ", "AHMED", "  sAYed  "]

for name in list(map((lambda text: f"- {text.strip().capitalize()} -"), myTexts)):
    print(name)

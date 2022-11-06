# ----------------------------------
# -- Built In Functions => Filter --
# ----------------------------------
# [1] Filter Take A Function + Iterator
# [2] Filter Run A Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function
# [4] Filter Out All Elements For Which The Function Return True
# [5] The Function Need To Return Boolean Value
# ---------------------------------------------------------------

# Example 1

def checkNumber(num):
    return num > 10


myNumbers = [0, 0, 1, 19, 10, 20, 100, 5, 0]

myResult = filter(checkNumber, myNumbers)

for number in myResult:
    print(number)

print("#" * 50)


# Example 2

def checkName(name):
    return name.startswith("O")


myTexts = ["Osama", "Omer", "Omar", "Ahmed", "Sayed", "Othman"]

myReturnedData = filter(checkName, myTexts)

for person in myReturnedData:
    print(person)

print("#" * 50)

# Example 3

myNames = ["Osama", "Omer", "Omar", "Ahmed", "Sayed", "Othman", "Ameer"]

for p in filter(lambda name: name.startswith("A"), myNames):
    print(p)

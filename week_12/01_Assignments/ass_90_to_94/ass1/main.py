# algorithm:
# 1. This code asks the user to input a number.
# 2. The code then checks if the number is longer than one character, and if so, it raises an IndexError.
# 3. If the number is equal to zero, the code raises a ValueError.
# 4. If the number is not an integer, it raises an Exception. 
# 5. Finally, if all these checks pass, the code prints out the number that was entered by the user.

NUM = input("Add Your Number : ")
# Your Code Here
if len(NUM) > 1:
    raise IndexError("Only One Character Allowed")
elif NUM == "0":
    raise ValueError("Number Must Be Larger Than 0")
elif NUM.lower().isalpha:
    raise Exception("Only Numbers Allowed")
else :
    print(f"The Number Is {NUM}")

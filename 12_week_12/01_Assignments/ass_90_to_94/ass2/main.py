# algorithm:
# The program starts by prompting the user to input a letter from "A" to "Z" and assigns the input to a variable called LETTER.
# The program then enters a try block.
# Inside the try block, the program checks if the length of the input LETTER is greater than 1.
# If the length of LETTER is greater than 1, the program raises a ValueError exception with the message "Invalid value".
# If the length of LETTER is not greater than 1, the program then checks if the input LETTER is not between "A" and "Z" (inclusive) when converted to uppercase.
# If the input LETTER is not between "A" and "Z" (inclusive) when converted to uppercase, the program raises an IndexError exception with the message "Invalid value".
# If the input LETTER is between "A" and "Z" (inclusive) when converted to uppercase, the program continues to the else block.
# In the else block, the program prints a message "You Typed {LETTER}"
# If a ValueError exception is raised in the try block, the program enters the except ValueError block and prints "You Must Write One Character Only"
# If an IndexError exception is raised in the try block, the program enters the except IndexError block and prints "The Letter Not In A - Z"
# If no exception is raised in the try block, the program continues to the else block.
# The program exits.


LETTER = input("Add Letter From A to Z : ")

# Your Code Here
try:
   if len(LETTER) > 1:
       raise ValueError("Invalid value")
   if not(LETTER.upper()>="A" and LETTER.upper()<="Z"):
         raise IndexError("Invalid value")
except ValueError:
    print("You Must Write One Character Only")
except IndexError:
    print("The Letter Not In A - Z")
else:
   print(f"You Typed {LETTER}") 



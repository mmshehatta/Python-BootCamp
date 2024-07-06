# -----------------------------------------------
# -- File Handling => Write and Append In File --
# -----------------------------------------------

myFile = open("myfile.txt", "w")
myFile.write("Hello\n")
myFile.write("Third Line")

myFile = open(r"D:\Python\Files\fun.txt", "w")
myFile.write("Elzero Web School\n" * 1000)

myList = ["Oasma\n", "Ahmed\n", "Sayed\n"]

myFile = open("myfile.txt", "w")
myFile.writelines(myList)

myFile = open("myfile.txt", "a")
myFile.write("Elzero")

# --------------------------------
# -- File Handling => Read File --
# --------------------------------
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
myFile = open("myfile.txt", "r")

print(myFile)  # File Data Object
print(myFile.name)
print(myFile.mode)
print(myFile.encoding)

print(myFile.read())
print(myFile.read(5))

print(myFile.readline(5))
print(myFile.readline())
print(myFile.readline())

print(myFile.readlines())
print(myFile.readlines(50))
print(type(myFile.readlines()))

for line in myFile:

    print(line)

    if line.startswith("07"):
        break

# Close The File

myFile.close()

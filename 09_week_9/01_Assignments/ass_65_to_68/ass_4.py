# التكليف 04
import os

# os.chdir(os.path.dirname())
print("+" * 30)
files = [name for name in os.listdir('.') if os.path.isfile(name)]
print(len(files))
files.sort()
print(type(files))
for i in files:
    print(i)
    os.remove(i)



def reverse_string(my_string):
      # Your Code Here
      length = len(my_string)
      for i in range(length - 1 , -1 , -1):
            yield my_string[i]

print("*" * 30)

# Reverse The String
for c in reverse_string("Elzero"):
  print(c)
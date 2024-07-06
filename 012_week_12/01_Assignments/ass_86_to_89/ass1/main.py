my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []
final_string = ""
for data in zip(my_list, my_tuple):
  # Write Your Code Here
  final_string += "".join(data)
  final_string  = final_string.lower().title()

print(final_string) # Elzero
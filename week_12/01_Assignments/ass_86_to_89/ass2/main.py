# Algorithm:
# 1. Initialize an empty list my_data
# 2. Loop through the elements of three lists (my_list1, my_tuple, my_list2) and append each combination to the list my_data 
# 3. Create a variable final_string and assign it an empty string
# 4. Join all the elements of my_data into a single string and assign it to final_string
# 5. Create a result variable and assign it to a sorted set of only alphabetical characters from final_string 
# 6. Join the characters in result into a single string and convert it to lowercase title format 
# 7. Print out the value of final_string

my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []

for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
    # Write Your Code Here
    final_string = ""
    my_data.append(str(item1) + str(item2) + str(item3))
    final_string += "".join(my_data)
    return_alpha_and_remove_duplicates = set([x for x in final_string if x.isalpha()]) 
    # print(remove_duplicates)
    sorted_result = "".join(sorted(return_alpha_and_remove_duplicates, key=final_string.index))
    final_string = sorted_result.lower().title()
print(final_string)



# explaintion of this line :
# result = ''.join([i for i in string if i.isalpha()])
#  This line of code is using list comprehension to create a new string (called "result") by joining all the
#  characters in the original string (called "string") that are alphabetical characters. The isalpha()
# method checks if each character in the string is an alphabetic character, and if so, it adds it to the new "result" string.

#Explaintion of this code : result = "".join( sorted(set(''.join([x for x in final_string if x.isalpha()])), key=final_string.index ))
# This code takes a string(final_string) and creates a new string(result) by first removing
#  all non-alphabetical characters from the original string, sorting the remaining characters alphabetically,
#  and then joining them back together. The key parameter is used to ensure that the characters are sorted in 
# the same order as they appeared in the original string.

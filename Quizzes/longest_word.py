test = "I love Python a lot ."
# method 1
print(max(test.split(),key=len))

# method 2
print(sorted(test.split() , key=len)[-1])

# method 3
print(sorted(test.split() , key=len , reverse=True)[0])
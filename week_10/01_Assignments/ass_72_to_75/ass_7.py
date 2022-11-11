# التكليف 07
# ==========

from functools import reduce
nums = [2, 4, 6, 2]

def mul_all(num1 , num2):
    return num1 * num2

multiplaction_result = reduce(mul_all,nums)
# print(multiplaction_result)

# Output
96


# with lambda function:
multiplaction_result2 = reduce(lambda num1 , num2: num1 * num2 , nums)
print(multiplaction_result2)

"""
Ass 1:
-----
قم بإنشاء Set جديدة تحتوي على الأرقام 1, 2, 3
قم بإنشاء Set جديدة تحتوي على الحروف A, B, C
قم بدمج ال Set الأولى والثانية بثلاث طرق مختلفة وإطبع كل طريقة في سطر

Refs:
https://www.delftstack.com/howto/python/how-to-join-two-sets-in-python/
"""
nums = {1, 2, 3}
letters = {"A", "B", "C"}
# method1
result = nums.union(letters)
print(result)

# method2:
nums |= letters
print(nums)

# method3:
nums.update(letters)
print(nums)

# Needed Output
# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}

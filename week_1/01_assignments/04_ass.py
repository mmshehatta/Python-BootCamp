#  قم بعمل Concatenate للمتغيرات مع بعض الكلمات لتخرج بهذه الرسالة الموجودة في ال Output التالي 
# "Hello, My Name Is Osama And Iam 38 Years Old and I Live in Egypt."


age = '25'
name ="mahmoud"
country = """Egypt"""


# method 1:
print("==== method1 ===")
print("Hello , my name is "+name+" and i'm "+age+" years old and i live in "+country)


# method2:
print("==== method2 ===")
print("My name is {0} and i'm {1} years old and i live in {2}".format(name,age,country))


# method3:
print("==== method3 ===")
print(f"My name is {name} and i'm {age} years old and i live in {country}")

# result:
# ==== method1 ===
# Hello , my name is mahmoud and i'm 25 years old and i live in Egypt
# ==== method2 ===
# My name is mahmoud and i'm 25 years old and i live in Egypt
# ==== method3 ===
# My name is mahmoud and i'm 25 years old and i live in Egypt


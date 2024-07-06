# التكليف 08
# ==========
# method : 1
# -------
print("=====  {{Method 1}} ======")
skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
skills = reversed(skills)

for i , value in enumerate(skills , 50 ):
    if type(value) == int:
        continue
    print(f" \"{i} - {value}\" ")


# Output
"50 - JavaScript"
"52 - Python"
"53 - PHP"
"55 - CSS"
"56 - HTML"

# method : 2
# -------
print("=====  {{Method 2}} ======")
skills2 = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
skills2 =skills2[::-1]
for i , value in enumerate(skills2 , 50 ):
    if type(value) == int:
        continue
    print(f" \"{i} - {value}\" ")
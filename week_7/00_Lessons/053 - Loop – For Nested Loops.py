# -----------------
# -- Loop => For --
# -- Nested Loop --
# -----------------

peoples = ["Osama", "Ahmed", "Sayed", "Ali"]

skills = ['Html', 'Css', 'Js']

for name in peoples:  # Outer Loop

  print(f"{name} Skills Is: ")

  for skill in skills:  # Inner Loop

    print(f"- {skill}")

# Dictionary

peoples = {
  "Osama": {
    "Html": "70%",
    "Css": "80%",
    "Js": "70%"
  },
  "Ahmed": {
    "Html": "90%",
    "Css": "80%",
    "Js": "90%"
  },
  "Sayed": {
    "Html": "70%",
    "Css": "60%",
    "Js": "90%"
  }
}

print(peoples["Osama"])
print(peoples["Ahmed"])
print(peoples["Sayed"])

print(peoples["Osama"]['Css'])
print(peoples["Ahmed"]['Css'])
print(peoples["Sayed"]['Css'])

for name in peoples:

  print(f"Skills and Progress For {name} Is: ")

  for skill in peoples[name]:

    print(f"{skill.upper()} => {peoples[name][skill]}")
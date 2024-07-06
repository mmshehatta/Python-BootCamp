# Create Your Decorator Here
def my_decorator(func):
    def wrapper():
        print("Sugar Added From Decorators")
        func()
        print("Ashrap ya m3lem :)")
        print("####################")
    return wrapper
        
@my_decorator
def make_tea():
  print("Tea Created")

@my_decorator
def make_coffe():
  print("Coffe Created")

print("*" * 30)
make_tea()
make_coffe()

# Needed Output

"Sugar Added From Decorators"
"Tea Created"
"####################"
"Sugar Added From Decorators"
"Coffe Created"
"####################"
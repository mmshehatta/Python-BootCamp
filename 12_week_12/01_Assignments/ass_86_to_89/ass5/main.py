""" Doc str ass 5 """
myFriends = ["Ahmed", "Osama", "Sayed"]

def say_hello(some_peoples) -> list:
    """method docstring """
    for some_one in some_peoples:
        print(f"Hello {some_one}")

say_hello(myFriends)

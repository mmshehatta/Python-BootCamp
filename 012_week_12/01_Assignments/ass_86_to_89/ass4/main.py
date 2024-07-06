# Write Function With Help To Get The Output
def say_hello_to(name):
    """
    parameter(someone) => Person Name
    Function To Say Hello To Anyone
    """
    return f"hello {name}"

print(say_hello_to("Osama")) # "Hello Osama"

# Write Doc String Line For The Function Here
print(say_hello_to.__doc__)
print(help(say_hello_to))

# Function Doc String Output
"parameter(someone) => Person Name"
"Function To Say Hello To Anyone"

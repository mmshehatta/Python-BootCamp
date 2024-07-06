import termcolor
import pyfiglet

# Test pyfiglet package.
print(pyfiglet.figlet_format("Mahmoud"))

# Test termcolor package.
print(termcolor.colored("Mahmoud" , color="green"))


# Test 2 package:
print(termcolor.colored(pyfiglet.figlet_format("Mahmoud"), color="green"))

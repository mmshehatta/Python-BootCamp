# 00 Lesson 
# >> 03 Data Types
# >> 00_Strings 
# >> 017_String_formatting_old_way.py
from icecream import ic

name ="mahmoud"
age=25
rank=10
# ic("My name is :"+name+ "and age is:"+age) #TypeError: can only concatenate str (not "int") to str

ic("My name is :%s and age is: %s" % (name,age)) #ic| "My name is :%s and age is: %s" % (name,age): 'My name is :mahmoud and age is: 25'
ic("My name is :%s and age is: %d" % (name,age)) #ic| "My name is :%s and age is: %d" % (name,age): 'My name is :mahmoud and age is: 25'
ic("My name is :%s and age is: %d and rank is :%f" % (name,age,rank)) #ic| "My name is :%s and age is: %d and rank is :%f" % (name,age,rank): 'My name is :mahmoud and age is: 25 and rank is :10.000000'
ic("My name is :%s and age is: %d and rank is :%d" % (name,age,rank)) #ic| "My name is :%s and age is: %d and rank is :%d" % (name,age,rank): 'My name is :mahmoud and age is: 25 and rank is :10'

name = "Mahmoud"
lang="python"
exp_year=10
ic("My  Name is :%s Iam %s Developer with %d year of Exp." % (name, lang , exp_year))#"My  Name is :%s Iam %s Developer with %s year of Exp." % (name, lang , exp_year): 'My  Name is :Mahmoud Iam python Developer with 10 year of Exp.'

# controling floating point num %f:
myNumber=10
ic("MyNumber is %d" % myNumber) #ic| "MyNumber is %d" % myNumber: 'MyNumber is 10'
ic("MyNumber is %f" % myNumber) #ic| "MyNumber is %f" % myNumber: 'MyNumber is 10.000000'
ic("MyNumber is %.2f" % myNumber) #ic| "MyNumber is %.2f" % myNumber: 'MyNumber is 10.00'
ic("MyNumber is %.1f" % myNumber) #ic| "MyNumber is %.1f" % myNumber: 'MyNumber is 10.0'
ic("MyNumber is %.0f" % myNumber) #ic| "MyNumber is %.0f" % myNumber: 'MyNumber is 10'


# Truncate string:
# --------------
MyLongString="Hello my friends in my course python for everybody"
ic("My Message Is:%s" % MyLongString)#ic| "My Message %s" % MyLongString: 'My Message Hello my friends in my course python for everybody'
ic("My Message Is:%.5s" % MyLongString)#ic| "My Message Is:%.5s" % MyLongString: 'My Message Is:Hello'
ic("My Message Is:%.2s" % MyLongString)#ic| "My Message Is:%.2s" % MyLongString: 'My Message Is:He'

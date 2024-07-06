# 00 Lesson 
# >> 03 Data Types
# >> 00_Strings 
# >> 018-Strings_Formatting _New_Ways.py
from icecream import ic

name ="mahmoud"
age=25
rank=10
# ic("My name is :"+name+ "and age is:"+age) #TypeError: can only concatenate str (not "int") to str

ic("My name is :{} and age is: {}".format(name,age)) #ic| "My name is :{} and age is: {}".format(name,age): 'My name is :mahmoud and age is: 25'

ic("My name is :{:s} and age is: {:d}".format(name ,age)) #ic| "My name is :%s and age is: %d" % (name,age): 'My name is :mahmoud and age is: 25'

ic("My name is :{:s} and age is: {:d} and rank is :{:f}".format(name , age , rank)) #ic| "My name is :{:s} and age is: {:d} and rank is :{:f}".format(name , age , rank): 'My name is :mahmoud and age is: 25 and rank is :10.000000'

ic("My name is :{:s} and age is: {:d} and rank is :{:.2f}".format(name,age,rank)) #ic| "My name is :{:s} and age is: {:d} and rank is :{:.2f}".format(name,age,rank): 'My name is :mahmoud and age is: 25 and rank is :10.00'

name = "Mahmoud"
lang="python"
exp_year=10
ic("My  Name is :{:s} Iam {:s} Developer with {:d} year of Exp.".format(name, lang , exp_year))#ic| "My  Name is :{:s} Iam {:s} Developer with {:d} year of Exp.".format(name, lang , exp_year): 'My  Name is :Mahmoud Iam python Developer with 10 year of Exp.'

# controling floating point num %f:
myNumber=10
ic("MyNumber is {:d}" .format(myNumber)) #ic| "MyNumber is {:d}" .format(myNumber): 'MyNumber is 10'
ic("MyNumber is {:f}".format(myNumber)) #ic| "MyNumber is {:f}".format(myNumber): 'MyNumber is 10.000000'
ic("MyNumber is {:.2f}".format(myNumber))  #ic| "MyNumber is {:.2f}".format(myNumber): 'MyNumber is 10.00'


# Truncate string:
# --------------
MyLongString="Hello my friends in my course python for everybody"
ic("My Message Is:{:s}".format(MyLongString) )#ic| "My Message Is:{:s}".format(MyLongString): 'My Message Is:Hello my friends in my course python for everybody'
ic("My Message Is:{:.5s}" .format(MyLongString) )#ic| "My Message Is:{:.5s}" .format(MyLongString): 'My Message Is:Hello'
ic("My Message Is:{:.2s}".format( MyLongString))#ic| "My Message Is:{:.2s}".format( MyLongString): 'My Message Is:He'



# format mony:
myBalance=500162350199
ic("My Balan ce in bank is {:d}:".format(myBalance))#ic| "My Balan ce in bank is {:d}:".format(myBalance): 'My Balan ce in bank is 500162350199:'
ic("My Balan ce in bank is {:_d}:".format(myBalance))#ic| "My Balan ce in bank is {:_d}:".format(myBalance): 'My Balan ce in bank is 500_162_350_199:'
ic("My Balan ce in bank is {:,d}:".format(myBalance))#ic| "My Balan ce in bank is {:,d}:".format(myBalance): 'My Balan ce in bank is 500,162,350,199:'

# Rearrang items:
a,b,c = "one","two","three"
ic("hello {} {} {}".format(a,b,c))#ic| "hello {} {} {}".format(a,b,c): 'hello one two three'
ic("hello {1} {2} {0}".format(a,b,c))#ic| "hello {1} {2} {0}".format(a,b,c): 'hello two three one'
ic("hello {2} {1} {0}".format(a,b,c))#ic| "hello {2} {1} {0}".format(a,b,c): 'hello three two one'

x,y,z=10,20,30
ic("hello {} {} {}".format(x,y,z))#ic| "hello {} {} {}".format(x,y,z): 'hello 10 20 30'
ic("hello {:d} {:d} {:d}".format(x,y,z))#ic| "hello {:d} {:d} {:d}".format(x,y,z): 'hello 10 20 30'
ic("hello {:d} {:f} {:f}".format(x,y,z))#ic| "hello {:d} {:f} {:f}".format(x,y,z): 'hello 10 20.000000 30.000000'
ic("hello {:d} {:.1f} {:.3f}".format(x,y,z))#ic| "hello {:d} {:.1f} {:.3f}".format(x,y,z): 'hello 10 20.0 30.000'


# format in version 3.6+
myname="Mahmoud"
age = 25

ic(f"My name is :{myname} and age is:{age}")#ic| f"My name is :{myname} and age is:{age}": 'My name is :Mahmoud and age is:25'

# finally formatting don't stop :) , but if you need to master it go to this awsome website www.Pyformat.com

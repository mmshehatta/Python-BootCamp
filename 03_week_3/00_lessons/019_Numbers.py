# 00 Lesson 
# >> 03 Data Types
# >> 01_Numbers
# >> 019_Numbers.py

from icecream import ic

# Intergers
ic(type(1))   #ic| type(1): <class 'int'>
ic(type(10))  #ic| type(10): <class 'int'>
ic(type(-10)) #ic| type(-10): <class 'int'>

# floating point
ic(type(1.5))#ic| type(1.5): <class 'float'>
ic(type(1.500))#ic| type(1.500): <class 'float'>
ic(type(100.500))#ic| type(100.500): <class 'float'>


# complex:
myComplexNumber = 2+4j
ic("my complex number is : {}".format(myComplexNumber))#ic| "my complex number is : {}".format(myComplexNumber): 'my complex number is : (2+4j)'
ic("real part is: {}".format(myComplexNumber.real))#ic| "real part is: {}".format(myComplexNumber.real): 'real part is: 2.0'
ic("complex part is: {}".format(myComplexNumber.imag))#ic| "complex part is: {}".format(myComplexNumber.imag): 'complex part is: 4.0'


# important info:
# [1] you can convert from int to float or complex
# [2] you can convert from float to int or complex
# [3] you can not convert from complex to any type

ic(10)          #ic| 10
ic(float(10))   #ic| float(10): 10.0
ic(complex(10)) #ic| complex(10): (10+0j)

ic(10.50)      #ic| 10.5
ic(int(10.50)) #ic| int(10.50): 10
ic(complex(10.50)) #ic| complex(10.50): (10.5+0j)


ic(10.5+0j)  #ic| (10.5+0j)
ic(int(10.5+0j)) #TypeError: can't convert complex to int
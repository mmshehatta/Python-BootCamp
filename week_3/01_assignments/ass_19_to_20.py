"""
التكليف 01
----------
قم بطباعة جميع أنواع ال Numbers كل واحد في سطر منفصل

"""
from icecream import ic
# Types of numbers:
# 1. Integers
# 2. floating point
# 3. Imaginary/complex

# Variables declaration
posInt = 50
negInt = -50
posFloat = 50.5
negFloat = -50.5
posComplex = 2+4j
negComplex = -2+4j

ic("****Integers:")
ic(type(posInt))
ic(type(negInt))
# output:
# ic| '****Integers:'
# ic| type(posInt): <class 'int'>
# ic| type(negInt): <class 'int'>

ic("****Floats:")
ic(type(posFloat))
ic(type(negFloat))
# output:
# ic | '****Floats:'
# ic| type(posFloat): <class 'float'>
# ic| type(negFloat): <class 'float'>

ic("****Imaginary/complex")
ic(type(posComplex))
ic(type(negComplex))
# output:
# ic | '****Imaginary/complex'
# ic | type(posComplex): < class 'complex' >
# ic | type(negComplex): < class 'complex' >


"""
التكليف 02
---------
قم بطباعة الجزء ال Imaginary من ال Complex Number التالي “1+2j” في السطر الأول وفي السطر الثاني قم بطباعة جزء ال Real
"""
imgNumber = 1+2j
ic(imgNumber.imag)
ic(imgNumber.real)
# output:
# ic | imgNumber.imag: 2.0
# ic | imgNumber.real: 1.0


"""
التكليف 03
---------
قم بتحويل الرقم 10 ل Floating Point Number مع وضع عشر أرقام بعد العلامة العشرية
"""
num = 10
f = float(num)
ic(round(f, 2))

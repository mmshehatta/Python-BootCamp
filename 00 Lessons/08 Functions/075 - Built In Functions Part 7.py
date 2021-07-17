
# >> 00 Lesson
# >> 08 Functions
# >> 075 - Built In Functions Part 5.py
from icecream import ic
# -------------------------------------------------
# --- 075 - Built In Functions Part 5.py-----------
# ------------------------------------------------

# [1] enumerate
# [2] help()
# [3] reversed()
# ------------------------------------------------
# 1.enumerate(irerable , strat?):

# class enumerate()
# Return an enumerate object.

#   iterable
#     an object supporting iteration

# The enumerate object yields pairs containing a count (from start, which defaults to zero) and a value yielded by the iterable argument.

# enumerate is useful for obtaining an indexed list:
#     (0, seq[0]), (1, seq[1]), (2, seq[2]), ...


mySkills = ["HTML", "CSS", "JS", "ReactJS"]

for s in mySkills:
    ic(s)
# ic| s: 'HTML'
# ic| s: 'CSS'
# ic| s: 'JS'
# ic| s: 'ReactJS'

mySkillsWithCounter = enumerate(mySkills)

for s in mySkillsWithCounter:
    ic(s)
# ic| s: (0, 'HTML')
# ic| s: (1, 'CSS')
# ic| s: (2, 'JS')
# ic| s: (3, 'ReactJS')

mySkillsWithCounter = enumerate(mySkills, 20)
# ic| type(mySkillsWithCounter): <class 'enumerate'>
ic(type(mySkillsWithCounter))
# ic| list(mySkillsWithCounter): [(20, 'HTML'), (21, 'CSS'), (22, 'JS'), (23, 'ReactJS')]
ic(list(mySkillsWithCounter))

for s in mySkillsWithCounter:
    ic(s)
# ic| s: (20, 'HTML')
# ic| s: (21, 'CSS')
# ic| s: (22, 'JS')
# ic| s: (23, 'ReactJS')


for c, s in enumerate(mySkills, 20):
    ic(f"{c} - {s}")

# ic| f"{c} - {s}": '20 - HTML'
# ic| f"{c} - {s}": '21 - CSS'
# ic| f"{c} - {s}": '22 - JS'


# 2.help()
# help: (*args: Any, **kwds: Any) -> None

# ic(help(ic))
# Help on IceCreamDebugger in module icecream.icecream object:

# class IceCreamDebugger(builtins.object)
#  |  IceCreamDebugger(prefix='ic| ', outputFunction=<function colorizedStderrPrint at 0x7fe47a764940>, argToStringFunction=<function argumentToString at 0x7fe47a7955e0>, includeContext=False)
#  |  
#  |  Methods defined here:
#  |  
#  |  __call__(self, *args)
#  |      Call self as a function.
#  |  
#  |  __init__(self, prefix='ic| ', outputFunction=<function colorizedStderrPrint at 0x7fe47a764940>, argToStringFunction=<function argumentToString at 0x7fe47a7955e0>, includeContext=False)
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |  
#  |  configureOutput(self, prefix=<object object at 0x7fe47a8d3320>, outputFunction=<object object at 0x7fe47a8d3320>, argToStringFunction=<object object at 0x7fe47a8d3320>, includeContext=<object object at 0x7fe47a8d3320>)
#  |  
#  |  disable(self)
#  |  
#  |  enable(self)
#  |  
#  |  format(self, *args)
#  |  
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
#  |  
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |  
#  |  __weakref__
#  |      list of weak references to the object (if defined)
#  |  
#  |  ----------------------------------------------------------------------
#  |  Data and other attributes defined here:
#  |  
#  |  contextDelimiter = '- '
#  |  
#  |  lineWrapWidth = 70



# 3.reversed(iterable)
# class reversed()
# Return a reverse iterator over the values of the given sequence.

myStr = "Mahmoud"

for letter in reversed(myStr):
    ic(letter)

# ic| letter: 'd'
# ic| letter: 'u'
# ic| letter: 'o'
# ic| letter: 'm'
# ic| letter: 'h'
# ic| letter: 'a'
# ic| letter: 'M'



for s in reversed(mySkills):
    ic(s)
# ic| s: 'ReactJS'
# ic| s: 'JS'
# ic| s: 'CSS'
# ic| s: 'HTML'
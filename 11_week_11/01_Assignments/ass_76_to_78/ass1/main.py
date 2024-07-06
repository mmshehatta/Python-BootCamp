
from random import randint


# The Random Number Between (10 And 50) .
s1 = set()
for i in range(10 , 51):
        s1.add(randint(10 , 50))

print(f"Random Number Between 10 And 50 => '{s1}' ")

# The Even Random Number Between (2 And 10) 
s1 = set()
s2 = set()
for i in range(2 , 11):
        s1.add(randint(2 , 10))
for a in s1:
   if a % 2 == 0:
       s2.add(a)
print(f"Random Even Number Between 2 And 10 => '{s2}' " )


# The Odd Random Number Between (2 And 10) 
s1 = set()
s2 = set()
for i in range(1 , 10):
        s1.add(randint(1 , 9))
for a in s1:
   if a % 2 != 0:
       s2.add(a)
print(f"Random Odd Number Between 1 And 9 =>  '{s2}' " )




# Module Methods Content Here.



# ----------------------------------------
# -- Decorators => Practical Speed Test --
# ----------------------------------------

from time import time

def myDecorator(func):  # Decorator

  def nestedFunc(*numbers):  # Any Name Its Just For Decoration

    for number in numbers:

      if number < 0:

        print("Beware One Of The Numbers Is Less Than Zero")

    func(*numbers)  # Execute Function

  return nestedFunc  # Return All Data

@myDecorator

def calculate(n1, n2, n3, n4):

  print(n1 + n2 + n3 + n4)

calculate(-5, 90, 50, 150)

def speedTest(func):

  def wrapper():

    start = time()

    func()

    end = time()

    print(f"Function Running Time Is: {end - start}")

  return wrapper

@speedTest

def bigLoop():

  for number in range(1, 20000):

    print(number)

bigLoop()
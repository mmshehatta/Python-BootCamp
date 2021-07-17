# >> 00 Lesson
# >> 08 Functions
# >>084 - Decorators - Function With Parameters.py
from icecream import ic

#############################################################
# >>084 - Decorators - Function With Parameters.py
#############################################################

# decorator to validate against strings:


def checkStringsDecorator(func):

    def WrapperFun(n1, n2):
        if type(n1) != int or type(n2) != int:
            ic("One of Two num is not integer")
        else:
            func(n1, n2)
    return WrapperFun
# decorator to validate against negative number:


def checkNegativeNumbersDecorator(func):

    def WrapperFun(n1, n2):
        if n1 < 0 or n2 < 0:
            ic("By Aware One of Two num is less than zero !")
        func(n1, n2)
    return WrapperFun


# Calculation Function:
@checkStringsDecorator
@checkNegativeNumbersDecorator
def calc_fun(num1, num2):
    ic(num1 + num2)


calc_fun(-1, 2)
# ic| 'By Aware One of Two num is less than zero !'
# ic| num1 + num2: 1

calc_fun("2", 2)
# ic| 'One of Two num is not integer'


# if we need to make function takes N of Params


def checkStringsDecorator2(func):

    def WrapperFun(*nums):
        for n in nums:
            if type(n) != int:
                ic("One of numbers is not integer")
                break
            func(*nums)
    return WrapperFun
# decorator to validate against negative number:


def checkNegativeNumbersDecorator2(func):

    def WrapperFun(*nums):
        for n in nums:
            if int(n) < 0:
                ic("By Aware One of nums is less than zero !")
                continue
            # func(*nums)
        func(*nums)
    return WrapperFun


print("$" * 30)


@checkStringsDecorator2
@checkNegativeNumbersDecorator2
def calc_fun2(*nums):
    res = 0
    for n in nums:
        if type(n) != int:
            res += int(n)
        res += n

    ic(res)


calc_fun2("1", 2, 3, 4)  # ic| 'One of numbers is not integer'
calc_fun2(-1, 2, 3, 4)   # ic| 'By Aware One of nums is less than zero !' , ic| res: 8

# 00 Lesson 
# >> 03 Data Types
# >> 00_Strings 
# >> 012_Indexing_And_ Slicing.py


from icecream import ic
# Indexing:
myString = "I Love Python I"

print(myString[0]) #index 0 => I
print(myString[9]) #index 9 => t
ic(myString[0])


print(myString[-1]) #index -1 => first char from end(n)
print(myString[-6]) #index -6 => 6th char from end(P)

# Slicing:
print(myString[8:11])  # print this str yth
print(myString[3:5])  # print this str ov

print(myString[:10])#if start not here , will start from zero(I love pyt)
print(myString[5:])#if start not here , will go to the end(e Python)
print(myString[:])  #Full Data

# Slicing: with steps:
print(myString[0::1])  # Full Data
print(myString[::1])  # Full Data
print(myString[::2])  # tack letter and skip 2 letters =>(ILv yhn)
print(myString[::3])  # tack letter and skip 3 letters =>(Io tn)





# example that apear in my mind and i implement it :) 
def get_Word_from_text(needText , originalText):
   result=''
   for ch in originalText:
       if ch.lower() in needText.lower():
           result += ch 
           
   return result

print("|"*40)
print(get_Word_from_text("ITI" , f"{myString}"))

# ====== Result =====
# I
# t
# I
# t
# yth
# ov
# I Love Pyt
# e Python I
# I Love Python I
# I Love Python I
# I Love Python I
# ILv yhnI
# Io tn
# ||||||||||||||||||||||||||||||||||||||||
# ItI

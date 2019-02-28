from modules.utils import *

# ====================================
# MORE ON NUMBERS
# ====================================

# a = 12
# b = 3 

# c = a + b
# d = c / 3
# e = d - 4
# print(e * 12)

# ====================================
# STRINGS
# ====================================
banner('more on strings')

parrot = "Norweigen Blue"
print(parrot)
print(parrot[3]) # 4th char, strings are 0-based array
print(parrot[-2]) # negatives count from the back of the string forward

# range within array, starting at 0, 
# and going to, but not including, 6
print(parrot[0:6])

print(parrot[:6])
print(parrot[6:])
sep()
print(parrot[2:3])

# start at position 0, up to 6, in steps of 2
# so...[N]o[r]w[e]igen Blue
print(parrot[0:6:2])

# starts at 2nd position [1], skipping ahead every 3 characters
# until it runs out of string, so it extracts all the commas
nums = "1, 2, 3, 4, 5, 6, 7, 8, 9, 0"
print(nums[1::2])


string1 = "he's "
string2 = "probably "
print(string1+string2)
print("he's " "probably " "pining") # concats the 3 separate strings

banner("repeat strings")

print("Hello "*5)
print("Hello "*(5+4))
print("Hello "*5 + "4")

banner("substring")

today = "Friday"
print("day" in today)
print("Fri" in today)
print("Thurs" in today)
print("Parrot" in "Fjord")

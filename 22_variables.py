# ----------------------------------------
# 22
# Variables
# ----------------------------------------
from modules.utils import *


banner('Strings')
# ----------------------------------------

greeting = "Bruce"
_myName = "Tim"
Tim45 = "Good"
Tim_Was_57 = "Hello"
Greeting = "There"

print(Tim_Was_57 + ' ' + greeting)

age = 48
# ERROR: Cant concat a string and an integer
# print(greeting + age)


banner('Numbers')
# ----------------------------------------

a = 12
b = 3

print(a+b)
print(a-b)
print(a*b)


# BELOW: normally this is division that returns as an integer.
# However, 3.6.4 by default seems to do the conversion.
# It only forces a float when one of the numbers is actually
# a float

print(a/b)
print(a//b)
print(a % b)

banner("For Loop")
# ----------------------------------------
for i in range(1, a/b):
	print(i)


banner("Formulas & Casting")
# ----------------------------------------
formula = ((((a + b) / 3) - 4) * 12)
print(formula)
print(float(formula)) # implicit cast to float

a = "RobK"
b = 48
print(a+str(b)) # implicit cast to string

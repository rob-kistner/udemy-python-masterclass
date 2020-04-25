# ----------------------------------------

# 59
# More on Dictionaries

# ----------------------------------------
from modules.utils import *


banner("The fruit list...")
# ----------------------------------------
fruits = {
    'orange': 'A sweet orange citrus fruit',
    'apple': 'Good for making cider',
    'lemon': 'A sour yellow citrus fruit',
    'grape': 'A small sweet fruit growing in bunches',
    'lime': 'A sour green citrus fruit'
}

print( fruits )

veg = {
    'cabbage': 'Every child\'s favorite',
    'sprouts': 'Mmmm lovely',
    'spinach': 'May I have some more fruit please?'
}


banner('''Note: doesn't return anything, 
affects the original dict only''')
# ----------------------------------------
veg.update( fruits )

print( veg )


banner("Makes a copy of the dictionary")
# ----------------------------------------
nice_and_nasty = fruits.copy()
nice_and_nasty.update( veg )

print( nice_and_nasty )

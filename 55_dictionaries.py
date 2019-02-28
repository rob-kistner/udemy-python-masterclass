# ----------------------------------------
# 
#  55
#  Python Dictionaries
# 
# ----------------------------------------
from modules.utils import *

fruits = {
    'orange': 'A sweet orange citrus fruit',
    'apple': 'Good for making cider',
    'lemon': 'A sour yellow citrus fruit',
    'grape': 'A small sweet fruit growing in bunches',
    'lime': 'A sour green citrus fruit'
}

print( fruits['lemon'] )
print( fruits['grape'] )
print( fruits['lime'] )

banner("Adding a new entry to the dict")
# ----------------------------------------

fruits[ 'pear' ]='An odd shaped apple'

print( fruits )

banner('''Adding a key that's already there will just replace
the key & value that's there''')
# ----------------------------------------

fruits['grape'] = 'Winds up together with peanut butter'

print(fruits)


banner("Delete a key/value pair")
# ----------------------------------------

del( fruits['lemon'] )
print( fruits )


banner("Will print the added tomatoes item in keys as well")
# ----------------------------------------


fruits[ 'tomatoes' ] = 'Not nice with ice cream'
fruit_keys = fruits.keys()
print( fruit_keys )


banner("Convert to tuple")
# ----------------------------------------
fruit_t = tuple( fruits.items() )
print( fruit_t )


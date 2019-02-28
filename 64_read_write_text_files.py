# ----------------------------------------

# 64
# Reading and writing text files

# ----------------------------------------
from modules.utils import *


banner('''Opens a text file and prints it out
one line at a time''')
# ----------------------------------------

jabber = open( 'jabber.txt', 'r' )

for line in jabber:
    print( line )

jabber.close()


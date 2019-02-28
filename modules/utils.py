# ----------------------------------------
#
#  UTILS
#
#  Utility printouts for testing scripts
#
# ----------------------------------------
repeats = 50

# ----------------------------------------
#  Just prints a newline
#  to separate stuff
# ----------------------------------------

def nl():
    print('\n')

# ----------------------------------------
#  Outputs a string of hyphens
#  to use as a separator
# ----------------------------------------

def sep():
    nl()
    print('-'*repeats)
    nl()

# ----------------------------------------
#  Outputs a string of characters
#  as a separator
# ----------------------------------------

def sepline(sep='-', count=40):
    print(sep * count)

# ----------------------------------------
#  Outputs a comment banner
#  with a custom string
# ----------------------------------------

def banner(s):
    nl()
    print('-' * repeats)
    print(s)
    print('-' * repeats)

# ----------------------------------------
#  Makes a printed header 
#  with rules beneath
# ----------------------------------------

def header(s):
    print('-' * repeats)
    print('|  ' + s)
    print('-' * repeats)


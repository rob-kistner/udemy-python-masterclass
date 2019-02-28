################################
#
#  UTILS
#
#  Utility printouts for testing scripts
#
################################

REPEATS = 36


##############################
#  Just prints a newline
#  to separate stuff
##############################

def nl():
    print('\n')


##############################
#  Outputs a string of hyphens
#  to use as a separator
##############################

def sep():
    nl()
    print('-' * REPEATS)
    nl()

##############################
#  Outputs a string of characters
#  as a separator
##############################

def sepline(char='-', count=20):
    print(char * count)


##############################
#  Outputs a comment banner
#  with a custom string
##############################

def banner(s):
    nl()
    print('-' * REPEATS)
    print(s)
    print('-' * REPEATS)


##############################
#  Makes a printed header 
#  with rules beneath
##############################

def header(s):
    print('-' * REPEATS)
    print('|  ' + s)
    print('-' * REPEATS)


################################
#
#  UTILS
#
#  Utility printouts for testing scripts
#
################################
import console


repeats = 36


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
    con_comment()
    nl()
    print('-'*repeats)
    nl()
    con_normal()

##############################
#  Outputs a string of characters
#  as a separator
##############################

def sepline(sep='-', count=20):
    print(sep * count)

##############################
#  Outputs a comment banner
#  with a custom string
##############################

def banner(s):
    con_comment()
    nl()
    print('-' * repeats)
    print(s)
    print('-' * repeats)
    con_normal()


##############################
#  Set console output 
#  color to pink
##############################

def con_comment():
    console.set_color(1.0, 0.4, 0.6)


##############################
#  Set console output 
#  color to white
##############################

def con_normal():
    console.set_color(1, 1, 1)


##############################
#  Clear console
##############################

def clear():
    console.clear()


##############################
#  Makes a printed header 
#  with rules beneath
##############################

def header(s):
    print('-' * repeats)
    print('|  ' + s)
    print('-' * repeats)


################################
#
#  FUNCTIONS - SCOPE
#
################################

from modules.utils import *


banner("""showing local function vs. global scope""")
##############################
def my_function():
    test = 1
    print('my_function: ', test)

test = 0
my_function()
print('global: ', test)


banner("""outer and inner scoping""")
##############################
def outer():
    # test = 1
    def inner():
        test = 2
        print('inner: ', test)
    inner()
    print('outer: ', test)
    
test = 5
outer()
print('global: ', test)


banner("""legb example:
if the variable isn't defined in the function,
it'll look for it down the legb chain""")
##############################
def legb_example():
    print('inside legb_example function: ', legb_val)
legb_val = 10
legb_example()


banner("""nonlocal scope:
works on enclosed scopes, but not global scopes""")
##############################
def outer():
    test = 1
    def inner():
        nonlocal test
        test = 2
        print('inner: ', test)
    inner()
    print('outer: ', test)
test = 0
outer()
print('global: ', test)

banner("""global scope:
works on global scope, but inner scopes are respected""")
##############################
def outer():
    global_test = 1
    def inner():
        global global_test
        global_test = 2
        print('inner: ', global_test)
    inner()
    print('outer: ', global_test)
global_test = 0
outer()
print('global: ', global_test)


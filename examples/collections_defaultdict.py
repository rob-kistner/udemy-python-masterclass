################################
#
# collections.defaultdict
#
################################
from collections import defaultdict
import utils as u


u.banner("""defaultdict just allows you to
add a member with a value to a dict 
without having initialized it""")
##############################

# initialize a new defaultdict of type integer
dd = defaultdict(int)


u.banner("Adding a new member called 'age'")
##############################
dd['age'] += 1
print(dd['age'])


u.banner("Adding 'birthyear' and 1969")
##############################
dd['birthyear'] += 1969
print(dd['birthyear'])


u.banner("If you don't pass anything, it just gets the value of 0")
##############################
dd['someval']
print(dd['someval'])

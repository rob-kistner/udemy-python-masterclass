################################
#
#  collections.namedtuple
#
################################
from collections import namedtuple
import modules.utils as u


u.clear()

u.banner("""namedtuples are created as a tuple
with 2 members:

  (1) string name of the namedtuple
  (2) list values
 
you instantiate by setting all the 
values as a param to a class-like 
instantiation call""")
##############################

Vision = namedtuple('Vision', ['left', 'combined', 'right'])
combined = (9.5 + 7.2) / 2
vision = Vision(9.8, combined, 7.2)


print("Left eye: {}".format(vision.left))
print("Right eye: {}".format(vision.right))
print("Combined: {}".format(vision.combined))


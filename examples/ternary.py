################################
#
# ternary operator
#
################################
from modules.utils import banner, clear

clear()

# function to output results
def print_order():
	print("sub total: {}".format(sub_total))
	print("order discount: -{}".format(discount))
	print("---")
	print("total: {}".format(sub_total - discount))

sub_total = 247


banner("classic if/then is fine but takes up 4 lines...")
###########################################

if sub_total > 100:
	discount = 25
else:
	discount = 0

print_order()


banner("We can do it in one line with a ternary...")
###########################################

discount = 25 if sub_total > 100 else 0

print_order()


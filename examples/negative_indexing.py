################################
#
# NEGATIVE INDEXING
#
################################
from modules.utils import banner, clear


clear()

banner("""Negative Indexing:

lists, tuples, dicts, etc
that can be accessed by indexes
can also have values accessed
in reverse by using negative
index numbers

Here's a list of 10 numbers...'""")
##############################

nums = list(range(10))
print(nums)


banner("""-1 would pull the last value
that you'd normally have to index
access as nums[len(nums)-1] if you
didn't already know the length""")
##############################

print(nums[-1])


banner("""and you can access them all
the way back down the line with 
other negative numbers""")
##############################

print(nums[-5])
print(nums[-10])


banner("""but you will get an out
of range error if you try to
pull a number past the list
length""")

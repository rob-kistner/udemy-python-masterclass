################################
#
#  LISTS
#
################################

from modules.utils import *

# make a basic list
mylist = [1,2,3]

banner("""list from a tuple...""")
##############################
mylist = ((1,3,5,7,9))
print(mylist)

banner("""list comprehension:
will add 5 to each value in the 
list""")
##############################
mylist = [x+5 for x in [2,3,4]]
print(mylist)


mylist = [1,2,3]

banner('add value to a list')
##############################
mylist.append(13)
mylist.append(1)
print(mylist)


banner('count how many 1\'s are in a list')
##############################
print(mylist)
mycount = mylist.count(1)
print(mycount)


banner('extend a list by 2 members')
##############################
a = [5,7]
print(a)
mylist.extend(a)
print(mylist)


banner('get the index position of member 13')
##############################
print(mylist)
idx = mylist.index(13)
print(idx)


banner('insert 17 at the 0 position')
##############################
print(mylist)
mylist.insert(0, 17)
print(mylist)


banner('remove the last element with pop()')
##############################
print(mylist)
popval = mylist.pop()
print(popval)
print(mylist)


banner('remove 17 from the list')
##############################
print(mylist)
mylist.remove(17)
print('.remove() doesn\'t return a value')
print(mylist)


banner('reverse the list')
##############################
print(mylist)
mylist.reverse()
print(mylist)


banner('sort the list')
##############################
print(mylist)
mylist.sort()
print(mylist)


banner('extend() can split a passed string into list members')
##############################
print(mylist)
mylist.extend('465')
print(mylist)


mylist = [13,6,3,65,188]


banner('get the minimum value in a list')
##############################
print(mylist)
min_list = min(mylist)
print(min_list)


banner('get the maximum value in a list')
##############################
print(mylist)
max_list = max(mylist)
print(max_list)


banner('sum all values in a list')
##############################
print(mylist)
sum_list = sum(mylist)
print(sum_list)

banner('get the length of a list')
##############################
print(mylist)
length = len(mylist)
print(length)

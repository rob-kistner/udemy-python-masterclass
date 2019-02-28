################################
#
# LIST SLICING
#
################################
from modules.utilslaptop import banner


nums = [1, 4, 9, 16, 25]

def showme():
    print(nums)

banner('''original list''')
########################################
showme()


banner('''accessing values in the list''')
########################################
showme()
print(nums[0]) # first item


banner('''accessing values starting from the right''')
########################################
showme()
print(nums[-1]) # first item from right
print(nums[-3]) # third item from right


banner('''concatenating to the list''')
########################################
showme()
nums += [36, 49, 65, 81, 100]
showme()


banner('''replace a single value''')
########################################
showme()
nums[2] = 64
showme()


banner('''add to the end of the list with .append()''')
########################################
showme()
nums.append(216)
nums.append(7**3)
showme()

################################
#
# LIST SLICING
#
################################
from modules.utilslaptop import banner


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

def showme():
    print(letters)


banner('''replace some of the values: [2:5]''')
########################################
letters[2:5] = ['C', 'D', 'E']
showme()

banner('''replace some of the values: [2:5]=[]''')
########################################
letters[2:5] = []
showme()


banner('''from index 1 onward: [1:]''')
########################################
print(letters[1:])


banner('''can add any number of elements anywhere
using the same number slice from:to...ie: [2:2]''')
########################################
showme()
letters[2:2] = ['c', 'd', 'e']
showme()


banner('''up to but not including index 2: [:2]''')
########################################
showme()
print(letters[:2])
showme()


banner('''from the end, 2 items inward [:-2]''')
########################################
showme()
print(letters[:-2])


banner('''show the even items with stride of 2: [::2]''')
########################################
showme()
print(letters[::2])

banner('''stride of -1 will show the reverse list: 
[::-1], and of course stride from the right with
larger negative values: [::-2]''')
########################################
showme()
print(letters[::-1])
print(letters[::-2])


banner('''clear it completely by setting to an empty list: [:]=[]''')
# ########################################
letters[:] = []
showme()


################################
#
# iterating sequences
#
################################
from utils import banner, clear


clear()

people = ['Sherry', 'Ed', 'Joe', 'Charlie', 'Missy']
ages = [56, 57, 54, 49, 51]
nationalities = ['Caucasian', 'Anglo-Saxon', 'Ugandian', 'West Indian', 'Italian']


banner("""in a standard for, you need to add
additional code to index the desired 
value and it can get a little sloppy""")
##############################

for idx in range(len(people)):
	person = people[idx]
	age = ages[idx]
	print(person, ':', age)


banner("""you can clean it up / shorten it
up by using enumerate. Note the 
second iterator gets passed directly 
into the loop...""")
##############################

for idx, person in enumerate(people):
	print(person, ':', ages[idx])


banner("""but the cleanest way always is
to use zip and set the dict members
to variables in the for loop...""")
##############################

for person, age in zip(people, ages):
	print(person, ':', age)


banner("""no reason we can't use 3 lists instead of just 2...'""")
##############################

for person, age, nationality in zip(people, ages, nationalities):
	print(person, ': age', age, ':', nationality)


banner("""you may, for some reason, want to 
exploded the zipped tuples in the 
for loop. That's easy, it's like 
javascript deconstruction.""")
##############################
for data in zip(people, ages, nationalities):
	person, age, nationality = data
	print(person, ': age', age, ':', nationality)


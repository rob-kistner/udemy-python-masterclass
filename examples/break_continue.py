################################
#
# break / continue
#
################################

import modules.utils as u
from datetime import date, timedelta
from modules.money import money


u.clear()

today = date.today()
tomorrow = timedelta( days=1 )
products = [
    { 'sku': 1, 'expiration_date': today, 'price': 100.0 },
    { 'sku': 2, 'expiration_date': tomorrow, 'price': 50.0 },
    { 'sku': 3, 'expiration_date': today, 'price': 20 },
]


u.banner("""
If the expiration date is not today,
skip the item using 'continue', else
print the item
""")
###########################################

u.header('Today\'s specials...')

for product in products:
    if product['expiration_date'] != today:
        continue
    product['price'] *= 0.8   # 20% discount
    print(
        'price for sku {}'.format(product['sku']),
        'is now {}'.format(money(product['price']))
    )


u.banner("""Flip it to tomorrow""")
###########################################

u.header('Tomorrow\'s specials...')

for product in products:
    if product['expiration_date'] != tomorrow:
        continue
    product['price'] *= 0.8   # 20% discount
    print(
        'price for sku {}'.format(product['sku']),
        'is now {}'.format(money(product['price']))
    )


u.banner("""Note that you can make a custom
error using else right after a for 
loop. This seems to be unique to the 
Python language. Below, an error 
will be thrown if no driver is 
found.""")
###########################################

class DriverNotFound(Exception):
    pass

people = [
    ('Tom', 16),
    ('Beth', 17),
    ('Rob', 13),
    ('Missy', 14),
]
driver_age = 17

for person, age in people:
    if age >= driver_age:
        driver = (person, age)
        print(driver)
        break
else:
    raise DriverNotFound('No driver old enough was found.')


u.banner("""Example of prime number printer
using break""")
###########################################

primes = []
upto = 100

for n in range(2, upto + 1):
    is_prime = True
    for divisor in range(2, n):
        if n % divisor == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(n)

print(primes)


u.banner("""Simplified prime number printer,
removing superfluous code""")
###########################################

primes = []
upto = 100
for n in range(2, upto+1):
    for divisor in range(2, n):
        if n % divisor == 0:
            break
    else:
        primes.append(n)
print(primes)

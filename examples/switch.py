################################
#
#  Switch example:
#  Applying discounts
#
################################
import modules.utils as u
from modules.money import money as usd

u.clear()

customers = [
    dict(id=1, total=200, coupon_code='F20'),
    dict(id=2, total=150, coupon_code='P30'),
    dict(id=3, total=100, coupon_code='P50'),
    dict(id=4, total=110, coupon_code='F15'),
]

u.banner("""if/elif/else version""")
###########################################

for customer in customers:
    code = customer['coupon_code']
    if code == 'F20':
        customer['discount'] = 20.0
    elif code == 'F15':
        customer['discount'] = 15.0
    elif code == 'P30':
        customer['discount'] = customer['total'] * 0.3
    elif code == 'P50':
        customer['discount'] = customer['total'] * 0.5
    else:
        customer['discount'] = 0.0

for customer in customers:
    print('Customer {}'.format(customer['id'])) 
    u.sepline('-', 22)
    print('Total: {}'.format(usd(customer['total'], True))) 
    print('Discount: {}'.format(usd(customer['discount'], True)))
    u.nl()


u.banner("""Simplifying by using dict to process""")
###########################################

discounts = {
    # percent, fixed discounts in vals
    'F20': (0.0, 20.0),
    'F15': (0.0, 15.0),
    'P30': (0.3, 0.0),
    'P50': (0.5, 0.0),
}
# calculate total discount
for customer in customers:
    code = customer['coupon_code']
    percent, fixed = discounts.get( code, (0.0, 0.0) )
    customer['discount'] = percent * customer['total'] + fixed

for customer in customers:
    print('Customer {}'.format(customer['id'])) 
    u.sepline('-', 22)
    print('Total:\t\t\t{}'.format(usd(customer['total'], True))) 
    print('Discount:\t\t{}'.format(usd(customer['discount'], True)))
    u.sepline('-', 22)
    print('Grand Total:\t{}'.format(usd(customer['total'] - customer['discount'], True)))
    u.nl()

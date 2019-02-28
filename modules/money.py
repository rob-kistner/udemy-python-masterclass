def money(amt, spaced=False):
	bucks = '$ ' if spaced else '$'
	return '{}{:,.2f}'.format(bucks, amt)


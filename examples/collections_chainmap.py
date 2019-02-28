################################
#
# ChainMap
#
################################
from collections import ChainMap
from utils import clear, banner

clear()

# two maps
default_conn = {'host': 'localhost', 'port': '8888'}
conn = {'port': 1234}


banner("""ChainMap adds two chains together
in a special object that is mutable""")
##############################

conn = ChainMap(conn, default_conn)
print(conn)


banner("print the first port found")
##############################

print(conn['port'])


banner("add a key/value into the first map in the chain")
##############################

conn['host'] = 'Packt Publishing'
print(conn)


banner("""delete the first found port,
now the second port gets printed""")
##############################

del conn['port']
print(conn['port'])


banner("easiest dict merge ever!")
##############################

conn = dict(conn)
print(conn)



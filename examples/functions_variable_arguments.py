################################
#
#  FUNCTIONS :
#  VARIABLE POSITIONAL ARGUMENTS
#
################################
from modules.utilslaptop import banner


banner("""variable positional arguments:
the *n as the parameter signals pythong
to access variable positional arguments""")
##############################
def minimum(*n):
    # print(type(n)) # this will be a tuple
    if n:
        mn = n[0]
        for value in n[1:]:
            if value < mn:
                mn = value
        print(mn)

minimum(1,3,-7,9)
minimum()


banner("""variable keyword arguments:
all listed methods of passing arguments 
result in the same: a dict is created 
containing thge arguments.

Note: the ** method of passing arguments
unpacks the dicts being passed""")
##############################
def func(**kwargs):
    print(kwargs)

func(a=1, b=42)
func(**{'a': 1, 'b': 42})
func(**dict(a=1, b=42))


banner("""More useful example, making a connection
to a database""")
##############################
def connect(**options):
    conn_params = {
        'host': options.get('host', '127.0.0.1'),
        'port': options.get('port', '8080'),
        'user': options.get('user', ''),
        'pwd': options.get('pwd', ''),
    }
    print(conn_params)
    # this is where you'd actually connect
    # db.connect(**conn_params)

connect()
connect(host='localhost', port=1234)
connect(port=5436, user='fab', pwd='gandalf')


banner("""keyword only arguments""")
########################################
def kwo(*a, c):
    print(a, c)

# 3 argument tuple plus required
# defined c
kwo(1, 2, 3, c=7)
# variable number of positional a argments
# get wrapped up into a tuple
kwo(13, 86, 92, 25, 38, 71, 11, 25, c=99)
# empty tuple and c of 4
kwo(c=4)
#kwo(1, 2) # this one's broken, missing 1 keyword-only argument

def kwo2(a, b=42, *, c):
    print(a, b, c)

kwo2(3, b=7, c=99)
kwo2(3, c=13)
#kwo(3, 23) # broken: missing 1 keyword-only argument


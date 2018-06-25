import sys

def print_ops():
    print('available operators: u (union), i (intersection), d (difference), s (symmetric difference)')

# returns the contents of the (newline separated) file as a set, given the argument number
def read_set(argnum):
    # @TODO: error checking for file open / read
    in_name = sys.argv[argnum]
    infile = open(in_name, 'r')
    in_read = infile.read()
    infile.close()
    newset = in_read.splitlines()
    newset = set(newset)
    return newset

# ================================

if len(sys.argv) != 4:
    print('error: wrong number of arguments')
    print('usage: python3 sets.py <operator> <set1_file> set2_file> <(optional) set3_file>')
    print_ops()

operators = 'u', 'i', 'd' 's'
op = sys.argv[1]    # operator
if op not in operators:
    print('error: unknown operator')
    print_ops()
    exit()

setA = read_set(2)
setB = read_set(3)
setC = set([])

if op == 'u':
    setC = setA | setB
elif op == 'i':
    setC = setA & setB
elif op == 'd':
    setC = setA - setB
elif op == 's':
    setC = setA ^ setB

# @TODO: make the below two lines work
newline = {'\n'}
setC = setC - newline

for item in setC:
    print(str(item))

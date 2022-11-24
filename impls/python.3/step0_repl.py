import sys

def READ(x):
    return(x)
def EVAL(y):
    return(y)
def PRINT(z):
    return(z)
def rep(a):
    r = READ(a)
    e = EVAL(r)
    p = PRINT(e)
    return(p)
for line in sys.sidin:
    if line == '^D':
        sys.exit("EOF Reached")
    print(rep(line))

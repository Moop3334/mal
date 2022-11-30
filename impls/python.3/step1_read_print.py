import sys, traceback


def READ(x):
    return(x)
#read

def EVAL(y):
    return(y)
#eval

def PRINT(z):
    return(z)
#print

def REP(a):
    return PRINT(EVAL(READ(a)))
#repl

#repl loop    
while True:
    try:
        line = input("user> ")
        if line == None: break
        if line == "": continue
        print(REP(line))
    except Exception as e:
        print("".join(traceback.format_exception(*sys.exc_info())))
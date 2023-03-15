import  sys

if  __name__ == "__main__":
    if (len(sys.argv) > 2):
        print("Wrong number of input, plase, insert one number")
        exit ()
    elif (len(sys.argv) == 1):
        exit ()
    if not (sys.argv[1].isdigit()):
        print("Please, an integer as argument, just one")
        exit()
    if (int(sys.argv[1]) % 2 == 0 and int(sys.argv[1]) != 0):
        print("ODD")
    elif (int(sys.argv[1]) % 2 != 0):
        print("EVEN")
    elif (int(sys.argv[1]) == 0):
        print("ZERO")
    

    

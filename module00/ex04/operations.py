import sys

def error_msg():
    print("error")
    exit(1)

if __name__ == "__main__":
    if (len(sys.argv) != 3):
        error_msg()
    if (sys.argv[1].isdigit() == 0 or sys.argv[2].isdigit() == 0):
        error_msg()
    suma = int(sys.argv[1]) + int(sys.argv[2])
    resta = int(sys.argv[1]) - int(sys.argv[2])
    prod = int(sys.argv[1]) * int(sys.argv[2])
    if (int(sys.argv[2]) != 0):
        quotient = int(sys.argv[1]) / int(sys.argv[2])
    else:
        quotient = "nope"
    if (int(sys.argv[2]) != 0):
        rest = int(sys.argv[1]) % int(sys.argv[2])
    else:
        rest = "nope"
    print("Sum : " + str(suma))
    print("Difference : " + str(resta))
    print("Product : " + str(prod))
    if (type(quotient) == float):
        print("Quotient : " + str(quotient))
    else:
        print("error: no quotient with zero as denominator")
    if (type(rest) == int):
        print("Remainder : " + str(rest))
    else:
        print("error: no quotient with zero as denominator")
        
    
    
    
        


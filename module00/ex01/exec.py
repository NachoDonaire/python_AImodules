import sys

if __name__ == "__main__":
    if (len(sys.argv) == 1):
        print("Please, insert an argument to the program")
        exit()
    sys.argv.pop(0)
    print(" ".join(sys.argv).swapcase()[::-1])

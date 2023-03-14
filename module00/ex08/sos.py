import sys
def text_to_morse(a):
    morse_dict = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
              'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
              'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
              's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
              'y': '-.--', 'z': '--..'}
    return (morse_dict[a])

if __name__ == "__main__":
    if (len(sys.argv) <= 1):
        print("error: wrong ammount of arguments")
        exit()
    sys.argv.pop(0)
    s = ""
    for i in sys.argv:
        s = s + " " + i
    for e in s:
        if not (e.isalpha() or e.isdigit() or e == ' '):
            print("ERROR")
            exit()
    c = ""
    for e, i in zip(s, range(len(s))):
        if (e == ' '):
            c = c + "/"
        elif (e.isalpha()):
            c = c + text_to_morse(e)
        elif(e.isdigit()):
            c = c + e
        else:
            print("ERROR")
            exit()
    print(c)

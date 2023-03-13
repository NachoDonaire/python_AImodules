import  re

def text_analyzer(s):
    if not (s):
        s = input("Please, introduce a string: \n")
    elif (type(s) != string):
        print("Wrong argument, it must be a string")
    lower = sum(1 for l in s if l.islower())
    upper = sum(1 for u in s if u.isupper())
    #punct = sum(1 for p in s if p.ispunct())
    punct = len(re.findall(r'[^\w\s]', s))
    spaces = sum(1 for sp in s if sp.isspace())

    print("-" + str(lower) + " lower letter(s)")
    print("-" + str(upper) + " upper letter(s)")
    print("-" + str(punct) + " punctuation mark(s)")
    print("-" + str(spaces) + " space(s)")

if __name__ == "__main__":
    text_analyzer("")


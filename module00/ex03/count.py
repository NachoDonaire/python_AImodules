import  re
import  sys

def text_analyzer(s):
    """
    This function takes a string as an argument and counts the number of lowercase and uppercase letters,
    punctuation marks and spaces in the string.

    Args:
        s (str): A string to be analyzed.

    Returns:
        None: This function does not return any value, it only prints the results.

    If the argument is an empty string, a valid string will be asked for the user.
    If the argument is not a string, it will return an error message.
    """
    if not (s):
        s = input("Please, introduce a string: \n")
    elif (type(s) != str):
        print("Wrong argument, it must be a string")
    lower = sum(1 for l in s if l.islower())
    upper = sum(1 for u in s if u.isupper())
    #punct = sum(1 for p in s if p.ispunct())
    punct = len(re.findall(r'[^\w\s]', s))
    spaces = sum(1 for sp in s if sp.isspace())

    print("The text contains " + str(lower + upper) + " characters")
    print("-" + str(lower) + " lower letter(s)")
    print("-" + str(upper) + " upper letter(s)")
    print("-" + str(punct) + " punctuation mark(s)")
    print("-" + str(spaces) + " space(s)")

if __name__ == "__main__":
    if (len(sys.argv) > 2):
        print("error: wrong argument")
        exit ()
    if (len(sys.argv) != 1):
        text_analyzer(sys.argv[1])



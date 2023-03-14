kata = "ssoqufviquooo"

if (type(kata) != str):
    print("error: no string as argument")
    exit ()
if (len(kata) > 42):
    print("error: string must be less or equal 42 characers.")
    exit ()
spaces = 41
neo_kata = "{:>{}}".format(kata, spaces)
print(neo_kata.replace(' ', '-'))

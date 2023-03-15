import random

def proof(text):
    lst = text.split(' ')
    print(lst)
    listy = sorted(lst, key=len)
    print(listy)
    for word in listy:
        yield word

def generator(text, sep=' ', option=None):
    lst = text.split(sep=" ")
    neo_lst = sorted(lst, key=len)
    if (option == "shuffle"):
        neo_lst = list(sorted(lst, key=lambda x: random.random()))
        for word in neo_lst:
            yield word
    elif option == "unique":
        neo_lst = list(set(lst))
        for word in neo_lst:
            yield word
    elif option == "ordered":
        neo_lst = sorted(lst, key=lambda x: x.lower())
        for word in neo_lst:
            yield word
    else:
        for word in lst:
            yield word

if __name__ == "__main__":
    for word in generator("hola que tal estas que", "unique", "ordered"):
        print(word)

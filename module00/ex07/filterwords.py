import  sys
import  string

if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print("error: bad arguments")
        exit()
    if not (str(sys.argv[2].isdigit())):
        print("error: second argument invalid")
        exit()
    lista = []
    s = sys.argv[1]
    punct = string.punctuation
    tab = s.maketrans('', '', punct)
    stringy = s.translate(tab)
    lista = stringy.split(' ')
    tucker = len(lista)
    lista_of = []
    for i, x in zip(lista, range(tucker)):
        if (len(str(i)) >= int(sys.argv[2])):
            lista_of.append(lista[x])
    print(lista_of)
   

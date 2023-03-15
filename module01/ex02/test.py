from vector import Vector

def printeito(v, n):
    print("\n--------------\n")
    print("Valor de v" + str(n) + " : " + str(v))
    print("Output" + str(v.__dict__))
    print("\n--------------\n")


if __name__ == "__main__":
    v = Vector([[3.], [2.], [4.]])
    printeito(v, 1)

    v2 = Vector([[3., 2., 4.]])
    printeito(v2, 2)
    
    v3 = Vector([[3.], [2.], [1.]])
    printeito(v3, 3)

    v4 = Vector([[3., 1., 4.]])
    printeito(v4, 4)

    dot = v2.T()
    print("Esto es la traspuesta de v2, un vector fila: " + str(dot))

    dotty = v3.T()
    print("Esto es la traspuesta de v3, un vector columna: " + str(dotty))
    print("\n")

    suma1 = v + v3
    print("Esto es la suma de v y v3, vectores columna" + str(suma1))

    suma2 = v2 + v4
    print("Esto es la suma de v2 y v4, vectores fila" + str(suma2))
    print()

    resta1 = v - v3
    print("Esto es la resta de v y v3, vectores columna" + str(resta1))

    resta2 = v2 - v4
    print("Esto es la resta de v2 y v4, vectores fila" + str(resta2))

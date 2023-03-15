from vector import Vector

def printeito(v, n):
    print("\n--------------\n")
    print("Valor de v" + str(n) + " : " + str(v))
    print("Output" + str(v.__dict__))
    print("\n--------------\n")


if __name__ == "__main__":
    v = Vector(3)
    printeito(v, 1)

    v2 = Vector([[1., 2., 1.]])
    printeito(v2, 2)
    
    v3 = Vector((1, 4))
    printeito(v3, 3)

    v4 = Vector([[3., 1., 4.]])
    printeito(v4, 4)


    dotander = v.dot(v3)
    print("Esto es el producto escalar  de v con v3, vectores columna: " + str(dotander))

    dotis = v2.dot(v4)
    print("Esto es el producto escalar de v2 con v4, vectores fila: " + str(dotis))
    print()

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
    print()

    prod = v2 * v
    print("Producto entre v2 y v, fila y columna" + str(prod))

    prod2 = v4 * v3
    print("Producto entre v4 y v3, fila y columna" + str(prod2))

    prod3 = v4 * 2.
    print("Producto entre v4 y 2, fila escalar" + str(prod3))

    prod4 = v * 2.
    print("Producto entre v y 2, columna escalar" + str(prod4))
    
    q1 = v3 / 2.
    print("Cociente entre v3 y 2, columna escalar" + str(q1))

    q2 = v2 / 2.
    print("Cociente entre v2 y 2, fila escalar" + str(q2))

class   Vector:
    def __init__(self, arg):
        if type(arg) == tuple:
            if arg[0] < arg[1]:
                tucker = []
                for element in range(arg[0], arg[1]):
                    tuckercin = [[]]
                    tuckercin[0] = float(element)
                    tucker.append(tuckercin)
                self.values = tucker
                self.shape = (len(range(arg[0], arg[1])), 1)
            else:
                print("Wrong tuple initializing vector")
                return

        elif type(arg) == int:
            tucker = []
            if (arg < 3):
                print("error: if initialize with int, arg must be more than 3")
                return 
            for element in range(arg):
                tuckercin = [[]]
                tuckercin[0] = float(element)
                tucker.append(tuckercin)
            self.values = tucker
            self.shape = (len(range(arg)), 1)

        elif type(arg) == list:
        #row vector
            if (len(arg) > 1):
                for a in arg:
                    if type(a) != list:
                        print("error: vector must be initialized as a list")
                        return
                    for n in a:
                        if type(n) != float:
                            print("error: vector must be float")
                            return
                self.values = arg
                self.shape = (len(arg), 1)

        #column vector
            elif (len(arg) == 1):
                for a in arg:
                    if type(a) != list:
                        print("error: vector must be initialized as a list")
                        return
                    for n in a:
                        if not type(n) == float:
                            print("error: vector must be float")
                            return
                self.values = arg
                self.shape = (1, len(arg[0]))
        else:
            print("error: wrong argument, only admits tuple, int, [[]]")
            return

    def dot(self, v2):
        if not (self.shape == v2.shape):
            print("vectors have not the same dimension")
            return
        escalar  = 0
        for r1, r2 in zip(range(len(self.values)), range(len(v2.values))):
            for e1, e2 in zip(self.values[r1], v2.values[r2]):
                escalar = escalar + e1 * e2
        return (escalar)

    def T(self):
        if not (self.shape[1] == 1):
            neo_v = []
            for element, i in zip(self.values[0], range(len(self.values[0]))):
                aux = [[]]
                aux[0] = element
                neo_v.append(aux)
            return neo_v
        elif not (self.shape[0] == 1):
            neo_v = []
            for row, i in zip(self.values, range(len(self.values))):
                for e in row:
                    neo_v.append(e)
            return (neo_v)

    def __add__(self, v2):
        if not self.shape == v2.shape:
            print("error: one is column and the other row")
            return
        if not (self.shape[1] == 1):
            suma = []
            for e1, e2 in zip(self.values[0], v2.values[0]):
                suma.append(e1 + e2)
            return suma
        elif not (self.shape[0] == 1):
            suma = []
            for row1, row2 in zip(self.values, v2.values):
                for e1, e2 in zip(row1, row2):
                    aux = [[]]
                    aux[0] = e1 + e2
                    suma.append(aux)
            return suma

    def __sub__(self, v2):
        if not self.shape == v2.shape:
            print("error: one is column and the other row")
            return
        if not (self.shape[1] == 1):
            suma = []
            for e1, e2 in zip(self.values[0], v2.values[0]):
                suma.append(e1 - e2)
            return suma
        elif not (self.shape[0] == 1):
            suma = []
            for row1, row2 in zip(self.values, v2.values):
                for e1, e2 in zip(row1, row2):
                    aux = [[]]
                    aux[0] = e1 - e2
                    suma.append(aux)
            return suma

    def __mul__(self, k):
        if type(k) == Vector:
            if not self.shape[0] == 1:
                print("first vector in product must be row vector")
                return
            if not k.shape[1] == 1:
                print("second vector must be column vector")
                return
            prod = []
            aux = []
            for row in k.values:
                for e in row:
                    aux.append(e)
            for e1, e2 in zip(self.values[0], aux):
                prody = [[]]
                prody[0] = e1 * e2
                prod.append(prody)
            return (prod)

        elif type(k) == float:
            if not self.shape[1] == 1:
                prod = []
                for e in self.values[0]:
                    prod.append(e * k)
                return prod
            else:
                prod = []
                for row in self.values:
                    for e in row:
                        prody = [[]]
                        prody[0] = e * k
                        prod.append(prody)
                return prod
        else:
            print("Product defined only between vectors and vector escalar")
            return
    def __truediv__(self, k):
        if type(k) == float:
            if (k == 0):
                print("Quotient no defined by zero")
                return
            if not self.shape[1] == 1:
                prod = []
                for e in self.values[0]:
                    prod.append(e / k)
                return prod
            else:
                prod = []
                for row in self.values:
                    for e in row:
                        prody = [[]]
                        prody[0] = e / k
                        prod.append(prody)
                return prod
        else:
            print("Quotient defined for vector and escalar, exclusively")
            return

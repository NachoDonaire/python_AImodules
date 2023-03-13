class Matrix:
    def __init__ (self, data):
        if type(data) == tuple:
            if len(data) != 2:
                self.error()
            self.data = [[0 for i in range(data[0])] for i in range(data[1])]
            self.shape = data
        elif type(data) == list:
            for i in range(len(data)):
                if type(data[i]) != list:
                    self.error()
            self.data = data
            self.shape = (len(data), max(len(max_len) for max_len in data))
        else:
            self.data = 0
            self.shape = 0

    def error(self):
        print("error")
        exit()
        #raise TypeError("error")

    def printeo(self):
        print(self.shape)
        print(self.data)

    def __add__(self, m2):
        suma = []
        if (type(m2) != Matrix or type(self.data) != list):
            self.error()
        else:
            if (self.shape != m2.shape):
                self.error()
            for row1, row2 in zip(self.data, m2.data):
                row_suma = []
                for element1, element2 in zip(row1, row2):
                    row_suma.append(element1 + element2)
                suma.append(row_suma)
            return suma
    def __sub__(self, m2):
        resta = []
        if (type(m2) != Matrix or type(self.data) != list):
            self.error()
        if (self.shape != m2.shape):
            self.error()
        for row1, row2 in zip(self.data, m2.data):
            row_sub = []
            for i, j in zip(row1, row2):
                row_sub.append(i - j)
            resta.append(row_sub)
        return (resta)
    def __radd__(self, m2):
        self.__add__(m2)
    def __rsub__(self, m2):
        self.__sub__(m2)

    def __truediv__(self, k):
        if type(self.data) != list or type(k) != int:
            self.error()
        else:
            div = []
            for row in self.data:
                neo_row = []
                for e in row:
                    neo_row.append(e / k)
                div.append(neo_row)
            return (div)

    def __rtruediv__(self, k):
        self.__truediv__(k)

    def __mul__(self, v):
        if (type(v) == Matrix):
            if (self.shape[1] != v.shape[0]):
                self.error()
            else:
                m_matrix = []
                for row1, row2 in zip(self.data, v.data):
                    row = []
                    for e1, e2 in zip(row1, row2):


            

        

        

if __name__ == "__main__":
    matrix = Matrix([[3, 2], [2, 3]]);
    m2 = Matrix((2, 2));
    k = 2;
    print(k / matrix)
    #matrix.printeo()


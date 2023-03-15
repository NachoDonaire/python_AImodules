class   Evaluator:
    #def __init__(self, ls):
     #   self.lst = ls
    def zip_evaluate(coef, words):
        if (type(coef) == list and type(words) == list):
            if (len(coef) != len(words)):
                print("error: coef and words must be of the same len")
                return
            suma = 0
            for e,i in zip(words, coef):
                suma += len(e) * i
            return suma
        else:
            print("error: not valid input2")
    def enumerate_evaluate(self, coef, words):
        if (type(coef) == list and type(words) == list):
            suma = 0
            for e,i in zip(words, coef):
                suma += len(e) * i
            coef_sum = 0
            words_sum = 0
            for i,e in zip(coef, words):
                coef_sum += i
                words_sum += e
            if not coef_sum == words_sum:
                return self.invalid_input()
            suma /= coef_sum
            return suma
        else:
            print("error: not valid input2")
    def invalid_input(self):
        print("not valid input")
        return 0
    
if __name__ == "__main__":
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    suma = Evaluator.zip_evaluate(coefs, words)
    print(suma)

import  functools as funt

def ft_reduce(f, i):
    return funt.reduce(f, i)

if __name__ == "__main__":
    lst = [1, 2, 3]
    print(ft_reduce(lambda u, q: u + q + 1, lst))

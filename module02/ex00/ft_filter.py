def ft_filter(f, i):
    return filter(f, i)


if __name__ == "__main__":
    lst = [2, 3, 4, 5, 6]
    print(list(ft_filter(lambda  dum: not dum % 2, lst)))


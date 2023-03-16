def ft_map(f, i):
    lst = map(f, i)
    return (lst)

if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    print(list(ft_map(lambda dum: dum + 1, lst)))

def numeros_naturales():
    n = 1
    yield n
    n += 1
    yield n
for natural in numeros_naturales():
    print(natural)

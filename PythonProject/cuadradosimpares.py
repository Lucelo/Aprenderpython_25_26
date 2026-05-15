lista = [1, 2, 3, 4, 5]

print(lista)

cuadrado = [i ** 2 for i in lista]

print(cuadrado)

cuadradoImpar= [i ** 2 for i in lista if i % 2 == 1]
cuadradoPar= [i ** 2 for i in lista if i % 2 == 0]

print(cuadradoImpar)

print(cuadradoPar)

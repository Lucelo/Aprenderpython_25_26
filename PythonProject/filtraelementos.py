def filtra_elementos(lista):
    print("por While")
    i = 0

    while i < len(lista):
        if lista[i] >= 18:
            print(lista[i])
        i += 1

    print("por for")
    for elemento in lista:
        if elemento >= 18:
            print(elemento)


if __name__ == "__main__":
    lista = [15, 20, 13, 30, 25]

    filtra_elementos(lista)

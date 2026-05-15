def calcular_area_rectangulo(base, altura):
    calcular = (base * altura)

    return calcular


if __name__ == "__main__":
    base = int(input("Digite el valor de la base: "))
    altura = int(input("Digite el valor de la altura: "))

    print("El resultado seria", calcular_area_rectangulo(base, altura))

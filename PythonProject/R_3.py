def calcular_perimetro(lado):
    lado = int(lado * 4)
    return lado


if __name__ == "__main__":
    lado = int(input("Que tan largo es la cara del cuadrado \n"))

    print("El perimetro de un cuadrado sea", calcular_perimetro(lado))

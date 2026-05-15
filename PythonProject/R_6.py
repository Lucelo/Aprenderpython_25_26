import math

def calculaRaiz(numero):

    raiz= math.sqrt(numero)

    return raiz


if __name__=="__main__":

    numero=int(input("Escribe un numero: \n"))

    print("El resultado es",calculaRaiz(numero))


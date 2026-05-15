def combersionDeTiempoHoraSegundo(horas):

    segundos= int(horas * 3600)

    return segundos



if __name__=="__main__":
    horas= int( input("Dime la cantidad de horas \n"))

    print("Los segundos serian", combersionDeTiempoHoraSegundo(horas))
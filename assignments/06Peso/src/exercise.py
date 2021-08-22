def main():
    #escribe tu código abajo de esta línea
    PesoI= float(input("Dame el peso inicial: "))
    PesoF= float(input("Dame el peso final: "))
    Meses= int(input("Dame la cantidad de meses: "))
    resta= PesoI-PesoF
    division= resta/Meses
    float(division)
    print("Lo que debes bajar por mes es: " + str(division))




if __name__ == '__main__':
    main()

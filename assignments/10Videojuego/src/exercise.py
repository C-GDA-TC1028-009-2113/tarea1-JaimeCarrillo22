def main():
    #escribe tu código abajo de esta línea
    JuegosN= int(input("Dame la cantidad de juegos nuevos: "))
    JuegosU= int(input("Dame la cantidad de juegos usados: "))
    multiplicacion= JuegosN*1000
    multiplicacion2= JuegosU*350
    suma= multiplicacion+multiplicacion2
    print("El total de la compra es: "+ str(suma))




if __name__ == '__main__':
    main()

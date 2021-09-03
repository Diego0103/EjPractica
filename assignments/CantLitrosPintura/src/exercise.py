import math
def main():
    #escribe tu código abajo de esta línea
    areapintar=float(input("Área a pintar: "))
    metroslitro=float(input("Metros por litro: "))
    cantlitros=areapintar/metroslitro
    print("La cantidad de litros a pintar: "+str(math.ceil(cantlitros)))


if __name__=='__main__':
    main()

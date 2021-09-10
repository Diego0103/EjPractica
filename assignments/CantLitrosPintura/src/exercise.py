#Litros de pintura
#Escribe un programa para calcular la cantidad de litros de pintura necesarios para pintar una superficie.
#El programa debe leer el área de la superficie a pintar en metros cuadrados y la cantidad de metros cuadrados que se pueden cubrir con un litro de pintura. Y mostrar la cantidad de litros de pintura que se deben comprar para cubrir esa superficie.
#Considera que sólo se pueden comprar litros completos de pintura.
#Entradas:
#El área a pintar (número flotante)
#La cantidad de metros cuadrados que se pueden cubrir con un litro de pintura (número flotante)
#Salida
#La cantidad de litros a pintar (número entero)
#Ejemplo de ejecución del programa:
#>>> 857.5
#>>> 10
#86
import math
def main():
    #escribe tu código abajo de esta línea
    areapintar=float(input("Área a pintar: "))
    metroslitro=float(input("Metros por litro: "))
    cantlitros=areapintar/metroslitro
    print("La cantidad de litros a pintar: "+str(math.ceil(cantlitros)))


if __name__=='__main__':
    main()

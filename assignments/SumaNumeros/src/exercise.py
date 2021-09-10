#Suma números
#Escribe un programa que sume los números enteros (positivos y negativos) que el usuario teclee y se 
#detenga hasta que el usuario teclee un cero.
#Entrada
#Una secuencia de números enteros positivos o negativos. La secuencia debe terminar con un 0.
#Salida
#La suma de los números tecleados.
#Ejemplo de ejecución del programa:
#>>>2
#>>>5
#>>>6
#>>>0
#13
def main():
    #escribe tu código abajo de esta línea
    n=int(input("Dame un número: "))
    suma=0
    while n!=0:
        suma=suma+n
        n=int(input("Dame un número: "))
    print (suma)

if __name__=='__main__':
    main()

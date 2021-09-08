#Escribe un método que reciba un número entero positivo n, después debe calcular la suma 1+2+3+...+n. 
#Finalmente regrese el resultado de la suma y sea impreso en pantalla.
#Entrada
#Un número entero positivo n
#Salida
#El resultado de la suma 1+2+3...+n
#Ejemplo de ejecución del programa:
#>>>6
#21
def main():
    #escribe tu código abajo de esta línea
    n=int(input("Dame un número: ")
    suma=0
    while n>0:
        suma=suma+n
        n=int(input("Dame un número: "))
    print(suma)
            



    

if __name__=='__main__':
    main()

#Cuenta números
#Escribe un programa que lea un número positivo n, e imprima todos los números en orden desde el 1 hasta n. Cada uno de los números debe ser impreso en una linea por separado.
#Entrada
#Un número entero positivo n
#Salida
#Los números enteros desde 1 hasta n, uno en cada renglón
#Ejemplo de ejecución del programa:
#>>>5
#1
#2
#3
#4
#5
def main():
    #escribe tu código abajo de esta línea
    n=int(input("Cuál es el número? "))
    for x in range(1,n+1):
        print(x)

if __name__=='__main__':
    main()

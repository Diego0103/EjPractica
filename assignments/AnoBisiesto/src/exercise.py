#Escribe un programa en el cual definas la función es_bisiesto. 
#Esta función debe recibir como parámetro un número entero que representa un año, y te debe regresar True
#si el año es bisiesto, y False en caso contrario.
#Recuerda que un año es bisiesto si es divisible entre 4, excepto cuando es divisible entre 100. Aquellos
#años que son divisibles entre 100 no son bisiestos, a menos que sean divisibles entre 400.
#Ejemplo 1:
#Entrada: 1800
#Salida: False
#Ejemplo 2:
#Entrada: 1996
#Salida: True
#Entrada
#Un número entero que representa un año
#Salida
#True si el año es bisiesto y False si no lo es
#Ejemplo de ejecución del programa:
#>>>2020
#True
def es_bisiesto(year):
    if year%4==0 and year%100!=0:
        return True
    else:
        return False

def main():
    #escribe tu código abajo de esta línea
    ano=int(input('Año: '))
    print (es_bisiesto(ano))

if __name__=='__main__':
    main()

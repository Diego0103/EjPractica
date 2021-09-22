#Escribe un programa que calcule el IMC (Índice de Masa Corporal) de una persona, el cual se utiliza para
#determinar si la proporción de peso y altura es adecuada. El IMC se puede calcular utilizando la 
#siguiente fórmula:
#indice = peso / altura**2
#Donde el peso debe darse en kilogramos y la altura en metros. La siguiente tabla muestra cómo se 
#clasifican los diferentes rangos de índice:
#Rango de índice          Descripción
#índice < 20                  'PESO BAJO'
#20 <= índice < 25         'NORMAL'
#25 <= índice < 30         'SOBREPESO'
#30 <= índice < 40         'OBESIDAD'
#40 >= índice                'OBESIDAD MORBIDA'
#Entrada
#Dos números flotantes (peso y altura) uno en cada renglón y recibidos en este orden.
#Salida
#Un string correspondiente a la descripción del índice de masa corporal, tal como se ve en la tabla, todo
# en mayúsculas.
#Ejemplo de ejecución del programa
#>>> 53
#>>> 1.66
#PESO BAJO
def main():
    #escribe tu código abajo de esta línea
    peso=float(input("peso: "))
    altura=float(input("altura: "))
    indice=peso / altura**2
    if indice >0 and indice < 20:
        print ('PESO BAJO')
    elif 20 <= indice < 25:
        print ('NORMAL')
    elif 25 <= indice < 30:
        print ('SOBREPESO')
    elif 30 <= indice < 40:
        print ('OBESIDAD')
    elif indice<100 and 40 >= indice:
        print ('OBESIDAD MORBIDA')
    else:
        print('ERROR')

if __name__=='__main__':
    main()

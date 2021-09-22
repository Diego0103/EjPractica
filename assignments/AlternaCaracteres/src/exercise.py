'''Escribe un programa que lea un valor n y que muestre en la pantalla n caracteres que alternan entre # 
y %.
Los caracteres se deben mostrar uno en cada renglón.
Observa que el primer caracter que se debe mostrar siempre es #
Entrada
Un valor entero positivo n
Salida
Una secuencia de caracteres que inicia con # y alterna entre # y %. Un caracter en cada renglón.
Ejemplo de ejecución del programa:
>>>7
#
%
#
%
#
%
#
'''
def main():
    #escribe tu código abajo de esta línea
    n= int(input("Número: "))
    for i in range(n):
        if i%2==0:
            print ('#')
        else:
            print ('%')

if __name__=='__main__':
    main()

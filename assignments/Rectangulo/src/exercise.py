#Ejercicio 2
#Escribe una función llamada areaRect que reciba como parámetro el largo y ancho de un rectángulo y que 
#regresa como valor de retorno el área del rectángulo.
#Escribe una función llamada perimetroRect que reciba como parámetro el largo y ancho de un rectángulo y
#que regresa como valor de retorno el perímetro del rectángulo.
#Observa que dentro de las funciones no mostrarás nada, solo regresarás el valor calculado usando return.
#Escribe ahora una función main que pregunte al usuario el largo y ancho del rectángulo y después pregunte 
#si quiere calcular el área o el perímetro del rectángulo (puedes pedir una clave a para área y p para 
#perímetro) y después muestre el valor correspondiente al cálculo que pidió el usuario.
def areaRect(l,a):
    area=l*a
    return (area)

def perimetroRect(l,a):
    perimetro=2*l+2*a
    return (perimetro)

def main():
    #escribe tu código abajo de esta línea
    largo=int(input("Largo: "))
    ancho=int(input("Ancho: "))
    calcular=input("Tecla (a) para area o (p) para perimetro: ")
    if calcular=="a" or calcular=="A":
        print("El área es: "+str(areaRect(largo,ancho)))
    elif calcular=="p" or calcular=="P":
        print("El perimetro es: "+str(perimetroRect(largo,ancho)))
    else:
        print("Incorrecto")
    

if __name__=='__main__':
    main()

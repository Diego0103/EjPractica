import math
def main():
    #escribe tu código abajo de esta línea
    altura= float(input("Altura: "))
    angulo= float(input("Ángulo: "))
    largo=round(altura/math.sin(math.radians(angulo))
    print("El largo es: "+str(largo))



if __name__=='__main__':
    main()

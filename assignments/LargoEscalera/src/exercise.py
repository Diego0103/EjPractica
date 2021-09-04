import math
def main():
    #escribe tu código abajo de esta línea
    altura= float(input("Altura: "))
    angulo= float(input("Ángulo: "))
    angulorad=math.radians(angulo)
    largo=altura/math.sin(angulorad)
    print("El largo es: "+str(math.ceil(largo)))
   



if __name__=='__main__':
    main()

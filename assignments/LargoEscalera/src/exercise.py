#Largo de una escalera 
#Escribe un programa que determine el largo que debe tener una escalera, la cual se necesita para alcanzar una altura determinada, cuando se pone contra una casa. La altura que se desea alcanzar y el ángulo que deberá hacer la escalera contra la pared, son datos que te proporciona el usuario. Para calcular el largo de la escalera usa la siguiente ecuación: largo=altura/seno(ángulo). Recuerda que las funciones de Python que calculan seno y coseno, reciben los ángulos en radianes, pero tu programa va a recibir los ángulos en grados.
#Entrada
#Un número que corresponde a la altura de la casa (flotante positivo) y el ángulo en grados (entero positivo), en ese orden.
#Salida
#Un número, un número que representa el largo que debe tener la escalera. IMPORTANTE: Redondea el número para que el resultado sea entero. Utiliza la función adecuada que te provee Python para realizar un redondeo.
#Ejemplo:
#>>> 2
#>>> 45
#3
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

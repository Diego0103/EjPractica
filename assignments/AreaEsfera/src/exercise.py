#Ejercicio 1
#El área y volumen de una esfera se calcula con las siguientes fórmulas:
#área =  4πr2
#volumen = 4πr33
#Escribe un programa que pida el valor del radio y muestre su área y su volumen.
#Ejercicio 2
#El área de un triángulo cuyos lados son de longitud a, b y c se calcula como 
#área = s(s−a)(s−b)(s−c)−−−−−−−−−−−−−−−−−−√2          
#dónde s=(a+b+c)2
#Escribe un programa que pida al usuario los valores a, b y c y calcule y muestre el área del triángulo usando esta fórmula.
import math
def main():
    #escribe tu código abajo de esta línea
    r=float(input("Radio: "))
    area=4*math.pi*r**2
    volumen=(4*math.pi*r**3)/3
    print("Área= "+str(float(area)))
    print("Volumen= "+str(float(volumen)))

if __name__=='__main__':
    main()

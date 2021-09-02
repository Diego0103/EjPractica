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

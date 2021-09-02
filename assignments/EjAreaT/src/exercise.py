import math
def main():
    #escribe tu código abajo de esta línea
    a=float(input("Dame a: "))
    b=float(input("Dame b: "))
    c=float(input("Dame c: "))
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Area: "+str(area))

if __name__=='__main__':
    main()

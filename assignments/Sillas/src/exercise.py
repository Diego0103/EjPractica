#Ejercicio 1
#En una tienda de sillas para oficina se venden de 3 tipos: básica, estándar y de lujo.
#Además existen los clientes normales y los clientes frecuentes.
#El precio de las sillas es:
#Básica $700.00 c/u
#Estándar $900.00 c/u
#De Lujo $1,500.00 c/u
#El dueño de la tienda ha decidido dar un descuento del 20% a los clientes frecuentes.
#Además ha decidido aplicar la siguiente política de descuentos por mayoreo a los clientes normales:
#si su compra es >= $10,000 y <$20,000 un 10% de descuento
#si su compra es >= $20,000 un 15% de descuento
#Escribe un programa que pregunte el tipo de silla, el tipo de cliente y la cantidad a comprar (supón que
#solo se va a comprar de un tipo de silla) y calcule y muestre:
#el precio antes de aplicar descuento,
#la cantidad de dinero que se otorga por descuento y
#el total a pagar por el cliente.
#Usa funciones para resolver tu programa.
#Entrada
#Una letra mayúscula que representa el tipo de silla
#Una letra mayúscula que representa el tipo de cliente
#Un número entero que indica la cantidad de sillas a comprar.
#Salida
#El precio antes de descuento
#El descuento
#El total a pagar por el cliente
#Ejemplo de ejecución del programa:
#>>>E                                                                                                              
#>>>F                                                                                                             
#>>>5                                                                                                              
#4500                                                                                                          
#900.0                                                                                                         
#3600.0 

def precioNormal(silla,cant):
    b=700
    e=900
    d=1500
    if silla=="b" or silla=="B":
        return cant*b
    elif silla=="e" or silla=="E":
        return cant*e
    elif silla=="d" or silla=="D":
        return cant*d
    else:
        return 0

def descuento(precion,tipocliente):
    if tipocliente=="N" or tipocliente=="n": 
        if precion>=10000 and precion<20000:
            return precion*0.1
        elif precion>=20000:
            return precion*0.15
        else:
            return 0
    elif tipocliente=="F" or tipocliente=="f":
        return precion*0.2
    else: 
        return 0

def preciofinal(precion,desc):
    totalneto=precion-desc
    return totalneto

def main():
    #escribe tu código abajo de esta línea
    tipoSilla=input("Escribe (b)ásica o (e)stándar o (d)e lujo: ")
    tipoCliente=input("Escribe (F)recuente o (N)ormal: ")
    cantSillas=int(input("Cantidad de sillas: "))
    total=precioNormal(tipoSilla,cantSillas)
    desc=descuento(total,tipoCliente)
    print("Precio normal: "+str(total))
    print("Descuento: "+str(desc))
    print("Precio Neto:"+str(preciofinal(total,desc)))

    

if __name__=='__main__':
    main()

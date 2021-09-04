#Ejercicio 1
#Escribe una función llamada equivalente que reciba como parámetro una cantidad de horas, minutos y 
#segundos y regrese como valor de retorno el tiempo equivalente en segundos.
#Por ejemplo:
#Si la función recibe los valores horas = 2, minutos = 20 y segundos = 8, regresará el valor 8408.
#Nota que la función no mostrará nada, solo regresa como valor de retorno la cantidad de segundos 
#equivalente.
#Ahora escribe una función main en la que pidas al usuario teclear cuanto tiempo en horas, minutos y 
#segundos han tardado 2 procesos, después de pedir el tiempo que dura cada proceso muestra el tiempo 
#equivalente en segundos de dicho proceso.
def equivalente(h,m,s):
    tseg=h*3600+m*60+s  
    return (tseg)

def main():
    hora=int(input("Horas: "))
    minutos=int(input("Minutos: "))
    segundos=int(input("Segundos: "))
    print("Tiempo en segundos: "+str(equivalente(hora,minutos,segundos)))

    
    

    
    
    

if __name__=='__main__':
    main()

"""
Ejercicio 01
Escribir dos funciones que permitan calcular:
    La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
    La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
"""


def hms_seg(h, m, s):

    return ((h*60)+m)*60+s

def seg_hms(s):

    horas = s//3600
    s = s % 3600
    minutos = s//60
    segundos = s % 60

    return (horas, minutos, segundos)

leyendo = True

while leyendo:

    try:
        print("La cantidad de segundos en un tiempo dado en horas, minutos y segundos.")
    
        horas = int(input("Introduzca el número de horas: "))
        minutos = int(input("Introduzca el número de minutos: "))
        segundos = int(input("Introduzca el número de segundos: "))

        print("La cantidad de horas, minutos y segundos de un tiempo dado en segundos.")

        segundos_total = int(input("Introduzca el número total de segundos: "))

        leyendo = False
    except:

        print("Introduzca solo valores numéricos.\n")


print("Total: " + hms_seg(horas, minutos, segundos))
print("Solución: " + seg_hms(segundos_total))  
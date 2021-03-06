"""
Ejercicio 03
Escribir un programa que reciba una a una las notas del usuario,
preguntando a cada paso si desea ingresar más notas, e imprimiendo el
promedio correspondiente.
"""

print("Introduzca sus notas")
i = 0
total = 0
masNotas = True
while masNotas:
    leyendo = True
    while leyendo:
        try:
            n = float(input("Introduzca nota : "))
            leyendo = False
        except ValueError:
            print("Introduzca un valor numérico")
    total += n
    i += 1
    leyendo = True
    while leyendo:
        respuesta = input("¿Otra nota? (S/N)")
        if (respuesta in "SNsn") and not(respuesta == ""):
            leyendo = False
    if respuesta in "Nn":
        masNotas = False
print("Su nota media es de", total / i, "puntos")
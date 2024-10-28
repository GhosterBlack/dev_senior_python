# Escribe un programa que solicite un año al usuario y 
# determine si es un año bisiesto. Un año es bisiesto si es 
# divisible por 4 pero no por 100, a menos que también sea divisible por 400.

# Creado por Ivan TG. Profe este no lo voy a complicar por que ya es complicado XD

anio = input("Escriba un año")
if anio.isnumeric():
    anio = int(anio)
    if (anio % 4 == 0) and (anio % 100 != 0 or anio % 400 == 0):
        print("El año es biciesto")
    else:
        print("El año no es biciesto")
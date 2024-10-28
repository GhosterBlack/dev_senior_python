# Escribe un programa que solicite al usuario su edad y su país de residencia. 
# El programa debe verificar si el usuario tiene al menos 18 años y si vive en un país específico 
# (por ejemplo, "España") para determinar si puede votar en las elecciones nacionales.

# Programa hecho por Ivan TG. 
# Hola profesor, a partir de este ejercicio me he propuesto llevarlos acabo usando solo las cosas que hasta ahora
# nos ha explicado, operadores, condicionales, variables, etc. 
# Tenga en cuenta que no los hago mas complejos por lucirme o por hacer mas de lo que me piden, sino que ya he hecho estos
# ejercicios varias veces y tomo esto como una oportunidad de practicar mi logica con pocos recursos.

pedirEdad = input("Por favor digite su edad")
puedeContinuar = True

if not (pedirEdad.isnumeric()):
    pedirEdad = input("Por favor digite un numero correcto")

if not pedirEdad.isnumeric():
    print("No has digitado una edad correcta")
    puedeContinuar = False

if puedeContinuar:
    edad = int(pedirEdad)
    puedeVotar = False
    pais = input("Escriba su pais de residencia")
    para16 = "Argentina argentina ARGENTINA Brasil brasil BRASIL Ecuador ecuador ECUADOR Malta malta MALTA Nicaragua nicaragua NICARAGUA"
    para17 = "Grecia grecia GRECIA Indonesia indonesia INDONESIA"
    if edad >= 18 or (pais in para16 and edad >= 16) or (pais in para17 and edad >= 17):
        puedeVotar = True
    
    if puedeVotar:
        print("Usted puede votar en las elecciones nacionales")
    else:
        print("Usted aun no puede votar en elecciones nacionales")

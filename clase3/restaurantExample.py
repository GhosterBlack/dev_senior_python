# Este programa fue hecho por Ivan TG Y Eduin Rodriguez

# Primero vamos a pedirle al chef los platos y sus precios
cantidadPlatos = 0
nombrePlato1 = ""
nombrePlato2 = ""
nombrePlato3 = ""
nombrePlato4 = ""
nombrePlato5 = ""
precioPlato1 = 0
precioPlato2 = 0
precioPlato3 = 0
precioPlato4 = 0
precioPlato5 = 0
digitarPlato = True

print("#############################################")

while digitarPlato and cantidadPlatos < 5:
    print("Digite el nombre del plato y el precio")
    # Primero almacenamos en variables temporales los nombres de los platos
    nombre = input("Escriba el plato: ")
    precio = input("Escriba el precio: ")
    # validamos que el precio sea un valor numerico
    while not precio.isnumeric():
        precio = input("Escriba un numero correcto de precio: ")
    precio = int(precio)

    # Almacenamos los datos ingresados en las variables globales para poder acceder a ellos mas tarde
    # Esto es lo que pasa cuando no tienes arrays XD
    if cantidadPlatos == 0:
        nombrePlato1 = nombre
        precioPlato1 = precio
    if cantidadPlatos == 1:
        nombrePlato2 = nombre
        precioPlato2 = precio
    if cantidadPlatos == 2:
        nombrePlato3 = nombre
        precioPlato3 = precio
    if cantidadPlatos == 3:
        nombrePlato4 = nombre
        precioPlato4 = precio
    if cantidadPlatos == 4:
        nombrePlato5 = nombre
        precioPlato5 = precio
    cantidadPlatos += 1
    # Ahora preguntamos si se desea ingresar un nuevo dato
    print("¿Desea escribir otro plato? \n 1) Si \n 2) No")
    isPosibleResponse = False
    if cantidadPlatos >= 5:
        isPosibleResponse = True
    # En caso de que la respuesta no sea correcta se vuelve a preguntar
    while not isPosibleResponse:
        response = input("Respuesta: ")
        if response == "1" or response == "Si" or response == "si" or response == "SI":
            isPosibleResponse = True
        if response == "2" or response == "No" or response == "no" or response == "NO":
            isPosibleResponse = True
            digitarPlato = False

# se informa que el programa ya registro los platos
print("------------------------------------ \n\
    Platos registrados \n\
    Iniciando programa de facturacion...\n\
------------------------------------")

gananciaTotal = 0
terminar = False
cantidadMesasAtendidad = 0

while not terminar:
    factura = "---------------------------- \n FACTURA"
    montoTotal = 0
    print(f"Mesa numero {cantidadMesasAtendidad+1} ¿Cuantas ordenes va a pedir?")
    numeroDePersonas = input("Numero de ordenes: ")
    while not numeroDePersonas.isnumeric():
        numeroDePersonas = input("Escriba un numero correcto: ")
    numeroDePersonas = int(numeroDePersonas)
    for i in range(numeroDePersonas):
        print("¿Que va a ordenar?")
        print(f"1) {nombrePlato1} ...... valor: {precioPlato1}$")
        if nombrePlato2 != "":
            print(f"2) {nombrePlato2} ...... valor: {precioPlato2}$")
        if nombrePlato3 != "":
            print(f"3) {nombrePlato3} ...... valor: {precioPlato3}$")
        if nombrePlato4 != "":
            print(f"4) {nombrePlato4} ...... valor: {precioPlato4}$")
        if nombrePlato5 != "":
            print(f"5) {nombrePlato5} ...... valor: {precioPlato5}$")

        response = input("Respuesta: ")
        if response == "1":
            factura += f"\n {nombrePlato1} ...... valor: {precioPlato1}$"
            montoTotal += precioPlato1
        elif response == "2":
            factura += f"\n {nombrePlato2} ...... valor: {precioPlato2}$"
            montoTotal += precioPlato2
        elif response == "3":
            factura += f"\n {nombrePlato3} ...... valor: {precioPlato3}$"
            montoTotal += precioPlato3
        elif response == "4":
            factura += f"\n {nombrePlato4} ...... valor: {precioPlato4}$"
            montoTotal += precioPlato4
        elif response == "5":
            factura += f"\n {nombrePlato5} ...... valor: {precioPlato5}$"
            montoTotal += precioPlato5
    factura += f"\n Total a pagar: {montoTotal} \n ----------------------------"
    print(factura)
    gananciaTotal += montoTotal

    print("¿Cerrar tienda? \n 1) Si \n 2) No")
    isPosibleResponse = False
    cantidadMesasAtendidad += 1

    # En caso de que la respuesta no sea correcta se vuelve a preguntar
    while not isPosibleResponse:
        response = input("Respuesta: ")
        if response == "1" or response == "Si" or response == "si" or response == "SI":
            isPosibleResponse = True
            terminar = True
        if response == "2" or response == "No" or response == "no" or response == "NO":
            isPosibleResponse = True

print(f"--------------------------------------- \n Dia terminado \n\
      Ganancia total: {gananciaTotal} \n\
---------------------------------------")

print("Fin del programa \n #############################################")

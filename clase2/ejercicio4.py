# Crea un programa que calcule el precio final de un producto con descuento. Solicita al usuario el precio original 
# del producto y el porcentaje de descuento. El programa debe calcular y mostrar el precio final utilizando operadores aritméticos.

# Programa creado por Ivan TG

print("Por favor seleccione un articulo \n\
1) Computador de mesa - 1200$ \n Laptop - 2) 1000$ \n 3) Televisor - 1500$ \n\
4) Nevera - 2000$ \n 5) Licuadora - 900$ \n 6) Otro - ?$")
descuento = 0
precio = 0
canContinue = True
article1 = 1200
article2 = 1000
article3 = 1500
article4 = 2000
article5 = 900

eleccion = input("Su eleccion: ")
if eleccion == "1":
    precio = article1

if eleccion == "2":
    precio = article2

if eleccion == "3":
    precio = article3

if eleccion == "4":
    precio = article4

if eleccion == "5":
    precio = article5

if eleccion == "6":
    precio = input("Dijite el precio de lo que compro: ")
    if not precio.isnumeric():
        print("Dijitacion incorrecta, ¡Adios!")
        canContinue = False
    precio = int(precio)

if canContinue:
    print("Dijite su codigo de descuento (caracteres al azar)")
    cadena = input("Escriba un codigo de descuento: ")
    if "A" in cadena:
        descuento += 5
    if "20" in cadena:
        descuento += 2
    if "zzz" in cadena:
        descuento += 4
    if "o" in cadena:
        descuento += 3
    if "h" in cadena:
        descuento += 3
    if "k" in cadena:
        descuento += 3
    if "l" in cadena:
        descuento += 3
    valor = precio * (descuento / 100)
    precio -= valor
    print(f"El precio final a pagar seria: {precio}$, por un descuento de: {descuento}%")
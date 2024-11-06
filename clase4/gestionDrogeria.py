terminarPrograma = False
ventasTotales = 0.0

nombres = []
precios = []
unidades = []
vendidas = []

# Menus
textoMenu = "---------------------------------\n\
¿Que desea hacer? \n\
1) Ingresar productos a stock \n\
2) Vender producto \n\
3) Mostrar Inventario \n\
4) Mostrar Ventas totales \n\
5) Salir del programa \n\
--------------------------------- \n"
numeroNegativo = "A ingresado un numero negativo, se tomara su valor absoluto"

while not terminarPrograma:
   print(textoMenu)
   response = input("Respuesta: ")
   if response == "1":
        cantidad = int(input("Ingrese la cantidad: "))
        if cantidad < 0:
            print(numeroNegativo)
            cantidad *= -1
        for i in range(cantidad):
            print(f"Datos del producto {i+1} (Si este producto ya esta en stock ingrese 0 para asignar el mismo valor)")
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            unidad = int(input("Ingrese las cantidades de este producto: "))
            nombre = nombre.lower()
            # Este if adicional lo hago para que el mensaje solo aparezca una vez
            if precio < 0 or unidad < 0:
                print(numeroNegativo)
            if precio < 0:
                precio *= -1
            if unidad < 0:
                unidad *= -1
            
            # revisamos que no exista este mismo nombre en la lista, si existe se actualizan los datos.
            if nombre in nombres:
                index = nombres.index(nombre)
                unidades[index] += unidad
                if precio > 0:
                    precios[index] = precio
            else:
                nombres.append(nombre)
                precios.append(precio)
                unidades.append(unidad)
                vendidas.append(0)
        print("*** Datos ingresados ***")
        pass
   elif response == "2":
        noExiste = False
        print("Lista de productos")
        for i in range(len(nombres)):
            if unidades[i] > 0:
                print(f"{i+1}. {nombres[i]} ----- {precios[i]}") 
        result = input("ingrese el numero del que desea vender: ")
        cantidadVender = int(input("Cuantas necesita: "))
        if cantidadVender < 0:
            print(numeroNegativo)
            cantidadVender *= -1
        if result.isnumeric():
            result = int(result) - 1
            if result < 0:
                result *= -1
            if result > len(nombres):
                result = len(nombres) - 1
        else:
            for j in range(len(nombres)):
                if nombres == result:
                    result = j
                    noExiste = True                
            pass
        if not noExiste:
            # Declaracion de variables
            nombre = nombres[result]
            precio = precios[result]
            cantidad = unidades[result]
            if cantidadVender >= cantidad:
                print("No hay suficientes productos en almacen")
            elif cantidad > 0:
                unidades[result] -= cantidadVender
                vendidas[result] += cantidadVender
                totalVenta = cantidadVender * precio
                ventasTotales += totalVenta
                print(f"Precio total: {totalVenta}")
        else:
            print("Este producto no esta en stock")
        pass
   elif response == "3":
        print("Lista de productos")
        for i in range(len(nombres)):
            print("\n-------------------------- ")
            print(f" {i+1}. {nombres[i]} \n precio: {precios[i]} \n cantidad en stock: {unidades[i]} \n vendidas: {vendidas[i]}")
            print("-------------------------- ")
        pass
   elif response == "4":
       print(f"Cantidad de ventas totales: {ventasTotales}")
       pass
   elif response == "5":
       print("Gracias por usar")
       terminarPrograma = True
       pass
   else:
       print("Numero equivocado")
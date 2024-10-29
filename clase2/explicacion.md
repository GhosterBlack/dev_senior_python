# Ejercicios de la clase dos

En esta carpeta encontraran los ejercicios pedidos en la
clase.

Trate en lo posible de tener creatividad mas que simplesa, los ejercicios desarrollados cumplen los requerimientos de formas diferente a lo mas sencillo pero asegurandome de que cumplieran su objetivo, sin usar recursos que no se hayan explicado en la clase, exceptuando conceptos que ya se vieron, (operadores y condicionales).

En este archivo mostrare una forma sencilla de realizar los ejercicios que desarrolle mas ampliamente en este desarrollo.

# Ejercicios sencillos.

- Ejercicio 1: Operadores aritmeticos.

```python
num1 = input("Ingrese cualquier numero")

if not (num1.isnumeric()):
  num1 = input("El valor no es un numero")


num2 = input("Ingrese cualquier numero nuevamente")

if not (num2.isdecimal()):
  num2 = input("El segundo valor no es numerico")

num1 = float(num1)
num2 = float(num2)



suma = num1 + num2
resta = num1 - num2
mult = num1 * num2
divi = num1 / num2

print (f"El numero 1 sumado con el numero 2 es: {suma}")
print (f"El numero 1 restado con el numero 2 es: {resta}")
print (f"El numero 1 multiplicado con el numero 2 es: {mult}")
print (f"El numero 1 dividido con el numero 2 es: {divi}")

```
En este ejercicio no se usa ningun ciclo, ni funciones especiales pero se logra hacer el calculo de dos numeros, sumandolos, restandolos, multiplicandolos y dividiendolos

- Ejercicio 2: Escribe un programa que solicite al usuario su edad y su país de residencia. El programa debe verificar si el usuario tiene al menos 18 años y si vive en un país específico (por ejemplo, "España") para determinar si puede votar en las elecciones nacionales.

```python
pedirEdad = input("Por favor digite su edad")

if not (pedirEdad.isnumeric()):
    pedirEdad = input("Por favor digite un numero correcto")

edad = int(pedirEdad)
pais = input("Escriba su pais de residencia")
if edad >= 18:
    print("Usted puede votar en las elecciones nacionales")
else:
    print("Usted aun no puede votar en elecciones nacionales")
```
Como se solicito solo se hace una verificacion de que el valor dijitado es un numero que pueda ser una edad, luego de esto se verifica que esta edad sea mayor a 18.

- Ejercicio 3: Escribe un programa que pida al usuario tres números. El programa debe determinar e imprimir cuál de los tres números es el mayor y cuál es el menor usando operadores relacionales.

``` python
num1 = input("Escriba un numero")

if not num1.isnumeric():
    num1 = input("Escriba un numero correcto")

num2 = input("Escriba un segundo numero")

if not num2.isnumeric():
    num2 = input("Escriba un numero correcto")

num3 = input("Escriba un tercer numero")

if not num3.isnumeric():
    num3 = input("Escriba un numero correcto")

if num1 > num2 and num1 > num3:
    print(f"El primer numero: {num1} es el mayor")

if num2 > num1 and num2 > num3:
    print(f"El segundo numero: {num2} es el mayor")

if num3 > num1 and num3 > num2:
    print(f"El tercer numero: {num3} es el mayor")

```
En este caso se simplifica mucho el ejercicio, simplemente pidiendo los numeros, validandolos y calificando quien es el mayor

- Ejercicio 4: Crea un programa que calcule el precio final de un producto con descuento. Solicita al usuario el precio original del producto y el porcentaje de descuento. El programa debe calcular y mostrar el precio final utilizando operadores aritméticos.

```python
precio = input("Escriba el precio")
if not precio.isnumeric():
    precio = input("Escriba un precio correcto")

descuento = input("Escriba el descuento")
if not descuento.isnumeric():
    descuento = input("Escriba un descuento correcto")

valor = precio * (descuento / 100)
precio -= valor
print(f"El precio a pagar es: {precio}$ con un descuento: {descuento}%")

```
En este caso simplemente pedimos tanto el precio como el descuento y hacemos el procedimiento.

- Ejercicio 5

El ultimo ejercicio ya esta simplificado, por lo que puede simplemente leerlo.



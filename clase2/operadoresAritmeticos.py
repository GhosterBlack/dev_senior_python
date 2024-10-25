num1 = input("Ingrese cualquier numero")

while not (num1.isnumeric()):
  num1 = input("El valor no es un numero")


num2 = input("Ingrese cualquier numero nuevamente")

while not (num2.isdecimal()):
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

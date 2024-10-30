# Escribe un programa que pida al usuario tres números. 
# El programa debe determinar e imprimir cuál de los tres números es el mayor y cuál es el menor usando operadores relacionales.

# Hecho por Ivan TG

# Tomese este programa con humor XD

print("Habian tres niños, manuelito, pedrito y juancito, los tres querian saber quien pesaba mas por lo que se fueron a pesar \n\
cuando se terminaron de pesar, pedrito le pregunto a manuelito cuanto pesaba.")
canContinue = True
manuelito = input("Cuanto peso manuelito? ")
whoishardest = 0
if not manuelito.isnumeric():
    print(f"Manuelito respondio: {manuelito} \n y Pedrito le dijo: Manuelito eres muy raro, Y se fueron a sus casas")
    canContinue = False

if canContinue:
    print(f"Manuelito entonces dijo: peso {manuelito}kg, ¿tu cuanto pesaste?")
    manuelito = int(manuelito)
    pedrito = input("¿Cuanto peso Pedrito? ")
    if not pedrito.isnumeric():
        print("Pedrito respondio: Eso que te importa... Y se fue a su casa")
        canContinue = False

if canContinue:
    pedrito = int(pedrito)
    if manuelito < pedrito:
        print(f"Pedrito entonces le dijo: Estas muy delgado, yo peso {pedrito}. ¿Tu cuanto pesas Juancito?")
        whoishardest = 2
    else:
        print(f"Pedrito dijo: Estas gordisimo, Manuelito, no como yo que peso {pedrito} ¿y tu Juancito?")
        whoishardest = 1
    juancito = input("Cuanto pesa juancito? ")
    if not juancito.isnumeric():
        print("Pedrito le dijo: Sabes que? no me importa... Y pedrito se fue")
        canContinue = True

if canContinue:
    juancito = int(juancito)
    print(f"Juancito respondio: {juancito}kg")
    
    if whoishardest == 1 and juancito < manuelito:
        print("Pedrito se rio y dijo: Ja los dos son tan gordos, pero tu eres el mas gordo, Manuelito")
    if whoishardest == 1 and juancito > manuelito:
        print("Pedrito respondio: Bueno tienes un consuelo Manuelito, Juancito es mas gordo que tu.")
    
    if whoishardest == 2 and juancito < pedrito:
        print("Pedrito dijo: Juancito estas muy gordo, Manuelito tu tienes que engordar un poco")
    if whoishardest == 2 and juancito > pedrito:
        print("Pedrito dijo: Tienen que engordar maaas, como es posible que yo sea el mas pesado")
    
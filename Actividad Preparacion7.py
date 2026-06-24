pasajeros_on = True

while pasajeros_on:

    contador = 1
    niño = 0
    joven = 0
    adulto = 0
    adulto_mayor = 0
    niño_precio = 0
    joven_precio = 0
    adulto_precio = 0
    adulto_mayor_precio = 0
    
    cantidad_pasajeros = int(input("Ingrese la cantidad total de pasajeros: "))

    for a in range (cantidad_pasajeros):

        while True:

            nombre = input(f"Ingrese el nombre del pasajero nro{contador}: ")

            edad = int(input(f"Ingrese la edad del pasajero nro{contador}: "))

            if edad > 0 and edad < 12:
                niño += 1
                contador += 1
                niño_precio += 2000
                break
            elif edad >= 12 and edad < 18:
                joven += 1
                contador += 1
                joven_precio += 3000
                break
            elif edad >= 18 and edad < 60:
                adulto += 1
                contador += 1
                adulto_precio += 5000
                break
            elif edad >= 60:
                adulto_mayor += 1
                contador += 1
                adulto_mayor_precio += 2500
                break
            else:
                print("Error. La edad debe ser un numero positivo distinto de 0")

    print("==============")
    print(" RESULTADO")
    print("==============")
    print(f"Total de Pasajeros: {cantidad_pasajeros}")
    print("------------------------")
    print(f"Pasajeros Niños: {niño}")
    print(f"Total a pagar: {niño_precio}")
    print("------------------------")
    print(f"Pasajeros Jovenes: {joven}")
    print(f"Total a pagar: {joven_precio}")
    print("------------------------")
    print(f"Pasajeros Adultos: {adulto}")
    print(f"Total a pagar: {adulto_precio}")
    print("------------------------")
    print(f"Pasajeros Adultos Mayores: {adulto_mayor}")
    print(f"Total a pagar: {adulto_mayor_precio}")
    print("------------------------")

    while True:

        pregunta_final = input("Desea clasificar mas pasajeros? (si/no): ")

        if pregunta_final.lower() == "si":
            pasajeros_on = True
            break
        elif pregunta_final.lower() == "no":
            pasajeros_on = False
            break
        else:
            print("Error. Debe ingresar (si) o (no)")
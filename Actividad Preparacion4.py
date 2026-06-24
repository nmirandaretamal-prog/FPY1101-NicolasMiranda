interruptor = True
saldo = 500000
cantidad_depositos = 0
cantidad_retiros = 0

while interruptor:

    print("=======================")
    print("    MENU PRINCIPAL")
    print("=======================")
    print("1) Consultar saldo")
    print("2) Depositar")
    print("3) Retirar")
    print("4) Ver movimientos")
    print("5) Salir")
    print("=======================\n")

    while True:

        try:
        
            accion = int(input("Ingrese el numero de la opción que desea realizar: "))
            print("")
            
            if accion > 0 and accion < 6:
                break

            else:
                print("Error. Debe ingresar unicamente numero en el rango de opciones \n")

        except ValueError:
            print(("Error. Ingrese unicamente el numero de la opción a realizar \n"))
 
    if accion == 1:

        print(f"Su saldo disponibles es de: {saldo}$\n")

    elif accion == 2:

        while True:

            try:

                deposito = int(input("Ingrese el monto que desea depositar: "))
                print("")

                if deposito > 0:
                    print("Deposito realizado con éxito\n")
                    saldo += deposito
                    print(f"Su saldo disponibles es de: {saldo}$\n")
                    cantidad_depositos += 1
                    break

                else:
                    print("Error. Unicamente puede depositrar un monto sobre 0\n")
            
            except ValueError:
                print("Error. Monto a depositar inválido\n")

    elif accion == 3:

        while True:

            try:

                retiro = int(input("Ingrese el monto que desea retirar: "))
                print("")

                if retiro > 0 and retiro <= saldo:
                    saldo -= retiro
                    print(f"Su saldo disponibles es de: {saldo}$\n")
                    cantidad_retiros += 1
                    break

                elif retiro > saldo:
                    print("Error. Saldo insuficiente\n")

                else:
                    print("Error. Unicamente puede retirar un monto sobre 0\n")
            
            except ValueError:
                print("Error. Monto a retirar inválido\n")

    elif accion == 4:

        print("---------------------------")
        print("   MOVIMIENTOS Y SALDO")
        print("---------------------------")
        print(f"SALDO:      {saldo}$")
        print(f"RETIROS:    {cantidad_retiros}")
        print(f"DEPOSITOS:  {cantidad_depositos}\n")

    elif accion == 5:

        print("Que tenga buen dia. Adiós")
        interruptor = False
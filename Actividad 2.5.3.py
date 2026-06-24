sw = 1
deuda = 100000
saldo = 500000

while sw == 1:
    try:
        print("1. Pago de Tarjeta de Crédito")
        print("2. Simulación de Compras")
        print("3. Salir")
        opcion = int(input("Ingrese la opción que desea realizar: "))
        
        if opcion > 0 and opcion < 4:
            if opcion == 1:
                while True:
                    monto_ingresar = int(input("Ingrese el monto a pagar: "))
                    if monto_ingresar >= 0:
                        if monto_ingresar <= saldo:
                            deuda -= monto_ingresar
                            saldo -= monto_ingresar
                            print(f"Pago exitoso. Deuda actual: {deuda} | Saldo actual: {saldo}")
                            break
                        else:
                            print(f"El monto ingresado no puede superar el saldo ({saldo}) de la tarjeta")
                    else:
                        print("El monto a ingresar debe ser mayor o igual a 0")
            
            if opcion == 2:
                print("Bienvenido a la simulación de compras")
                nro_compras = int(input("Ingrese el numero de compras a realizar: "))
                total = 0
                nro_compra = 1
                
                for i in range(nro_compras):
                    while True:
                        monto_compra = int(input(f"Ingrese el monto de la compra {nro_compra}: "))
                        if monto_compra >= 0:
                            saldo -= monto_compra
                            total += monto_compra
                            print(f"Compra {nro_compra} procesada. Saldo actual: {saldo}")
                            nro_compra += 1
                            break
                        else:
                            print("El monto de cada compra debe ser mayor o igual a 0")
                            
                if total > 0:
                    print("Simulación de compras finalizada con éxito")
                    print(f"Total gastado: {total}")
                    print(f"Saldo final disponible: {saldo}")
            
            if opcion == 3:
                sw = 0
        else:
            print("Selección fuera de rango")
            
    except ValueError:
        print("Ingreso Erróneo, debe ingresar un valor numérico")
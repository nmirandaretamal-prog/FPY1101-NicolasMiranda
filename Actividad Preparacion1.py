#Activador
menu1_on = True

#Bucle para repetir el menu constantemente
while menu1_on:

    #Variables
    tipo_cliente = None
    nombre_cliente = None
    monto_compra = 0
    porcentaje_descuento = 0
    dcto = 1
    total = 0

    try:
        
        #Input nombre
        nombre_cliente = input("Ingrese su nombre: ")

        #While para válidar datos
        while True:
            
            #Input tipo cliente
            tipo_cliente = input("Ingrese su tipo de cliente (normal, frecuente y premium): ")
            
            #Correccion tipo cliente
            if tipo_cliente.lower() == "normal" or tipo_cliente.lower() == "frecuente" or tipo_cliente.lower() == "premium":
                break
            else:
                print("Tipo de cliente no valido. Ingrese nuevamente")
        
        #While para válidar datos
        while True:

            #Input monto
            monto_compra = int(input("Ingrese el monto de su compra: "))

            #Matematica y cálculo
            if monto_compra <= 20000 and monto_compra > 0:
                porcentaje_descuento = 0
                break

            elif monto_compra > 20000 and monto_compra < 49999:
                porcentaje_descuento = 8
                dcto = 0.92
                break

            elif monto_compra > 50000:
                porcentaje_descuento = 15
                dcto = 0.85
                break

            else:
                print("el monto no puede ser negativo...")

        #Descuento Adicional
        if tipo_cliente == "premium":
            porcentaje_descuento += 5
            dcto -= 0.05
        
        elif tipo_cliente == "frecunete" and monto_compra >= 30000:
            porcentaje_descuento += 3
            dcto -= 0.03

        #Calculo del total
        total = monto_compra * dcto
        
        #Mostrar al cliente
        print("**********************")
        print("Resultado de compras")
        print("**********************")
        print(f"Nombre: {nombre_cliente}")
        print(f"Tipo cliente: {tipo_cliente.lower()}")
        print(f"Monto bruto: {monto_compra}$")
        print(f"Porcentaje de descuento: {porcentaje_descuento:.0f}%")
        print(f"Total final: {total:.0f}$")
        
        #Pregunta final
        pregunta_final = input("Desea realizar otra compra (si/no): ")
        
        #Decisión
        if pregunta_final.lower() == "no":
            menu1_on = False
        elif pregunta_final.lower() == "si":
            menu1_on = True
    
    #Except
    except ValueError:
        print("Error al ingresar algun dato")
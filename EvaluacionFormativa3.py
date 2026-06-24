#Variable para controlar la repetición de los menus
sw = 1
sw1 = 1
sw2 = 1
sw3 = 1
sw4 = 1

while sw == 1:

    #Asignación de variables
    pedidos = 0
    total = 0
    total_final = total
    Pikachu_Roll = 0
    Otaku_Roll = 0
    Pulpo_Venenoso_Roll = 0
    Anguila_Eléctrica_Roll = 0
    descuento = None
    limite = 6
    descuento = 0

    #Estructura de repetición para el menu
    while sw1 == 1:

        #estructura try para asegurarse que el usuario ingrese correctamente sus compras
        try:

            #Menu de opciones para el cliente
            print("Bienvenido a SushiRoll \n")
            print("1) Pikachu Roll $4500")
            print("2) Otaku Roll $5000")
            print("3) Pulpo Venenoso Roll $5200")
            print("4) Anguila Eléctrica Roll $4800")
            print("5) Continuar")
            print("6) Salir \n")

            #Se recive la respuesta del usuario
            opciones = int(input("Ingrese una opción: \n"))

            #Uso de estructura if en caso de que el usuario desee salir sin concretar la compra
            if opciones == 6:
                print("Que tenga buen dia")
                sw1 == 0
                quit()
            elif opciones > limite:
                raise ValueError("Debe ingresar una opción válida \n")
            elif opciones == 5:
                break

            cantidad = int(input("Ingrese cuantos desea llevar: \n"))

            #Estructura de repetición para las respuestas dl usuario
            if opciones == 1:
                Pikachu_Roll += cantidad
                pedidos += cantidad
                total += 4500 * cantidad
            elif opciones == 2:
                Otaku_Roll += cantidad
                pedidos += cantidad
                total += 5000 * cantidad
            elif opciones == 3:
                Pulpo_Venenoso_Roll += cantidad
                pedidos += cantidad
                total += 5200 * cantidad
            elif opciones == 4:
                Anguila_Eléctrica_Roll += cantidad
                pedidos += cantidad
                total += 4800 * cantidad

            else:
                print("debe ingresar una opción válida")

        #Uso de estructura except en caso de que el usuario ingrese una opción invalida 
        except Exception as e:
            print(f"Ingreso erroneo {e}")     
        
    #Estructura While para continuar con el descuento 
    while sw2 == 1:    
        
        #estructura try para asegurar que el usuario ingrese una opción válida
        try:

                #Se le pregunta al usuario si posee un código
                pregunta_codigo = input("Tiene algun codigo de descuento (si/no): \n")
            
                #Estructura de decision en caso de que el usuario tenga un codigo
                if pregunta_codigo.lower() == "si":

                    #Estructura While para que el usuario ingrese correctamente el código
                    while sw3:

                        #Se solicita al usuario que ingrese el codigo 
                        codigo_dcto = input("Ingrese su codigo de descuento: ")
                        
                        #Estructuras de desición para el ingreso del código
                        if codigo_dcto.lower() == "soyotaku":
                            descuento = total * 0.10
                            total_final = total * 0.90
                            sw2 = 0
                            sw3 = 0
                        elif codigo_dcto.lower() == "x":
                            print("Procediendo con la compra...\n")
                            sw3 = 0
                        else:
                            print("Debe ingresar un código válido o la letra (x) para cancelar el codigo de descuento\n")
                            total_final = total
                    sw2 = 0
        
                elif pregunta_codigo.lower() == "no":
                    sw2 = 0
                    total_final = total
                else:
                    print("Debe ingresar si o no unicamente \n")

        #Uso de estructura except en caso de que el usuario ingrese una opción invalida    
        except Exception as e:
            print(f"Ingreso erroneo {e}\n")

    #se muestra el resultado de la compra
    print("******************************")
    print(f"TOTAL PRODUCTOS:{pedidos}")
    print("******************************")
    print(f"Pikachu Roll : {Pikachu_Roll}")
    print(f"Otaku Roll: {Otaku_Roll}")
    print(f"Pulpo Venenoso Roll: {Pulpo_Venenoso_Roll}")
    print(f"Anguila Eléctrica Roll: {Anguila_Eléctrica_Roll}")
    print("******************************")
    print(f"Subtotal por pagar: ${total:.0f}")
    print(f"Descuento por código: ${descuento:.0f}")
    print(f"TOTAL: ${total_final:.0f}")   

    respuesta_final = input("Desea realizar otra compra? (si/no): ")
    if respuesta_final.lower() == "si":
        sw = 1
        sw1 = 1
        sw2 = 1
        sw3 = 1
        print("Volviendo al menu principal... \n")
    elif respuesta_final.lower() == "no":
        sw = 0
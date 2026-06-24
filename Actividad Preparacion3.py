interruptor = True

while interruptor:

    user1 = "admin"
    user2 = "docente"
    user1_pw = "1234"
    user2_pw = "duoc2026"
    contador_user = 1
    contador_pw = 1
    marcador1 = 3
    marcador2 = 3

    while True:
    
        intento_user = input(f"Ingrese el usuario al que desea acceder. Intento numero {contador_user}: ")

        if intento_user == user1:
            break

        elif intento_user == user2:
            break

        else:
            print("")
            print(f"Error. Usuario inexistente. Intentos restantes ({marcador1})")

            if contador_user == 3:
                print("Maxima cantidad de errores alcanzada.")
                exit()

            contador_user += 1
            marcador1 -= 1

    while True:

        intento_userpw = input(f"Ingrese la contraseña del usuario. Intento numero {contador_pw}: ")

        if intento_user == user1 and intento_userpw == user1_pw:
            print("Acceso concedido")
            break

        elif intento_user == user2  and intento_userpw == user2_pw:
            print("Acceso concedido")
            break

        else:
            print("")
            print(f"Error. Contaseña incorrecta. Intentos restantes ({marcador1})")

            if contador_pw == 3:
                print("Maxima cantidad de errores alcanzada.")
                exit()

            contador_pw += 1
            marcador2 -= 1
    
    while True:    
        
        pregunta_final = input("Desea ingresar a otro usuario? (si/no): ")

        if pregunta_final.lower() == "si":
            interruptor = True
            break

        elif pregunta_final.lower() == "no":
            interruptor = False
            break

        else:
            print("Respuesta incorrecta. Ingrese nuevamente")
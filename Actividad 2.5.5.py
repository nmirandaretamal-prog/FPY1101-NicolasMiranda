sw = 1
usuario1 = None
usuario2 = None
usuario3 = None
contrasena1 = None
contrasena2 = None
contrasena3 = None

while sw == 1:
    print("1) iniciar sesión")
    print("2) registrar usuario")
    print("3) salir")
    
    try:
        accion = int(input("Seleccione una opción: "))
        
        if(accion > 0 and accion < 4):
            if accion == 1:
                if usuario1 == None and usuario2 == None and usuario3 == None:
                    print("es necesario registrar un usuario antes")
                else:
                    user_ingreso = input("Ingrese usuario: ")
                    pass_ingreso = input("Ingrese contraseña: ")
                    
                    acceso = 0
                    if user_ingreso == usuario1 and pass_ingreso == contrasena1 and usuario1 != None:
                        acceso = 1
                    if user_ingreso == usuario2 and pass_ingreso == contrasena2 and usuario2 != None:
                        acceso = 1
                    if user_ingreso == usuario3 and pass_ingreso == contrasena3 and usuario3 != None:
                        acceso = 1
                    
                    if acceso == 1:
                        sw2 = 1
                        while sw2 == 1:
                            print("1) Realizar llamada")
                            print("2) Enviar correo electrónico")
                            print("3) Cerrar sesión")
                            accion2 = int(input("Seleccione una opción: "))
                            
                            if(accion2 > 0 and accion2 < 4):
                                if accion2 == 1:
                                    celular = input("Ingrese número de celular: ")
                                    conteo_largo = 0
                                    for caracter in celular:
                                        conteo_largo = conteo_largo + 1
                                    
                                    if conteo_largo == 9:
                                        if celular[0] == "9":
                                            print(f"Llamando al número {celular}...")
                                        else:
                                            print("El número debe empezar con 9")
                                    else:
                                        print("El número debe tener 9 dígitos")
                                
                                if accion2 == 2:
                                    valido = 0
                                    while valido == 0:
                                        correo_input = input("Ingrese correo electrónico: ")
                                        encontrado = 0
                                        for c in correo_input:
                                            if c == "@":
                                                encontrado = 1
                                        
                                        if encontrado == 1:
                                            correo = correo_input
                                            mensaje = input("Ingrese el mensaje a enviar: ")
                                            print(f"Correo {correo} enviado")
                                            valido = 1
                                            sw2 = 0 # Vuelve al menú principal
                                        else:
                                            print("Error: el correo debe tener al menos un @")
                                
                                if accion2 == 3:
                                    print("Cierre de sesión exitoso")
                                    sw2 = 0
                            else:
                                print("Selección fuera de rango")
                    else:
                        print("Usuario o contraseña incorrecta")

            if accion == 2:
                u_nuevo = input("Ingrese nuevo usuario: ")
                c_nueva = input("Ingrese nueva contraseña: ")
                
                if usuario1 == None:
                    usuario1 = u_nuevo
                    contrasena1 = c_nueva
                    print("Usuario 1 registrado")
                elif usuario2 == None:
                    usuario2 = u_nuevo
                    contrasena2 = c_nueva
                    print("Usuario 2 registrado")
                elif usuario3 == None:
                    usuario3 = u_nuevo
                    contrasena3 = c_nueva
                    print("Usuario 3 registrado")
                else:
                    print("No hay más espacio para registrar usuarios")

            if accion == 3:
                print("Cierre de sesión exitoso, adiós")
                sw = 0
        else: 
            print("Selección fuera de rango")
            
    except Exception as e:
        print(f"Ingreso Erróneo: {e}")
biblioteca_on = True

nombre = None
prestamos = 0
ultimo_libro = None

while biblioteca_on:

    print("====================================")
    print(" PRESTAMOS Y ESTADISTICAS")
    print("====================================")
    print("1) Registrar prestamo")
    print("2) Buscar libro")
    print("3) Ver Estadisticas")
    print("4) Salir")

    libro_1 = "mein kampf"
    libro_2 = "principito"
    libro_3 = "manual de manuales"

    while True:
        accion = int(input("Ingrese la opcion que desea realizar: "))

        if accion > 0 and accion < 5:
            break
        else:
            print("Error. Debe elegir una opción disponible")

    if accion == 1:

        nombre = input("Ingrese su nombre: ")
            
        while True:    
            
            libro = input("Ingrese el libro que deesea arrendar o escriba (salir): ")

            if libro == libro_1:
                prestamos += 1
                ultimo_libro = "mein kampf"  
                print("Préstamo registrado con exito")
                break

            elif libro == libro_2:
                prestamos += 1
                ultimo_libro = "principito"  
                print("Préstamo registrado con exito")
                break

            elif libro == libro_3:
                prestamos += 1
                ultimo_libro = "manual de manuales"  
                print("Préstamo registrado con exito")
                break

            elif libro == "salir":
                print("Cancelando Prestamo y volviendo a menu...\n")
                break 
            else:
                print("Error. El libro no existe o el ingreso fue inválido") 

    if accion == 2:

        while True:
        
            buscador = input("Ingrese el libro que esta buscando o escriba (salir): ")

            if buscador.lower() == libro_1 or buscador.lower() == libro_2 or buscador.lower() == libro_3:
                print("Libro disponible")
                break
                
            elif buscador.lower() == "salir":
                print("Cancelando busqueda y volviendo al menu...\n")
                break
            
            else:
                print("el libro no existe o en ingreso fue invalido")

    if accion == 3:

        print("===================")
        print("  ESTADISTICAS")
        print("===================")
        print(f"Total de prestamos: {prestamos}")
        print(f"Ultimo libro solicitado: {ultimo_libro}\n")

    if accion == 4:
        print("Gracias por venir")
        biblioteca_on = False
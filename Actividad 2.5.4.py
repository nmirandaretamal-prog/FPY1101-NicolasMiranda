while True:
    print("1. Calcular pisos de la pirámide")
    print("2. Salir")
    
    try:
        opcion = int(input("Ingrese una opción: "))
        
        if opcion == 1:
            print("")
            ladrillos = int(input("Introduzca el número de ladrillos disponibles: "))
            altura = 0
            utilizados = 0
            por_fila = 1
            
            while utilizados < ladrillos:
                altura = altura + 1
                por_fila = por_fila + 1
                utilizados = utilizados + por_fila
                
            print("La altura de la pirámide es de: ", altura)
            print("")
            
        if opcion == 2:
            break
            
        if opcion < 1 or opcion > 2:
            print("Opción no válida")
            
    except:
        print("Error en el ingreso")
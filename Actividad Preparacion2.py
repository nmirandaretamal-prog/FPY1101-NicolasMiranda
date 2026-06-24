#Interruptor loop principal
alumnos_on = True

#While principal
while alumnos_on:

    #Variables
    cantidad_alumnos = 0
    presentes = 0
    ausentes = 0
    justificados = 0
    presentes_totales = 0
    porcentaje_presentes = 0
    estado_curso = None
    contador = 1

    #Try para válidar correcto ingreso de datos
    try:

        cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))

        #While para correcto ingreso de datos
        for a in range (cantidad_alumnos):
        
            while True:

                #Inputs para datos
                nombre_alumnos = input(f"Ingrese el nombre del alumno {contador}: ")
                print("P) Presente A) Ausente J) Justificado")
                estado_asistencia = input(f"Ingrese el estado de asistencia del alumno {contador}: ")

                #Condicionales para almacenar los datos
                if estado_asistencia.lower() == "p":
                    presentes += 1
                    contador += 1
                    break                

                elif estado_asistencia.lower() == "a":
                    ausentes += 1
                    contador += 1
                    break

                elif estado_asistencia.lower() == "j":
                    justificados += 1
                    contador += 1
                    break
                else:
                    print("Ingrese los datos correctamente")

        #Matematica segun los datos
        presentes_totales = presentes + justificados
        porcentaje_presentes = (presentes_totales / cantidad_alumnos ) * 100

        if porcentaje_presentes == 100:
            estado_curso = "Curso con asistencia perfecta" 
        
        elif porcentaje_presentes < 75:
            estado_curso = "Curso con asistencia crítica"

        elif porcentaje_presentes >= 75:
            estado_curso = "Curso con asistencia aceptable"

        print("======================")
        print("   REPORTE FINAL")
        print("======================")
        print(f"Alumnos Totales: {cantidad_alumnos}")
        print("----------------------")
        print(f"Alumnos presentes: {presentes}")
        print(f"Alumnos Ausentes: {ausentes}")
        print(f"Alumnos Justificados: {justificados}")
        print("----------------------")
        print(f"Estado del curso: {estado_curso} \n")

        while True:
            pregunta_final = input("Desea pasar asistencia nuevamente (si/no): ")
            if pregunta_final.lower() == "si":
                alumnos_on = True
                break
            elif pregunta_final.lower() == "no":
                alumnos_on = False
                break
            else:
                print("Responda correctamente")

    #Except para el try            
    except ValueError:
        print("Error al ingresar los datos")    
def validar_nota(mensaje):
    while True:
        try:
            nota = float(input(mensaje))
            if 1.0 <= nota <= 7.0:
                return nota
            else:
                print("Error: La nota debe estar entre 1.0 y 7.0.")
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")

def calcular_promedio(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

def mostrar_estado_academico(nombre, promedio):
    print("\n--- ESTADO ACADÉMICO ---")
    print(f"Alumno: {nombre}")
    print(f"Promedio Final: {promedio:.1f}")
    if promedio >= 4.0:
        print("Estado: APROBADO")
    else:
        print("Estado: REPROBADO")
    print("------------------------")

def main():

    nombre_alumno = ""
    promedio_actual = 0.0
    datos_registrados = False

    while True:
        print("\n=== MINI ERP ACADÉMICO ===")
        print("1. Registrar alumno y notas")
        print("2. Mostrar estado académico")
        print("3. Salir")
        
        opcion = input("Seleccione una opción (1-3): ")
        
        if opcion == '1':
            nombre_alumno = input("\nIngrese nombre del alumno: ")
            print("Ingrese las 3 notas del alumno:")
            n1 = validar_nota("Nota 1: ")
            n2 = validar_nota("Nota 2: ")
            n3 = validar_nota("Nota 3: ")
            
            promedio_actual = calcular_promedio(n1, n2, n3)
            datos_registrados = True
            print("¡Datos registrados exitosamente!")
            
        elif opcion == '2':
            if datos_registrados:
                mostrar_estado_academico(nombre_alumno, promedio_actual)
            else:
                print("\nError: Primero debe registrar a un alumno (Opción 1).")
                
        elif opcion == '3':
            print("\nSaliendo del sistema ERP. ¡Hasta luego!")
            break 
            
        else:
            print("\nOpción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()

    # Mejora: Se añadió este comentario para control de versiones en GitHub
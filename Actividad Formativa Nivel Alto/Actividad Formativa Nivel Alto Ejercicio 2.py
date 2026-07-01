def registrar_usuario():
    nombre = input("Ingrese el nombre del estudiante: ")
    carrera = input("Ingrese la carrera del estudiante: ")
    return nombre, carrera

def registrar_libro():
    libro = input("Ingrese el título del libro: ")
    while True:
        try:
            dias = int(input("Ingrese la cantidad de días de préstamo: "))
            if dias <= 0:
                print("Los días deben ser mayores a 0.")
                continue
            return libro, dias
        except ValueError:
            print("Por favor, ingrese un número entero de días.")

def generar_resumen(nombre, carrera, libro, dias):
    print("\n--- REPORTE DE RESERVA ---")
    print(f"Estudiante: {nombre}")
    print(f"Carrera: {carrera}")
    print(f"Libro solicitado: {libro}")
    print(f"Días de préstamo: {dias}")

    if dias > 14:
        print("ADVERTENCIA: El préstamo supera el límite estándar de 14 días. Sujeto a multas por retraso.")

def main():
    print("--- SISTEMA DE RESERVAS DE BIBLIOTECA ---")

    print("\n--- Datos del Usuario ---")
    nombre_usuario, carrera_usuario = registrar_usuario()
    
    print("\n--- Datos del Libro ---")
    titulo_libro, dias_prestamo = registrar_libro()

    generar_resumen(nombre_usuario, carrera_usuario, titulo_libro, dias_prestamo)

if __name__ == "__main__":
    main()

    # Mejora: Se añadió este comentario para control de versiones en GitHub
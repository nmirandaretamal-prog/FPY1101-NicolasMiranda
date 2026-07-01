def validar_temperatura():
    while True:
        try:

            temp = float(input("Ingrese una temperatura: "))
            return temp 
        except ValueError:
 
            print("Error: Dato inválido. Por favor ingrese un valor numérico.")

def calcular_promedio(lista_temperaturas):
    suma = sum(lista_temperaturas)
    cantidad = len(lista_temperaturas)
    return suma / cantidad

def obtener_alerta(promedio):
    if promedio > 30:
        return "ALERTA: Temperatura promedio crítica (calor excesivo)."
    elif promedio < 5:
        return "ALERTA: Temperatura promedio crítica (frío extremo)."
    else:
        return "Estado estable: Temperaturas dentro del rango normal."

def main():
    print("--- SISTEMA DE GESTIÓN DE TEMPERATURAS ---")
    temperaturas = []

    for i in range(5):
        print(f"\nRegistro {i+1} de 5:")
        temp_valida = validar_temperatura()
        temperaturas.append(temp_valida)

    promedio = calcular_promedio(temperaturas)
    alerta = obtener_alerta(promedio)

    print("\n--- REPORTE FINAL ---")
    print(f"Temperaturas registradas: {temperaturas}")
    print(f"Temperatura promedio: {promedio:.2f}°C")
    print(f"Estado: {alerta}")

if __name__ == "__main__":
    main()
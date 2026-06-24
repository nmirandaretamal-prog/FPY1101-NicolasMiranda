nombre = input("Ingrese su nombre: ")

while True:
        edad = int(input("Ingrese su edad: "))
        if edad >= 0:
            break
        else:
            print("Error: La edad no puede ser negativa")
while True:
    tipo_entrada = input("Tipo de entrada (General/VIP): ").strip().lower()
    if tipo_entrada in ['general', 'vip']:
        break
    else:
        print("Error: Ingrese 'General' o 'VIP'.")

dias_validos = ['lunes', 'martes', 'miercoles', 'miércoles', 'jueves', 'viernes', 'sabado', 'sábado', 'domingo']
while True:
    dia = input("Día de la semana: ").strip().lower()
    if dia in dias_validos:
        break
    else:
        print("Error: Día ingresado no válido.")

estudiante = input("¿Es estudiante? (si/no): ").strip().lower() == 'si'
premium = input("¿Posee membresía Premium? (si/no): ").strip().lower() == 'si'

if tipo_entrada == 'general':
    valor_base = 9000
else:
    valor_base = 15000

porcentaje_descuento = 0.0

if edad >= 60:
    porcentaje_descuento += 0.25
elif estudiante:
    dias_semana = ['lunes', 'martes', 'miercoles', 'miércoles', 'jueves']
    if dia in dias_semana:
        porcentaje_descuento += 0.20
    else:
        porcentaje_descuento += 0.10

if premium:
    porcentaje_descuento += 0.05
    if tipo_entrada == 'vip':
        porcentaje_descuento += 0.03

descuento_total_dinero = int(valor_base * porcentaje_descuento)
valor_final = valor_base - descuento_total_dinero

print("\n    RESUMEN DE COMPRA ")
print(f"Cliente: {nombre}")
print(f"Tipo de entrada: {tipo_entrada.capitalize()}")
print(f"Valor base: ${valor_base}")
print(f"Descuento total aplicado: ${descuento_total_dinero} ({(porcentaje_descuento * 100):.0f}%)")
print(f"Valor final: ${valor_final}")
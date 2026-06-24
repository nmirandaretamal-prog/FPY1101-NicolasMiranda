import random

nombre = input("Ingrese su nombre de usuario: ")
pin = input("Ingrese su PIN secreto: ")
nivel_acceso = input("Ingrese el nivel de acceso: ")

codigo_secreto = random.randint(0, 10)

if codigo_secreto % 2 != 0:
    codigo_secreto += 1

print("Se ha generado un código numérico aleatorio. Tienes 3 intentos para descifrarlo")

intento_1_usuario = 0
intento_2_usuario = 0
intento_3_usuario = 0

for intento in range (1, 4):
    adivinanza_usuario= int(input(f"Intento: {intento}/3 - Ingrese el código: "))

    if adivinanza_usuario == codigo_secreto:
        if intento == 1:
            print("Acceso inmediato")
        elif intento == 2:
            print("Acceso parcial")
        elif intento == 3:
            print("Acceso Restringido")   
        break
    else:
        if intento == 1:
            intento_1_usuario = adivinanza_usuario
            if codigo_secreto > adivinanza_usuario:
                print("Incorrecto. El código secreto es mayor")
            else:
                print("Incorrecto. El código secreto es menor")
        elif intento == 2:
            intento_2_usuario = adivinanza_usuario
            intento_1 = abs(codigo_secreto - intento_1_usuario)
            intento_2 = abs(codigo_secreto - intento_2_usuario)

            if intento_1 < intento_2:
                print("Incorrecto. El primer intento estuvo mas cerca")
            elif intento_2 < intento_1:
                print("Incorrecto. El segundo intento estuvo mas cerca")
            else:
                print("Incorrecto. Ambos intento estan a la misma distancia")
        elif intento == 3:
            print(f"Accesp bloqueado. El codigo era: {codigo_secreto}")
print("Bienvenido a Matriculas DuocUC")
nombre=input("Igrese su nombre completo: ")
carrera=input("Ingrese la carrera deseada: ")
matricula=int(input("Ingrese el valor de la matricula: "))
mensualidad=int(input("Ingrese el valor de la mensualidad: "))
meses_a_pagar=int(input("Ingrese la cantidad de meses que pagara: "))

costo_anual=mensualidad*12
subtotal=(meses_a_pagar*mensualidad)+matricula

if meses_a_pagar >= 10:
    descuento="5%"
    total_final=subtotal*0.95

print("")
print(f"\t\tMATRICULAS DUOC\nNOMBRE:\t\t{nombre}\nCARRERA:\t{carrera}")
print(f"MATRICULA:\t{matricula}\nMENSUALIDAD:\t{mensualidad}")
print(f"MESES A PAGAR:\t{meses_a_pagar}\nCOSTO ANUAL:\t{costo_anual}")
print(f"DESCUENTO:\t{descuento}\nSUBTOTAL:\t{subtotal}\nTOTAL:\t\t{total_final}")
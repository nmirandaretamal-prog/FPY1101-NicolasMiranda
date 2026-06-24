"""nombre_t=input("Ingrese su nombre: ")
horas_t=int(input("Ingrese sus horas trabajadas: "))
valor_h=int(input("Ingrese el valor por hora: "))
sueldo_base=(horas_t*valor_h*30)
sueldo_final=sueldo_base+25000+30000
print("")
print("\tRESUMEN")
print("")
print(f"\nNOMBRE: {nombre_t} \nHORAS TRABAJADAS: {horas_t} \nVALOR POR HORA: {valor_h} \nSUELDO BASE: {sueldo_base} \nMOVILIZACIÓN: 25000 \nCOLACION: 30000 \nSUELDO FINAL: {sueldo_final}")"""

"""nombre=input("Ingrese su nombre: ")
print("")
nombre_producto=input("Ingrse el nombre del producto: ")
precio_producto=int(input("Ingrse el precio del producto: "))
cantidad_producto=int(input("Ingrese la cantidad del producto: "))

nombre_producto1=input("Ingrse el nombre del producto: ")
precio_producto1=int(input("Ingrse el precio del producto: "))
cantidad_producto1=int(input("Ingrese la cantidad del producto: "))

nombre_producto2=input("Ingrse el nombre del producto: ")
precio_producto2=int(input("Ingrse el precio del producto: "))
cantidad_producto2=int(input("Ingrese la cantidad del producto: "))

total_bruto=(precio_producto*cantidad_producto)+(precio_producto1*cantidad_producto1)+(precio_producto2*cantidad_producto2)
if total_bruto >= 20000:
    total_final=total_bruto*0.90
else:
    total_final=total_bruto
print("")
print(f"\t\tRESUMEN DE COMPRA\nNOMBRE: \t\t{nombre}\nPRIMER PRODUCTO:\t{nombre_producto} \nPRECIO:\t\t\t{precio_producto} \nCANTIDAD:\t\t{cantidad_producto}")
print(f"\nSEGUNDO PRODUCTO:\t{nombre_producto1} \nPRECIO:\t\t\t{precio_producto1} \nCANTIDAD:\t\t{cantidad_producto1}") 
print(f"\nTERCER PRODUCTO:\t{nombre_producto2} \nPRECIO:\t\t\t{precio_producto2} \nCANTIDAD:\t\t{cantidad_producto2}")
print(f"\nSUBTOTAL:\t\t{total_bruto} \nTOTAL A PAGAR:\t\t{total_final}")"""

"""nombre=input("Ingrese su nombre: ")
nota1=float(input("ingrese su primera nota: "))
nota2=float(input("ingrese su segunda nota: "))
nota3=float(input("ingrese su tercera nota: "))
nota4=float(input("ingrese su cuarta nota: "))

promedio=(nota1+nota2+nota3+nota4)/4


if promedio <= 4.0:
    restante_para_aprobar=4.0-promedio
    print(f"Su nota es: {promedio:.2f}")
    print(f"Si desea aprobar necesita: {restante_para_aprobar:.2f} puntos para aprobar ")
else:
    print(f"Su nota es: {promedio:.2f}")
    print("Ustes ha aprobado el curso")"""

"""nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
carrera=input("Ingrse su carrera: ")
año_ingreso=(input("Ingrese su año de ingreso: "))

class usuario_institucional:
    def __init__(self,nombre,correo):
        self.nombre=nombre
        self.correo=correo

nombre_usuario=nombre[:2]+apellido[:2]+año_ingreso
correo_usuario=nombre_usuario+"@gmail.com"

primer_usuario=usuario_institucional(nombre_usuario, correo_usuario)

print(f"USUARIO:\t{primer_usuario.nombre}")
print(f"GMAIL:\t\t{primer_usuario.correo}")"""

nombre=input("Ingrese su nombre: ")
edad=input("Ingrese su edad: ")
prevision=input("Ingrese su previción: ")
consulta=int(input("Ingrese el valor de su consulta: "))

if prevision.lower() == "isapre":
    descuento="20%"
    total=consulta*0.80
elif prevision.lower() == "fonasa":
    descuento="10%"
    total=consulta*0.90

print("")
print("\t\tCOMPROBANTE")
print("")
print(f"NOMBRE:\t\t{nombre}\nEDAD:\t\t{edad}")
print(f"TOTAL BRUTO:\t{consulta}\nDESCUENTO:\t{descuento}\nTOTAL A PAGAR:\t{total}")
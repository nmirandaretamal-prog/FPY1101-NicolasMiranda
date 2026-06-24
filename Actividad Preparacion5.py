calculadora_on = True

while calculadora_on:

    nombre = None
    nota = 0
    pre_promedio = 0.0
    nota_mayor = 7
    nota_menor = 0
    estado = None
    contador = 1
            
    nombre = input("Ingrese el nombre del alumno: ")
    cantidad_ev = int(input("Ingrese el total de evaluaciones: "))

    for a in range (cantidad_ev):

        while True:

            nota = float(input(f"Ingrese la nota {contador}: "))

            if nota >= 2 and nota <= 7:
                contador += 1
                pre_promedio += nota
                break

            else:
                print("Debe ingresar una nota válida")
                
        if nota > nota_menor:
            nota_menor = nota

        if nota < nota_mayor:
            nota_mayor = nota

    promedio_final = pre_promedio / cantidad_ev
    
    if promedio_final >= 4:
        estado = "Aprobado"
    else:
        estado = "Reprobado"
        
    print("=========================")
    print("    RESULTADO ")
    print("=========================")
    print(f"Nombre: {nombre}")
    print(f"Promedio: {promedio_final:.1f}")
    print(f"Nota más alta: {nota_mayor}")
    print(f"Nota más baja: {nota_menor}")
    print(f"Estado: {estado}")

    while True:    
        
        pregunta_final = input("Desea calcular el promedio de otro estudiante (si/no): ")

        if pregunta_final.lower() == "si":
            calculadora_on = True
            break

        elif pregunta_final.lower() == "no":
            calculadora_on = False
            break

        else:
            print("Respuesta incorrecta. Ingrese nuevamente")
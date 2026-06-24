tienda_on = True

while tienda_on:

    subtotal = 0

    cantidad_productos = int(input("Ingrese el total de productos: "))
    contador = 1
    descuento = "0%"

    for a in range (cantidad_productos):

        nombre_producto = input(f"Ingrese el nombre del producto {contador}: ")

        while True:

            valor_producto = int(input(f"Ingrese el valor del producto {contador}: "))
            cantidad_unitaria = int(input(f"Ingrese la cantidad que llevara del producto {contador}: "))

            if valor_producto > 0 and cantidad_unitaria > 0:
                contador += 1
                producto_final = valor_producto * cantidad_unitaria
                subtotal += producto_final
                break
            else:
                print("El valor o la cantidad del producto no pueden ser 0 o negativo")

    if subtotal > 100000:
        subtotal *= 0.90
        descuento = "10%"

    total = subtotal * 1.19

    print("===============")
    print("   BOLETA")
    print("===============")
    print(f"Cantidad de productos: {cantidad_productos}")
    print(f"Subtotal: {subtotal}")
    print(f"descuento: {descuento}")
    print("IVA: 19%")
    print(f"Total Final: {total:.0f}")

    while True:    
    
        pregunta_final = input("Desea registrar nuevas ventas? (si/no): ")

        if pregunta_final.lower() == "si":
            tienda_on = True
            break

        elif pregunta_final.lower() == "no":
            tienda_on = False
            break

        else:
            print("Respuesta incorrecta. Ingrese nuevamente")
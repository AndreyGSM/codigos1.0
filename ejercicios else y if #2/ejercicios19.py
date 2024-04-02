

valor_unitario = float(input("Ingrese el valor unitario de cada artículo: "))

cantidad_articulos = int(input("Ingrese la cantidad de artículos: "))

total_sin_descuento = valor_unitario * cantidad_articulos

if total_sin_descuento < 20000:
    descuento = total_sin_descuento * 0.15
else:
    descuento = total_sin_descuento * 0.35

total_con_descuento = total_sin_descuento - descuento

print(f"El total a pagar es: ${total_con_descuento:.2f}")

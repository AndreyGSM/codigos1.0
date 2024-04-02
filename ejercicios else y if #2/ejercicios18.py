
cantidad_articulos = int(input("Ingrese la cantidad de artículos: "))

valor_unitario = float(input("Ingrese el valor unitario de cada artículo: "))

total_sin_descuento = cantidad_articulos * valor_unitario

if total_sin_descuento > 100000:
   
    descuento = total_sin_descuento * 0.20
   
    total_con_descuento = total_sin_descuento - descuento
else:
    total_con_descuento = total_sin_descuento

print(f"El total a pagar es: ${total_con_descuento:.2f}")

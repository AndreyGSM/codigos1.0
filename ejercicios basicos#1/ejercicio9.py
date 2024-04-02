valor_unitario = float(input("Ingrese el valor unitario del producto: "))
cantidad = int(input("Ingrese la cantidad de productos comprados: "))
subtotal = valor_unitario * cantidad  
iva = subtotal * 0.16
total_pagar = subtotal + iva
print(f"Subtotal: {subtotal} unidades monetarias")
print(f"IVA: {iva} unidades monetarias")
print(f"Total a pagar: {total_pagar} unidades monetarias")

valor_compra = float(input("Ingrese el valor total de la compra: "))

if 10000 <= valor_compra <= 20000:
    descuento = valor_compra * 0.10
elif 20001 <= valor_compra <= 50000:
    descuento = valor_compra * 0.30
else:
    descuento = valor_compra * 0.50

valor_final = valor_compra - descuento

print(f"El valor final a pagar es: ${valor_final:.2f}")

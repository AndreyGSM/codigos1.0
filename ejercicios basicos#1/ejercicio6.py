
def calcular_porcentaje(numero, porcentaje):
    return (numero * porcentaje) / 100
numero = float(input("Ingrese el número: "))
porcentaje_30 = calcular_porcentaje(numero, 30)
porcentaje_60 = calcular_porcentaje(numero, 60)
porcentaje_90 = calcular_porcentaje(numero, 90)

print(f"El 30% de {numero} es {porcentaje_30}")
print(f"El 60% de {numero} es {porcentaje_60}")
print(f"El 90% de {numero} es {porcentaje_90}")
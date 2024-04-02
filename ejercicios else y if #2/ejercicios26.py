def es_positivo_o_negativo(numero):
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "cero"

def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

numero = float(input("Ingrese un número: "))

print("1. Determinar si es positivo o negativo")
print("2. Determinar si es par o impar")
opcion = int(input("Seleccione una opción: "))

if opcion == 1:
    resultado = es_positivo_o_negativo(numero)
    print(f"El número es {resultado}.")
elif opcion == 2:
    resultado = es_par_o_impar(numero)
    print(f"El número es {resultado}.")
else:
    print("Opción no válida.")

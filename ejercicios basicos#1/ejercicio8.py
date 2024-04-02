def calcular_promedio():
    numeros = []
    for i in range(5):
        numero = float(input(f"Ingrese el número {i+1}: "))
        numeros.append(numero)
    
    promedio = sum(numeros) / len(numeros)
    print("El promedio de los números ingresados es:", promedio)

calcular_promedio()
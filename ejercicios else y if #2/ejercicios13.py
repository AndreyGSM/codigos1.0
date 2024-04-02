numero1 = float(input("Ingrese el primer número: "))

numero2 = float(input("Ingrese el segundo número: "))

if numero1 > numero2:
    print(f"El primer número ({numero1}) es mayor que el segundo número ({numero2}).")
elif numero1 < numero2:
    print(f"El segundo número ({numero2}) es mayor que el primer número ({numero1}).")
else:
    print("Los números ingresados son iguales.")

N = int(input("Ingrese el número N: "))

suma = 0

contador = 1

while contador <= N:
    suma += contador
    contador += 1

print("La suma de los primeros {} números naturales es: {}".format(N, suma))

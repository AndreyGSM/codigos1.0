def calcular_distancia():
    velocidad = float(input("Ingrese la velocidad (km/h): "))
    tiempo = float(input("Ingrese el tiempo (horas): "))
    distancia = velocidad * tiempo
    print(f"La distancia recorrida es: {distancia} km")

def calcular_tiempo():
    velocidad = float(input("Ingrese la velocidad (km/h): "))
    distancia = float(input("Ingrese la distancia (km): "))
    tiempo = distancia / velocidad
    print(f"El tiempo necesario es: {tiempo} horas")

def calcular_velocidad():
    distancia = float(input("Ingrese la distancia (km): "))
    tiempo = float(input("Ingrese el tiempo (horas): "))
    velocidad = distancia / tiempo
    print(f"La velocidad es: {velocidad} km/h")

print("Seleccione qué cálculo desea realizar:")
print("1. Calcular distancia recorrida")
print("2. Calcular tiempo")
print("3. Calcular velocidad")
opcion = int(input("Ingrese el número de la opción: "))

if opcion == 1:
    calcular_distancia()
elif opcion == 2:
    calcular_tiempo()
elif opcion == 3:
    calcular_velocidad()
else:
    print("Opción no válida.")

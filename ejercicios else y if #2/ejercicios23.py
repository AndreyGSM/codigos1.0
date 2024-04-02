
edad = int(input("Ingrese la edad del deportista: "))

estatura = float(input("Ingrese la estatura del deportista en cm: "))


peso = float(input("Ingrese el peso del deportista en kg: "))

if edad <= 18 and estatura > 180 and peso <= 80:
    print("El deportista es aceptado en el equipo de baloncesto de Bogotá.")
else:
    print("El deportista no cumple con las condiciones para ser aceptado en el equipo de baloncesto de Bogotá.")

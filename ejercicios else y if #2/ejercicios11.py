from datetime import datetime

anio_nacimiento = int(input("Ingrese su año de nacimiento: "))

anio_actual = datetime.now().year

edad = anio_actual - anio_nacimiento

if edad >= 18:
    print("La persona es mayor de edad.")
else:
    print("La persona no es mayor de edad.")
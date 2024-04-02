
suma_edades = 0

for i in range(15):
   
    edad = int(input("Ingrese la edad del estudiante {}: ".format(i+1)))
    
    suma_edades += edad

promedio_edades = suma_edades / 15

print("La edad promedio del grupo de estudiantes es:", promedio_edades)

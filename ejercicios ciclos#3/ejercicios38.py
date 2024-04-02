
suma_notas = 0

for i in range(15):
    
    nota = float(input("Ingrese la nota del estudiante {}: ".format(i+1)))
    
    suma_notas += nota

promedio_notas = suma_notas / 15

if promedio_notas >= 4.0:
    print("El estudiante gana la materia de Programación de Software.")
else:
    print("El estudiante no gana la materia de Programación de Software.")

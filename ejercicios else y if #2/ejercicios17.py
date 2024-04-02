
codigo_estudiante = input("Ingrese el código del estudiante: ")

nombre_estudiante = input("Ingrese el nombre del estudiante: ")

nombre_materia = input("Ingrese el nombre de la materia: ")

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

nota_definitiva = (nota1 + nota2 + nota3) / 3

if nota_definitiva >= 4.0:
    resultado = "aprobó"
else:
    resultado = "desaprobó"

print(f"Nombre del estudiante: {nombre_estudiante}")
print(f"Código del estudiante: {codigo_estudiante}")
print(f"Nombre de la materia: {nombre_materia}")
print(f"Nota definitiva: {nota_definitiva}")
print(f"El estudiante {resultado} la materia.")
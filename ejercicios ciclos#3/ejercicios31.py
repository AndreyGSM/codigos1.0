
mayores_de_edad = 0


for i in range(20):
  
    edad = int(input("Ingrese la edad del estudiante {}: ".format(i+1)))
    
    if edad >= 18:
        mayores_de_edad += 1


print("El número de estudiantes mayores de edad es:", mayores_de_edad)


suma_estaturas = 0

for i in range(18):
   
    estatura = float(input("Ingrese la estatura del estudiante {}: ".format(i+1)))
    
    suma_estaturas += estatura

promedio_estaturas = suma_estaturas / 18

if promedio_estaturas < 140:
    print("Estudiantes muy bajos")
elif 140 <= promedio_estaturas < 170:
    print("Estudiantes de estatura normal")
else:
    print("Estudiantes muy altos")

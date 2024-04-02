
hombres = 0
mujeres = 0

for i in range(25):
   
    genero = input("Ingrese el género del estudiante {}: ".format(i+1)).lower()
    
    if genero == "hombre":
        hombres += 1
    elif genero == "mujer":
        mujeres += 1
    else:
        print("Género no reconocido. Por favor, ingrese 'hombre' o 'mujer'.")

print("Hay {} hombres y {} mujeres en el curso.".format(hombres, mujeres))

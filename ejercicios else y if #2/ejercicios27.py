def pasa_o_no_materia():
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))
    promedio = (nota1 + nota2 + nota3) / 3
    if promedio > 3.0:
        return "El estudiante pasa la materia."
    else:
        return "El estudiante no pasa la materia."

def es_mayor_o_menor_de_edad():
    ano_nacimiento = int(input("Ingrese el año de nacimiento: "))
    ano_actual = int(input("Ingrese el año actual: "))
    edad = ano_actual - ano_nacimiento
    if edad >= 18:
        return "El estudiante es mayor de edad."
    else:

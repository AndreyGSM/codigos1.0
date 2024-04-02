def es_numero_positivo(valor):
    try:
        valor = float(valor) 
        if valor > 0:
            return True
        else:
            print("El número ingresado no es positivo.")
            return False
    except ValueError:
        print("El valor ingresado no es un número.")
        return False


numero = input("Ingrese un número: ")

if es_numero_positivo(numero):
    print("El número ingresado es positivo.")
else:
    print("El número ingresado no es positivo.")
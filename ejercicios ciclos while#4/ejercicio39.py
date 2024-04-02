
continuar = 's'

while continuar.lower() == 's':
    
    base = float(input("Ingrese la base: "))
    
    exponente = float(input("Ingrese el exponente: "))
   
    resultado = base ** exponente
   
    print("El resultado de la operación de potencia es:", resultado)
    
    continuar = input("¿Desea calcular otra operación de potencia? (s/n): ")

print("Programa finalizado.")

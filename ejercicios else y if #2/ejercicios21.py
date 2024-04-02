
suma_temperaturas = 0
contador_dias = 0

for dia in range(1, 8):
    temperatura = float(input(f"Ingrese la temperatura del día {dia}: "))
    suma_temperaturas += temperatura
    contador_dias += 1

temperatura_promedio = suma_temperaturas / contador_dias

if temperatura_promedio > 35:
    print("Que semana tan calurosa")
elif 15 <= temperatura_promedio < 35:
    print("Que clima tan delicioso")
else:
    print("Que semana tan fría")

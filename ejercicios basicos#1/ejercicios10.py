salario_diario = float(input("Ingrese el salario diario del empleado: "))
dias_trabajados = int(input("Ingrese el número de días trabajados: "))
salario_total_sin_descuentos = salario_diario * dias_trabajados
descuento_pension = salario_total_sin_descuentos * 0.10
descuento_salud = salario_total_sin_descuentos * 0.15
salario_total_con_descuentos = salario_total_sin_descuentos - descuento_pension - descuento_salud
print(f"El salario total a pagar al empleado es: {salario_total_con_descuentos} unidades monetarias")
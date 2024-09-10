from os import system
system("cls")

"""
1- Pedir al usuario que ingrese nombre y apellido del encuestado, guardarlo como string.
2- Pedir al usuario que ingrese el salario mensual del encuestado y guardarla como entero.
3- Pedir al usuario que ingrese la cantidad de horas trabajadas en la semana anterior por el
encuestado y guardarlo como entero. Validar que sea un valor entre 0 y 120
4- Calcular el ingreso horario del encuestado (ingreso dividido por horas trabajadas) y
generar una respuesta por pantalla con todos los datos ingresados para verificar que estén
bien cargados."""

nombre = input("Ingrese su nombre y apellido: ")
salario_mensual = int(input("Ingrese su salario mensual: "))
while salario_mensual < 0:
    salario_mensual = int(input("error!!. Ingrese salario válido: "))

horas_trabajadas = int(input("Ingrese cantidad de horas trabajadas en la semana anterior: "))
while horas_trabajadas < 0 or horas_trabajadas > 120:
    horas_trabajadas = int(input("Error!!. Ingrese horas válidas (entre 0 y 120): "))

ingreso_horario = salario_mensual / horas_trabajadas

msje = "                DATOS INGRESADOS\n"
msje += "================================================\n"
msje += f"Nombre y apellido del encuestado es: {nombre}\n"
msje += f"El salario mensual del encuestado es: {salario_mensual}\n"
msje += f"Horas trabajadas: {horas_trabajadas}\n"
msje += f"El ingreso horario del encuestado es: {ingreso_horario}"

print(msje)
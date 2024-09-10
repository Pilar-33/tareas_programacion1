from os import system
system("cls")

"""
Ejercicio 8:
Genere un segundo módulo en el cual existan las funciones necesarias para 
la gestión del equipo de recursos humanos de la empresa.
#?En el mismo debe existir una primera función que calcule el valor del 
#?salario de cada empleado. 
#El valor del mismo es la cantidad de horas trabajadas multiplicadas 
#por 10 y un incremento del 3% por cada año de antigüedad.
#?También debe haber una segunda función que calcule la productividad 
#?del empleado. 
# La misma se calcula como la cantidad de artefactos producidos, 
# dividido por la cantidad de horas de trabajo.
#?En tercer lugar debe haber una función que reporte toda la 
#?información del empleado
incluyendo la calculada en las dos funciones anteriores, nombre y edad
"""
# Primera funcion
def calcular_salario(horas_trabajadas: int, antiguedad: int) -> float:
    """
    Calcula el salario de un empleado basado en las horas trabajadas y 
    la antigüedad.
    
    Args:
    - horas_trabajadas (int): Número de horas trabajadas por el empleado.
    - antiguedad (int): Años de antigüedad del empleado.

    Returns:
    salario (float): Valor del salario del empleado.
    """
    # Calcula el salario base
    salario_base = horas_trabajadas * 10
    
    # Calcula el incremento del 3% por cada año de antigüedad
    incremento = 1 + (0.03 * antiguedad)
    
    # Calcula el salario final aplicando el incremento
    salario_final = salario_base * incremento

    return salario_final

# Segunda función
def calcular_productividad(horas_trabajadas: int, 
                        cantidad_artefactos: int) -> int:
    """
    Calcula la productividad de un empleado dividiendo la cantidad 
    de artefactos producidos entre las horas trabajadas.

    Args:
    - cantidad_artefactos (int): Número de artefactos producidos 
    por el empleado.
    - horas_trabajadas (int): Número de horas trabajadas por 
    el empleado.
    
    Returns:
    productividad (float): Productividad del empleado.
    """
    if horas_trabajadas > 0:
        productividad = cantidad_artefactos / horas_trabajadas
        productividad = int(productividad)
        return productividad
    else:
        productividad = 0
        return productividad
    

# Tercera función
def reportar_informacion(nombre: str, edad: int, horas_trabajadas: int, 
                antiguedad: int, cantidad_artefactos: int) -> str:

    """
    Reporta toda la información del empleado incluyendo 
    lo calculada en las dos funciones anteriores.
    
    Args:
    - nombre (str): Nombre del empleado.	
    - edad (int): Edad del empleado.
    - horas_trabajadas (int): Número de horas trabajadas por el empleado.
    - antiguedad (int): Años de antigüedad del empleado.
    - cantidad_artefactos (int): Número de artefactos producidos 
    por el empleado.

    Returns:
    msje (str): Mensaje con la información del empleado.
    """
    salario_final = calcular_salario(horas_trabajadas, antiguedad)
    productividad = calcular_productividad(horas_trabajadas, 
                                        cantidad_artefactos)
    msje = "INFORMACIÓN DEL EMPLEADO\n========================\n"
    msje += f"Nombre: {nombre}\n"
    msje += f"Edad: {edad} año(s)\n"
    msje += f"Horas trabajadas: {horas_trabajadas} horas\n"
    msje += f"Antigüedad: {antiguedad} años\n"
    msje += f"Cantidad de artefactos: {cantidad_artefactos}\n"
    msje += f"Salario final: ${salario_final:.2f}\n"
    msje += f"Productividad: {int(productividad)} artefactos por hora"
    return msje


#Solicitar datos
nombre = input("Nombre: ")
edad = int(input("Edad: "))
horas_trabajadas = int(input("Horas trabajadas: "))
antiguedad = int(input("Antiguedad en años: "))
cantidad_artefactos = int(input("Cantidad de artefactos: "))

print(" ")
informe_final = reportar_informacion(nombre, edad, horas_trabajadas, 
                                    antiguedad, cantidad_artefactos)

print(informe_final)
print(reportar_informacion.__doc__)
print(calcular_productividad.__doc__)
print(calcular_salario.__doc__)
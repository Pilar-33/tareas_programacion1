from os import system
system("cls")

# Primera funcion
def calcular_salario(horas_trabajadas: int, antiguedad: int) -> float:
    """Calcula el salario de un empleado basado en las horas trabajadas y
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
def calcular_productividad(horas_trabajadas: int, cantidad_artefactos: int) -> int:
    """Calcula la productividad de un empleado dividiendo la cantidad
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
def reportar_informacion(
    nombre: str,
    edad: int,
    horas_trabajadas: int,
    antiguedad: int,
    cantidad_artefactos: int,
) -> str:
    
    """Reporta toda la información del empleado incluyendo
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
    productividad = calcular_productividad(horas_trabajadas, cantidad_artefactos)

    msje = f"""
    INFORMACIÓN DEL EMPLEADO
    ========================
    Nombre: {nombre}
    Edad: {edad} año(s)
    Horas trabajadas: {horas_trabajadas} horas
    Antigüedad: {antiguedad} años
    Cantidad de artefactos: {cantidad_artefactos}
    Salario final: ${salario_final:.2f}
    Productividad: {int(productividad)} artefactos por hora"""
    return msje


# Solicitar datos
nombre = input("Nombre: ")
edad = int(input("Edad: "))
horas_trabajadas = int(input("Horas trabajadas: "))
antiguedad = int(input("Antiguedad en años: "))
cantidad_artefactos = int(input("Cantidad de artefactos: "))

print(" ")
informe_final = reportar_informacion(
    nombre, edad, horas_trabajadas, antiguedad, cantidad_artefactos
)

print(informe_final)

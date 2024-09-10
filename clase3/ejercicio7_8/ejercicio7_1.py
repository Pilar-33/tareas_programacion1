from os import system

system("cls")

# CONSTANTES
IVA = 21
RETENCIONES = 15


# FUNCIONES
def calcular_ventas_nacionales(valor_ventas_nacionales: float, IVA: float) -> float:
    """La función realiza el cálculo de ventas nacionales sin IVA.

    Args:
    - valor_ventas_nacionales (float): Valor total de las ventas nacionales.
    - IVA (float): Porcentaje del IVA aplicando a las ventas.
    Por defecto es 21%.

    Returns:
    float: Valor de las ventas sin IVA.
    """
    resultado_nacional = valor_ventas_nacionales * (1 / (1 + (IVA / 100)))
    return resultado_nacional


def calcular_valor_exportaciones(
    valor_exportaciones: float, RETENCIONES: float
) -> float:
    """La función realiza el cálculo del valor de exportaciones
    con retenciones.

    Args:
    - valor_exportaciones (float): Valor total de las exportaciones.
    - retenciones (float): Porcentaje de retenciones aplicando
    a las exportaciones. Por defecto es 15%.

    Returns:
    float: Valor de las exportaciones con retenciones.
    """
    resultado_exportaciones = valor_exportaciones * (1 - (RETENCIONES / 100))
    return resultado_exportaciones


def calcular_total_con_impuestos(
    valor_ventas_nacionales: float,
    valor_exportaciones: float,
    IVA: float,
    RETENCIONES: float,
) -> float:
    """La función calcula el total de ventas y exportaciones
    después de aplicar impuestos.

    Args:
    - valor_ventas_nacionales (float): Valor total de las ventas nacionales.
    - valor_exportaciones (float): Valor total de las exportaciones.
    - iva (float): Porcentaje del IVA aplicado a las ventas nacionales.
    Por defecto es 21%.
    - retenciones (float): Porcentaje de retenciones aplicadas a las
    exportaciones. Por defecto es 15%.

    Returns:
    float: El total de las ventas nacionales sin IVA y las
        exportaciones después de las retenciones.
    """
    ventas_nacionales_sin_iva = calcular_ventas_nacionales(valor_ventas_nacionales, IVA)
    exportaciones_con_retenciones = calcular_valor_exportaciones(
        valor_exportaciones, RETENCIONES
    )
    resultado_final = ventas_nacionales_sin_iva + exportaciones_con_retenciones
    return resultado_final


# Datos ingresados
valor_ventas_nacionales = float(input("Valor ventas nacionales: "))
valor_exportaciones = float(input("Valor exportaciones: "))


# Probando las funciones
ventas_sin_iva = calcular_ventas_nacionales(valor_ventas_nacionales, IVA)

valor_con_retenciones = calcular_valor_exportaciones(valor_exportaciones, RETENCIONES)

total_con_impuestos = calcular_total_con_impuestos(
    valor_ventas_nacionales, valor_exportaciones, IVA, RETENCIONES
)

print(" ")
msje = (
    f"Ventas sin IVA: ${ventas_sin_iva:.2f}\n"
    f"Valor de las exportaciones con retenciones: "
    f"${valor_con_retenciones:.2f}\n"
    f"Total con impuestos: "
    f"${total_con_impuestos:.2f}"
)

print(msje)

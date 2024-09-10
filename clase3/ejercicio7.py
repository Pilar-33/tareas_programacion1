from os import system
system('cls')

"""
Supongamos que le solicito a chatgpt una función para calcular valores de ventas de
productos con impuestos para una determinada empresa:
La respuesta de chatgpt es:

! def calculo_impuestos(valor_exportaciones, valor_ventas_nacionales, iva = 21, 
!   retenciones = 15):
!    resultado_nacional = valor_ventas_nacionales* (1 / (1 + (iva / 100)))
!    resultado_exportaciones = valor_exportaciones* (1- (retenciones / 100))
!    resultado_final = resultado_nacional + resultado_exportaciones
!    return resultado_final
¿Considera que cumple con los objetivos de una función?
Corrija la función dentro de un módulo, divida en distintas funciones de ser necesario,
documente y denomine correctamente"""

#? Observaciones:
"""
La función no cumple con los objetivos:
1. Minificación: La función realiza múltiples tareas en lugar 
    de enfocarse en una tarea específica.
2. Depuración: La estructura no es clara, 
    lo que dificulta la identificación de errores.
4. Reutilización: Al contener todo el cálculo en un solo bloque, 
    la función no es reutilizable.
5. Independencia: La función está acoplada; si ocurre un error 
    en el cálculo de resultado_nacional, afectará al cálculo final, 
    lo que provocaría que toda la función falle.
"""


"""
2- Crear una función que permita determinar si un número es par o no. La función retorna
“True” en caso afirmativo y “False” en caso contrario. Probar en el programa principal
realizando la invocación o llamada
"""


def es_par(numero: int) -> bool:
    if numero % 2 == 0:
        return True
    else:
        return False

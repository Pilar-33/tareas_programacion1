from os import system
system("cls")

def sumar(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        suma += numero
    return suma
"""def calcular_promedio(lista_numeros):
    suma = sum(lista_numeros)
    cantidad = len(lista_numeros)
    return suma/cantidad"""
def calcular_promedio(lista_numeros):
    cantidad = len(lista_numeros)
    resultado = sumar(lista_numeros)/cantidad
    return resultado

print(calcular_promedio([4,5,6]))
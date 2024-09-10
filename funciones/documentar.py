def sumar_dos_numeros(num1, num2):
    """
    Esta función recibe por parametro
    dos números enteros y devuelve 
    la suma de ambos.
    """
    return num1 + num2


print(sumar_dos_numeros(5, 7)) # 12

help(sumar_dos_numeros)
print(sumar_dos_numeros.__doc__)

def mi_funcion_resta(a, b):  #Args: argumentos o parámetros
    """
    Realizamos una resta de dos números

    Args:
        a(int/float): Primer operando a utilizar
        b(int/float): Segundo operando a utilizar
    
    Returns:
        int/float: Valor numerico que contiene la resta
    """
    return a - b

print(mi_funcion_resta(5, 3)) # 2
print(mi_funcion_resta.__doc__)

print(" ")
# Todo lo que eata por debajo de la funcion se va dejar de ejecutar
def restar(a, b):
    resultado = a - b
    return resultado
    #print("Gracias por venir")

print(restar(5, 3)) # 2


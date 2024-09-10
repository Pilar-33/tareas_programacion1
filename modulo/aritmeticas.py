from os import system
system('cls')

def sumar(num1: int, num2: int) -> int:
    resultado = num1 + num2
    return resultado

def restar(num1: int, num2: int) -> int:
    resultado = num1 - num2
    return resultado

def multiplicar(num1: int, num2: int) -> int:
    resultado = num1 * num2
    return resultado

def dividir(num1: int, num2: int) -> float:
    if num2!=0:
        resultado = num1 / num2
        return f"{resultado:.2f}"
    else:
        return "Error: No se puede dividir por cero"
    
"""# Testeo de la función sumar
resultado = sumar(5,7)
print(resultado)

# Testeo de la función restar
resultado = restar(5,7)
print(resultado)

# Testeo de la función multiplicar
resultado = multiplicar(5,7)
print(resultado)

# Testeo de la función dividir
resultado = dividir(5,7)
print(resultado)

"""


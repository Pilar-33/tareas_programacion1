from os import system
system('cls')
def dividir(numero_a: int, numero_b: int = 2) -> int:
    resultado = numero_a/numero_b
    return resultado
resultado_dividir = dividir(13)
print(resultado_dividir)
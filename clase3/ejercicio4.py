from os import system
system("cls")

"""# 4- Realizar un programa en donde se puedan utilizar 
los prototipos de la función Restar en
sus 4 combinaciones.
restar1(int, int)->int:
restar2()->int:
restar3(int, int):
restar4():"""
# 1er prototipo
def restar1(a: int, b: int) -> int:
    resta = a - b
    return resta

# 2do prototipo
def restar2(a, b) -> int:
    resta = a - b
    return resta

# 3er prototipo
def restar3(a: int, b: int):
    print(f"{a} - {b} = {a - b}")

# 4to prototipo
def restar4(a, b):
    print(f"{a} - {b} = {a - b}")

# Pruebas del programa, llamando las funciones
numero1 = int(input("Primer número: "))
numero2 = int(input("Segundo número: "))

# Llamando la función 1er prototipo
resultado1 = restar1(numero1, numero2)
print(resultado1)

# Llamando la función 2do prototipo
resultado2 = restar2(numero1, numero2)
print(resultado2)

# Llamando la función 3er prototipo
restar3(numero2, numero1)
restar4(numero2, numero1)
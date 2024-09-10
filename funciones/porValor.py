from os import system
system("cls")

# paso por Valor, pero python trabaja por referencia
def mi_funcion(numero):
    numero = 98
    print(numero)
    print(id(numero))

numero = 10
print(numero)
print(id(numero))

mi_funcion(numero)
print(numero)
print(id(numero))
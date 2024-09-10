from os import system
system('cls')

def mi_funcion(lista: list):
    lista.append(23)
    print(lista)

lista = [1,2,3,4]
print(lista)
print(id(lista))

mi_funcion(lista)
print(lista)

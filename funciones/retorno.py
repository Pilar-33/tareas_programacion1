from os import system
system('cls')

def saludar(nombre):
    saludo = f"Hola {nombre}"
    return saludo

saludo = saludar("María")
print(saludo)
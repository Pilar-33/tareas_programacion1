from os import system
system("cls")

def saludar(nombre):
    saludo = f"Hola {nombre}"
    return saludo

saludo = saludar("María")
print(saludo)

#funcion len
variable = "Pilar"
print(len(variable))
print(len("Silvia"))

#sin función len


#Contar caracteres
def contar_caracteres(nombre):
    contador = 0
    for _ in nombre: #como no se usa la variable i se coloca por convención _
        contador += 1
    
    return contador

nombre = input("Ingrese su nombre: ")
respuesta = contar_caracteres(nombre)

print(f"{nombre} tiene: {respuesta} letras")

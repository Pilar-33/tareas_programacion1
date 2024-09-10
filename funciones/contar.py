from os import system
system("cls")

def contar_caracteres(texto):
    contador = 0
    for i in texto:
        contador += 1
    return contador

texto = "Hola"
respuesta = contar_caracteres(texto)

print(f"El texto '{texto}' tiene {respuesta} caracteres.")

numero = "1234567"
for i in numero:
    salida = (int(i))

print(type(salida))
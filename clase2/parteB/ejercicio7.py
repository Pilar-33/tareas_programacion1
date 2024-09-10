from os import system
system("cls")

"""#7- Dada la siguiente lista:
lista_numeros = [14, 99, 8, 15, 17, 33, 19, 24, 12, 10]
a) Contar cuántos son múltiplos de 5
b) mostrar sólo los números pares."""
#a) Contar cuántos son múltiplos de 5
lista_numeros = [14, 99, 8, 15, 17, 33, 19, 24, 12, 10]
lista_ordenada = sorted(lista_numeros)
contar_5 = 0

for numero in lista_ordenada:
    if numero % 5 == 0:
        contar_5 += 1

#b) mostrar sólo los números pares
numeros_pares = []
for numero in lista_ordenada:
    if numero % 2 == 0:
        numeros_pares.append(numero)
msje = f"a) Cantidad de números múltiplos de 5: {contar_5}\n"
msje+= f"b) Lista números pares: {numeros_pares}"
print(msje)
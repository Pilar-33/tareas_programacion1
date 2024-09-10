#for de  0 a 4 range
for numero in range (5):
    print(f"El número es: {numero}")
    if numero == 17:
        break

#mostrar solo numeros pares
for numero in range (20):

    if (numero % 2) == 1:
        continue
    else:
        print(f"El número es: {numero}")


for letra in "perro":
    
    if letra == "r":
        continue
    else:
        print(letra)


for numero in range (20):
    if (numero % 3) == 0:
        continue
    else:
        print(f"El número es: {numero}")

for numero in range (1,20):
    if (numero % 3) != 0:
        continue
    else:
        print(f"El número es: {numero}")


for numero in range (1,20):
    if not (numero % 3) == 0:
        continue
    else:
        print(f"El número es: {numero}")

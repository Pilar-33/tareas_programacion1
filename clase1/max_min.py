lista_numeros = list(range(1, 44, 3))

print(lista_numeros)

lista = [1,33,77,33,2,3,88] 

maximo =float("-inf")
minimo =float("inf")
bandera = True
for numero in lista_numeros:
    if bandera == True:
        bandera == False
        maximo == numero
        minimo == numero
    else:
        if numero >  maximo:
            maximo = numero
        elif numero < minimo:
            minimo = numero

print(maximo)
print(minimo)


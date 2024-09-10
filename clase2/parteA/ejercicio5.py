from os import system
system("cls")

"""
5- Dada la siguiente lista de ingresos horarios:
[ 10, 15, 33, 8, 45, 16, 90, 19, 43, 54,
9, 32, 15, 6, 50, 19, 26, 65, 10, 18 ]
a) Calcular el promedio de ingresos/hora del 20% que más gana.
b) Calcular el promedio de ingresos/hora de todos los respondentes.
c) Buscar cuál es el valor que más se repite.
d) Calcular la media geométrica"""

lista_ingresos = [10, 15, 33, 8, 45, 16, 90, 19, 43, 54,
9, 32, 15, 6, 50, 19, 26, 65, 10, 18]

lista_ordenada = sorted(lista_ingresos, reverse= True)
print(lista_ordenada)
# a)Calcular el promedio de ingresos/hora del 20% que más gana
porcentaje = 0.2
elementos = len(lista_ingresos) 
cantidad_top = int(elementos * porcentaje)
cantidad_top = max(cantidad_top, 1)
top_20_percent = lista_ordenada[:cantidad_top]
promedio_top = sum(top_20_percent)/len(top_20_percent)
"""print(f"Elementos: {elementos}")
print(f"cantidad top: {cantidad_top}")
print(f"Porcentaje top: {top_20_percent}")
print(f"promedio top 20%: {promedio_top}")"""

# b) Promedio de ingresos/hora de todos los respondientes
suma_ingresos = 0

for ingreso in lista_ingresos:
    suma_ingresos += ingreso
promedio_ingresos = suma_ingresos / len(lista_ingresos)

"""#c.1) Buscar cuál es el valor que más se repite.
if len(lista_ingresos) == len(set(lista_ingresos)):
    repite = "No hay elementos repetidos"
else:
    repite = max(set(lista_ingresos), key = lista_ingresos.count)

#c.2) Buscar cuál es el valor que más se repite.
valor_mas_repetidos = None
max_apariciones = 0

for numero in lista_ingresos:
    apariciones = 0
    for valor in lista_ingresos:
        if numero == valor:
            apariciones += 1
    
    if apariciones > max_apariciones:
        max_apariciones = apariciones
        valor_mas_repetidos = numero"""

#c) Buscar cuál es el valor que más se repite.
numeros_repetidos = set()
maximo_apariciones = 0
for i in range(len(lista_ingresos)):
    numero_actual = lista_ingresos[i]
    veces = 0
    for j in range(len(lista_ingresos)):
        if lista_ingresos[j] == numero_actual:
            veces += 1
    if veces > maximo_apariciones:
        maximo_apariciones = veces
        numeros_repetidos = [numero_actual]
    elif veces == maximo_apariciones:
        numeros_repetidos.append(numero_actual)

#d)Calcular la media geométrica: 2,4, 8 -> producto = 2*4*8, media_geometrica = producto ** (1/len(lista_ingresos))
producto = 1
n = len(lista_ingresos)

for numero in lista_ingresos:
    producto += numero
media_geometrica = producto ** (1/n)
print(producto)
msje = f"Lista ordenada en forma descendente: {lista_ordenada}"
msje = f"a)\nEl 20% de ingresos es: {cantidad_top}\nLos máximos son: {top_20_percent}\nEl promedio de ingresos/hora del 20% es: {promedio_top}\n"
msje += f"b) El promedio de todos los respondientes: {promedio_ingresos}\n"
"""msje += f"c.1) El valor que más se repite: {repite}\n"
msje += f"c.2)\nEl valor que más repite: {valor_mas_repetidos}\nNro de veces: {max_apariciones}\n"""
msje += f"c)\nNúmeros que se repiten: {numeros_repetidos}\nNro de veces: {maximo_apariciones}\n"
msje += f"d)La media geométrica es: {media_geometrica:.2f}"

print(msje)
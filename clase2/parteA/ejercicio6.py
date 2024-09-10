from os import system
system("cls")

"""
6- Suponiendo que tenemos dos listas en las cuales la posición es la misma en ambas para
cada respondente:
lista_edad = [26, 45, 33, 67, 53, 59, 19, 37, 41, 32]
lista_nombres = [“Juan”, “Matias”, “Carla”, “Susana”, “Olivia”, “Carlos”, “Daniel”, “Jimena”,
“Mariela”, “Ignacio”]
a) Devolver el nombre del respondiente más jóven y del más grande.
b) Genere dos nuevos listado por sexo y calcule la media etaria para varones y mujeres
c) Utilizando continue, calcule la media etaria para mayores de 40 años"""

lista_edad = [26, 45, 33, 67, 53, 59, 19, 37, 41, 32]
lista_nombres = ["Juan", "Matias", "Carla", "Susana", "Olivia", "Carlos", "Daniel", "Jimena", "Mariela", "Ignacio"]

# a) Devolver el nombre del respondiente más jóven y del más grande
nombre_joven = lista_nombres[0]
edad_joven = lista_edad[0]
nombre_grande = lista_nombres[0]
edad_grande = lista_edad[0]

for posicion in range(len(lista_edad)):
    if lista_edad[posicion] < edad_joven:
        edad_joven = lista_edad[posicion]
        nombre_joven = lista_nombres[posicion]
    elif lista_edad[posicion] > edad_grande:
        edad_grande = lista_edad[posicion]
        nombre_grande = lista_nombres[posicion]

#b) Genere dos nuevos listado por sexo y calcule la media etaria para varones y mujeres
lista_varones = [16,23,19,22,40,15]
lista_mujeres = [30,14,39,40,50,52]
suma_mujeres = 0
suma_varones = 0

for mujeres in lista_mujeres:
    suma_mujeres += mujeres

for hombres in lista_varones:
    suma_varones += hombres

media_mujeres = suma_mujeres/len(lista_mujeres)
media_varones = suma_varones/len(lista_varones)

#c) Utilizando continue, calcule la media etaria para mayores de 40 años// revisar
suma_edad = 0
contador_mayores = 0
for edad in lista_edad:
    if edad < 41:
        continue
    suma_edad += edad
    contador_mayores += 1

if contador_mayores > 0:
    media_edad = suma_edad/contador_mayores
else:
    media_edad = 0

msje = f"Nombre del más joven es: {nombre_joven}\n"
msje += f"Nombre del más grande: {nombre_grande}\n"
msje += f"Media etaria de mujeres: {media_mujeres}\n"
msje += f"Media etaria de varones: {media_varones}\n"
msje += f"Media etaria mayores de 40 años: {media_edad}"

print(msje)

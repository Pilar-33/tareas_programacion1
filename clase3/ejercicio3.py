from os import system
system("cls")

"""3- Especializar la función del punto 1 
para que valide el número en un rango determinado
pasado por parámetro “desde”-“hasta”."""

def mostrar_numero(numero: int, desde: int, hasta: int) -> None:
    if numero >= desde and numero <= hasta:
        print(f"Número ingresado dentro de rango ({desde} y {hasta}): {numero}")
    else:
        print(f"Número fuera de rango ({desde} y {hasta})")

# Pidiendo número, llamar a la funcion, asignadole valor al parametro
num = int(input("Ingrese un número: "))
mostrar_numero(num, 1, 20)

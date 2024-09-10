from os import system
system("cls")

#1- Crear una función que muestre por pantalla el número que recibe como parámetro.
# crando función
def mostrar_numero(numero: int) -> None:
    print(f"El número que recibe por parámetro es: {numero}")

# Pidiendo número, llamar a la funcion, asignadole valor al parametro
num = int(input("Ingrese un número: "))
mostrar_numero(num)

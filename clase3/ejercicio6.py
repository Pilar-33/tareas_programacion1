from os import system

system("cls")

"""
6- Realizar un programa que: asigne a las variables numero1 y numero2 
los valores solicitados al usuario, valide los mismos entre 10 y 100, 
asigne a la variable operacion el valor solicitado al usuario: 
's'-sumar, 'r'-restar (validar),realice la operación de dichos valores
a través de una función. Mostrar el resultado por pantalla"""


def sumar(num1: int, num2: int) -> str:
    suma = f"{num1} + {num2} = {num1 + num2}"
    if isinstance(suma, str):
        return suma
    else:
        return str(suma)  # Convierte a string si no lo es


def restar(num1, num2) -> str:
    resta = f"{num1} - {num2} = {num1 - num2}"
    return resta


numero1 = int(input("Ingrese el primer número (entre 10 y 100): "))
while numero1 < 10 or numero1 > 100:
    numero1 = int(input("Error!. Ingrese un número entre 10 y 100: "))

numero2 = int(input("Ingrese el segundo número (entre 10 y 100): "))
while numero2 < 10 or numero2 > 100:
    numero2 = int(input("Error!. Ingrese un número entre 10 y 100: "))

operacion = input("Operación:\n's'-sumar\n'r'-restar\nElija una operación: ")
while operacion != "s" and operacion != "r":
    print("Error! Elija una operación válida:")
    operacion = input("Operación:\n's'-sumar\n'r'-restar\nElija una operación: ")

match operacion:
    case "s":
        resultado = sumar(numero1, numero2)
    case "r":
        resultado = restar(numero1, numero2)

print(resultado)

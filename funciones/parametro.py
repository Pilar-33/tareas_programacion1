from os import system
system('cls')

#parametro por nombre
def restar(num1, num2):
    resultado = num1 - num2
    print(resultado) 

number1 = int(input("Ingrese primer número: "))
number2 = int(input("Ingrese segundo número: "))

restar(num2=number2, num1=number1)

#parametro por posicion
def restar1(num1, num2):
    resultado = num1 - num2
    print(resultado)

restar1(number1, number2)

#parametro por defecto
def sumar(num1, num2, num3 = 5):
    resultado = num1 + num2 + num3
    print(resultado)

sumar(number1, number2)

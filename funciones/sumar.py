from os import system
system('cls')

def sumar(num_1, num_2):
    suma = num_1 + num_2
    print(f"{num_1} + {num_2} = {suma}")

#sumar(8,10)
num_1 = int(input("Ingrese primer número: "))
num_2 = int(input("Ingrese segundo número: "))
sumar(num_1, num_2)
from os import system
system("cls")

"""
5- Realizar un programa que: asigne a la variable numero1 
un valor solicitado al usuario,valide el mismo entre 10 y 100, 
realice un descuento del 5% a dicho valor a través de una
función llamada realizarDescuento(). Mostrar el resultado 
por pantalla. Atención: pueden reutilizarse funciones ya creadas.
"""
DESCUENTO = 0.05

#Definiendo función de descuento
def realizarDescuento(numero):
    descuento = numero * DESCUENTO
    return descuento
#Pidiendo al usuario que ingrese un número y validando
numero1 = int(input("Digite un número entre 10 y 100: "))
while numero1 < 10 or numero1 > 100:
    numero1 = int(input("Error!. Digite un número entre 10 y 100: "))

#Llamando la función de descuento
descuento_realizado = realizarDescuento(numero1)

#Calculando el precio final
precio_final = numero1 - descuento_realizado

#Mostrando el resultado del descuento
print(f"Descuento del 5% de ${numero1}: ${descuento_realizado:.2f}\nPrecio Final: ${precio_final}")




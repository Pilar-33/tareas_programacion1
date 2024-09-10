from os import system
system("cls")

""""8- Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000
por cada estadía como base, se pide el ingreso de una estación del
año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del
Plata/Córdoba) para vacacionar para poder calcular el precio final:
-en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un
descuento del 10% Mar del Plata tiene un descuento del 20%-en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene
un aumento del 10% Mar del Plata tiene un aumento del 20%-en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene un
aumento del 10% Mar del Plata tiene un aumento del 10% y Córdoba tiene el
precio sin descuento.
Validar el ingreso de dato"""

estadia_base = 15000

estacion = input("Estación del año (invierno/verano/otoño/primavera): ")
while estacion != "invierno" and estacion != "verano" and estacion != "otoño" and estacion != "primavera":
    estacion = input("Error!. Estación del año (invierno/verano/otoño/primavera): ")

localidad = input("Localidad (bariloche/cataratas/mar del plata/cordoba): ")
while localidad != "bariloche" and localidad != "cataratas" and localidad != "mar del plata" and localidad != "cordoba":
    localidad = input("Error!. Localidad (bariloche/cataratas/mar del plata/cordoba): ")

match estacion:
    case "invierno":
        if localidad == "bariloche":
            estadia_final = estadia_base + (estadia_base * 0.20)
        elif localidad == "cordoba" or localidad == "cataratas":
            estadia_final = estadia_base - (estadia_base * 0.10)
        elif localidad == "mar del plata":
            estadia_final = estadia_base - (estadia_base * 0.20)
        
    case "verano":
        if localidad == "bariloche":
            estadia_final = estadia_base - (estadia_base * 0.20)
        elif localidad == "cordoba" or localidad == "cataratas":
            estadia_final = estadia_base + (estadia_base * 0.10)
        elif localidad == "mar del plata":
            estadia_final = estadia_base + (estadia_base * 0.20)
    case "otoño" | "primavera":
        if localidad == "bariloche" or localidad == "cataratas" or localidad == "mar del plata":
            estadia_final = estadia_base + (estadia_base * 0.10)
        elif localidad == "cordoba":
            estadia_final = estadia_base
        

print(f"La tarifa del viaje es: ${int(estadia_final)}")


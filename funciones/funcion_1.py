
lista_1 = [26,4533,67,53,59,19,37,41,32]
lista_2 = [33,55,777,1234]
lista_3 =[3331,53333,777,1234]

def calcular_media_geo(lista):
    producto = 1
    for numero in lista:
        producto *= numero

    resultado = producto ** (1/len(lista))
    return resultado

media_geo_1 = calcular_media_geo(lista_1)
media_geo_2 = calcular_media_geo(lista_2)
media_geo_3 = calcular_media_geo(lista_3)

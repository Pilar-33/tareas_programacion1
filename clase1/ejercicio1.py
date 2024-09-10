from os import system
system("cls")

var_1 = 33
var_2 = "Pedro"
var_3 = True
var_4 = 3.33
var_5 = 44

#Paradigma estructutado
if (var_1 != 0 and var_5 != 0):
    result = var_1 / var_5
else:
    print("Los números a dividir deben ser distintos de cero")
print(f"Resultado: {result}")

print("===========================")
#Paradigma funcional
def dividir(num_1, num_2):
    if (num_1 != 0 and num_2 != 0):
        return num_1 / num_2
    else:
        print("Los números a dividir deben ser distintos de cero")

print(f"Resultado: {dividir(6,2)}")


#paradigma orientado a objetos
class calculadora:
    def _init_(self) -> None:
        self.resultado = 0
    
    def dividir(self, num_1, num_2):
        if (num_1 != 0 and num_2 != 0):
            self.resultado = num_1/num_2
            return self.resultado
    
obj_calculadora = calculadora() #se crea el resultado
print(f"El resultado es: {obj_calculadora.resultado}") #muestro el resultado por defecto
#obj_calculadora.dividir()
print(f"El resultado de la división con el objeto calculadora es: {obj_calculadora.dividir(6,2)}")
#Implementar la clase Operaciones. Se deben cargar dos valores enteros por teclado en el método
#__init__, calcular su suma, resta, multiplicación y división, cada una en un método, imprimir dichos resultados.

class Operaciones:
    def __init__(self):
        self.valor1=int(input("ingrese primer valor: "))
        self.valor2=int(input("ingrese segundo valor:"))

    def calcular_suma(self):
        suma=self.valor1 + self.valor2
        print ("La suma de los dos valores es: ", suma)

    def calcular_resta(self):
        resta=self.valor1 - self.valor2
        print ("la resta de los dos valores es: ", resta)

    def calcular_multiplicacion(self):
        multiplicacion= self.valor1 * self.valor2
        print ("la multiplicacion de los dos valores es: ", multiplicacion)

    def calcular_division(self):
        division = self.valor1 / self.valor2
        print ("la division de los dos valores es: ", division)

#bloque principal

operacion1=Operaciones()
operacion1.calcular_suma()
operacion1.calcular_resta()
operacion1.calcular_multiplicacion()
operacion1.calcular_division()

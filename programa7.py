#Desarrollar una clase que represente un Cuadrado y tenga los siguientes métodos: inicializar el valor del lado llegando como parámetro al método
#__init__ (definir un atributo llamado lado), imprimir su perímetro y su superficie.

class Cuadrado:
    def __init__(self, lado):
        self.lado=lado

    def calcular_perimetro(self):
        perimetro=self.lado*4
        print ("el perimetro del cuadrado es: ", self.lado)

    def calcular_superficie(self):
        superficie=self.lado*self.lado
        print ("la superficie del cuadrado es: ", self.lado)

#bloque principal
cuadrado1=Cuadrado(12)
cuadrado1.calcular_perimetro()
cuadrado1.calcular_superficie()
#Desarrollar un programa que cargue los lados de un triángulo e implemente los siguientes métodos: inicializar los atributos, imprimir el valor 
#del lado mayor y otro método que muestre si es equilátero o no. El nombre de la clase llamarla Triangulo.

class Triangulo:
    def inicializar(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def imprimir(self):
        print("Lado1:", self.lado1)
        print("Lado2:", self.lado2)
        print("Lado3:", self.lado3)

    def lado_mayor(self):
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print("El lado mayor es:", self.lado1)
        elif self.lado2 > self.lado3:
            print("El lado mayor es:", self.lado2)
        else:
            print("El lado mayor es:", self.lado3)

    def es_equilatero(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("El triángulo es equilátero")
        else:
            print("No es equilátero")

# Bloque principal
triangulo1 = Triangulo()
triangulo1.inicializar(3, 4, 5)
triangulo1.imprimir()
triangulo1.lado_mayor()
triangulo1.es_equilatero()


    

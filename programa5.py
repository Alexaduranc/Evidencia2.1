#Confeccionar una clase que represente un empleado. Definir como atributos su nombre y su sueldo. En el método __init__ cargar los atributos por
#teclado y luego en otro método imprimir sus datos y por último uno que imprima un mensaje si debe pagar impuestos (si el sueldo supera a 3000)

class Empleado:
    def __init__(self):
        self.nombre = input("Ingrese el nombre del empleado: ")
        self.sueldo = float(input("Ingrese el sueldo del empleado: "))

    def imprimir(self):
        print("Nombre de empleado:", self.nombre)
        print("Sueldo de empleado:", self.sueldo)

    def pagar_impuestos(self):
        if self.sueldo > 3000:
            print("Debe pagar impuestos")
        else:
            print("No paga impuestos")


# Bloque principal
empleado1=Empleado()
empleado1.imprimir()
empleado1.pagar_impuestos()


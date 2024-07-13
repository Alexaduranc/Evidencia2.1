#Confeccionar una clase que permita carga el nombre y la edad de una persona. Mostrar los datos cargados.  Imprimir un mensaje si es mayor de edad 
# (edad>=18)
class Persona:
    def inicializar(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)

    def mostrar_datos(self):
        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("No es mayor de edad")

# Bloque principal

persona1 = Persona()
persona1.inicializar("Diego", 20)
persona1.imprimir()
persona1.mostrar_datos()

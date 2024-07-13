#Implementar una clase llamada Alumno que tenga como atributos su nombre y su nota. Definir los métodos para inicializar sus atributos
#imprimirlos y mostrar un mensaje si está regular (nota mayor o igual a 4). Definir dos objetos de la clase Alumno.

class Alumnos:
    def inicializar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre", self.nombre)
        print ("Nota:", self.nota)

    def mostrar_estado(self):
        if self.nota >=4:
            print ("Regular")
        else: 
            print ("Libre")

# Bloque principal

alumno1=Alumnos()
alumno1.inicializar("diego", 2)
alumno1.imprimir()
alumno1.mostrar_estado()

alumno1=Alumnos()
alumno1.inicializar("alexa", 10)
alumno1.imprimir()
alumno1.mostrar_estado()

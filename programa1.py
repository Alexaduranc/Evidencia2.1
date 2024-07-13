#implementaremos una clase llamada persona que tendra como atributo (variable) su nombre y dos metodos (funciones), uno de dichos metodos
#inicializara el atributo nombre y el siguiente metodo mostrara en la pantalla el contenido del mismo. Definir el atributo nombre y de
#la clase persona.

class Persona:
    def inicializar(self, nombre):
        self.nombre = nombre

    def imprimir(self):
        print("Nombre:", self.nombre)

# Bloque principal
persona1 = Persona()
persona1.inicializar("Diego")
persona1.imprimir()

persona2 = Persona()
persona2.inicializar("Alexa")
persona2.imprimir()
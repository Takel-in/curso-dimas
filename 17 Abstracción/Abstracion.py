#Abstracción
"""
    Clases abstractas.
        - Lo las vamos a instanciar nuna directamente.
        - contienen al menos un método abstracto.
        - Las vamos a usar de Base para subclases más espécificas.

    Métodos Abstractos.
        - Debemos sobreescribirlo en cada una de las subclases.

"""

from abc import ABC, abstractmethod # Importamos la clase abc del fichero abc y el métodos Abstractmethos.  
                                    #con Import ejecutamos clases que están en otros archivos.


class Personaje(ABC): #Al heredar de ABC hacemos que la clase sea una clase abastracta.

    @abstractmethod #Esto es un decorador que envuelve y modifica la función que está decorando. 
                    #Es decir que convierte el init en un métido abastaracto por lo que obliga a redefinirlo.
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 0
        self.inventario = []
        self.vida = 100

    @abstractmethod
    def atacar(self, objetivo):
        pass # Como lo hemos declarado abstracto no tiene sentido que haga algo porque siempre se obluga a redifinir en los hijos.

    @abstractmethod
    def getStatus(self): #me sirve definirlo porque todos tienen estos elementos de manera que puedo aprobechar el código e incluso ampliarlo en la subclase.
        print(F"Nombre: {self.nombre}. Nivel {self.nivel} ")

    def subirDeNivel(self):
        self.nivel +=1

    def verInventario(self):
        print(f"Inventario de {self.nombre}")
        for objeto in self.inventario:
            print (objeto)

class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.vida = 120
        self.inteligencia = 95
        self.inventario = ["Poción de Maná", "Grimorio"]

    def getStatus(self):
        print (f"{self.nombre} es de la clase mago")
        super().getStatus()

    def atacar(self, objetivo):
        objetivo.vida  -= self.inteligencia*0.6
        print(f"vida actual del objetivo es:{objetivo.vida}")

    def saludar(self):
        print("Hola que tal soy un mago")




class Guerrero(Personaje):

    def __init__(self, nombre):
        super().__init__(nombre)
        self.vida = 200
        self.fuerza = 75
        self.inventario = ["Poción de vida", "Escudo", "Espada"]

    def getStatus(self):
        print (f"{self.nombre} es de la clase guerrero")
        super().getStatus()

    def atacar(self, objetivo):
        objetivo.vida -= self.fuerza * 0.8
        print(f"vida actual del objetivo es:{objetivo.vida}")

#pj = Personaje("kike") #Daría un error porque el método init es abastracto y por lo tanto ya no puedes generar personajes.

guerrero = Guerrero("kaladin") 
mago = Mago("Yuno") 

guerrero.getStatus() #kaladin es de la clase guerrero
                     #Nombre: kaladin. Nivel 0 
mago.getStatus()     #Yuno es de la clase mago 
                     #Nombre: Yuno. Nivel 0 

guerrero.verInventario() #Inventario de kaladin
                         #Poción de vida
                         #Escudo
                         #Espada
mago.verInventario() #Inventario de Yuno
                     #Poción de Maná
                     #Grimorio

mago.atacar(guerrero) # Vida actual del objetivo es:143.0
guerrero.atacar(mago) # Vida actual del objetivo es:60.0

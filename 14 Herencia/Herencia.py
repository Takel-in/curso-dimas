# Herencia
"""
Que es la herencia
    La herencia es uno de los pilares de la prg orientada a objetos.
    Es un mecanismo o funcionalidad que permite que una clase reciba todas las características, 
          métodos y atirbutos, de otra Clase.
    La clase que hereda, tendrá todos los métidos y atributos de la clase la cual está heredando. 
          Además tendrá también los suyos propios.

Nomencaltura de la herencia
    Superclase
        También conocida como clase padre. Es la clase de la cual se heredan las características. 
        Suele ser más general y sirve de base para otras clases.
    Subclase
        También conocida como clase hijo. Es la clase que recibe la herencia y amplía los métodos 
        y atributos de la superclase con los suyos propios. Suele ser una clase más concreta o específica.

Ejemplo
    Clase:Persona
        Atributos:
            Nombre:str
            Edad:int

    Subclase:Trabajador
        Atributos:
            Nombre:str  #Ese lo hereda de Persona.
            Edad:int    #Ese lo hereda de Persona.
            Suelto:float
            Cargo:str
            Empresa:str

Tipos de hrencia:
    Herencia simple es la forma más básica de herencia que existe, como su nombre bien indica.
        Una subclase hereda de una superclase.
    Herencia jerárquica se produce cuando múltiples subclases hereda de una única superclase.
    Herencia Múltiple se produce cuando una subclase hereda de dos superclases al mismo tiempo.
    Herencia multinivel se produce cuano una subclase herda de una superclase, a su ver, esta 
        superclase hereda de otra superclase.
    
"""

class Persona:
    def __init__(self, nombr, eda, dn):
        self.nombre = nombr
        self.edad = eda
        self.dni = dn

    def presentarse(self):
        print (f"¡Hola!\nMe llamo {self.nombre} y tengo {self.edad} años")

persona = Persona("Oscar", 23, "123456789A")
persona.presentarse() #¡Hola!
                      #Me llamo Oscar y tengo 23 años
print (persona.dni) #3123456789A


class Trabajador(Persona):   #Ponemos entre paréntesis el nombre de la clase de la heredamos.
    pass

# probamos la clase trabajador para ver que en el inicializado le pasamos la inicialización del primera clase. 
trabajador = Trabajador("juan", 33, "23456789B") 
trabajador.presentarse()#¡Hola!
                        #Me llamo juan y tengo 33 años
print(trabajador.dni) #23456789B

class Trabajador2(Persona):   #Ponemos entre paréntesis el nombre de la clase de la heredamos.
    def __init__(self, nombr, eda, dn, sueld, carg, empres): 
        super().__init__(nombr, eda, dn) #Al generar el ini tenemos que llamar a la superclase con los atributos de la misma.
        self.sueldo = sueld
        self.carga = carg
        self.empresa = empres

    def calcularSueldoAnual(self):
        return self.sueldo * 14

#trabajador = Trabajador2("juan", 33, "23456789B") # Genera Excepción porque ahora faltarían los parámetros de la clase hija.
trabajador2 = Trabajador2("juan", 33, "23456789B", 1500, "machaca", "Google" )
trabajador2.presentarse() #¡Hola!
                          #Me llamo juan y tengo 33 años
print (trabajador2.dni)  #23456789B

print (trabajador2.calcularSueldoAnual()) #21000

# Herencia jeráquica
class Estudiante (Persona):

    def __init__(self, nombr, eda, dn, universida, curs, asignatur):
        super().__init__(nombr, eda, dn)
        self.universidad = universida
        self.curso = curs
        self.asignatura = asignatur

    def describirse(self):
        print(f""" ¡Hola soy {self.nombre}!. Tengo {self.edad} años y estudio en la universidad_ {self.universidad}
        Estoy en el curso {self.curso}
        """)

estudiante = Estudiante("María", 20, "345678901C", "Universidad de Madrid", 3, ["programacion", "contabilidad", "cálculo", "algebra"])
estudiante.describirse() # ¡Hola soy María!. Tengo 20 años y estudio en la universidad_ Universidad de Madrid
                         #        Estoy en el curso 3

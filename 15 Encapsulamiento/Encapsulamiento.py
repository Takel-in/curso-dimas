# Encapsulamiento.
"""
    Encapsulamiento
        Pilar funamienta de la poo
        Permite regular el acceso a métodos y atributos de una clase.
        En cierta manera, enmascara la complejidad de una clase.

    Modificadores de acceso
        Metodos y Atributos
            Públicos Son accesibles por
                Cualquier punto del código
                Dentro / Fuera de la clase, subclase,...
            Protegidos Son accesibles por.
                La misma clase
                Las subclases
                Clases dentro del mismo paquete
            Privados Son accesible por:
                unicamente dentro de la misma clase.

    Utilidades
        Nos permite oculatar métods y atributos fuera de la propia clase.
        Podemos regular la modificación de los atributos (privados) evitando que se 
            accedan a ellos directamente. Crearemos métodos (publicos) para modificar 
            los atributos del objeto.
        Enmascarar la complejidad de algunos métodos haciéndoslos privamdos y utilizarlos 
            desde métodos públicos.
    
    Encapsulamiento en Python
                NO EXISTE.

        Es una convención, pero es solo sintaxis, no es funcional
            _atributo = "atributoProtegido". Un guión bajo al principio del nombre de un atributo
                indica que es protegido.
            __atributo = "atributoPrivado". Un doble guión bajo al principiio del nombre de un atributo
                indica que es privado.
            La misma Síntaxis para lo métodos.
            Para Python, todos los atributos y métidoso son Públicos. La convención simplemente se usa 
            entre programadores para indicar cómo se deben usar los métodos y atributos de una clase.
        Existen seudoformas de encapsulación (pero mentira)    

  

"""

class Circulo:
    def __init__(self, radio):
        self.radio = radio
        self.pi = 3.1415

    def calcularPerimetro(self):
        return 2 * self.pi * self.radio

    def calcularArea(self):
        return self.pi * self.radio ** 2

c1 = Circulo(2.5)
print(c1.calcularArea()) #19.634375000000002
print(c1.calcularPerimetro()) #15.707500000000001
print(f"La constante PI es {c1.pi}") #La constante PI es 3.1415

# Si queremos indicar en la clase que las variables radio y pi deberían usarse de manera protegida.
class Circulo:
    def __init__(self, radio):
        self._radio = radio
        self._pi = 3.1415

    def calcularPerimetro(self):
        return 2 * self._pi * self._radio

    def calcularArea(self):
        return self._pi * self._radio ** 2
    
c1 = Circulo(2.5)
print(c1.calcularArea()) #19.634375000000002
print(c1.calcularPerimetro()) #15.707500000000001
print(f"La constante PI es {c1._pi}") #La constante PI es 3.1415  ##Pero esto no queremos que lo haga ya que la consideramos protegido y no publica


# Si queremos indicar en la clase que las variables radio y pi deberían usarse de manera privada.
class Circulo:
    def __init__(self, radio):
        self.__radio = radio
        self.__pi = 3.1415

    def calcularPerimetro(self):
        return 2 * self.__pi * self.__radio

    def calcularArea(self):
        return self.__pi * self.__radio ** 2
    
c1 = Circulo(2.5)
print(c1.calcularArea()) #19.634375000000002
print(c1.calcularPerimetro()) #15.707500000000001
#print(f"La constante PI es {c1.__pi}") #DA error por...
""" Da error porque al poner los 2 guiones bajos lo que hace Python es cambiar el nombre  __pi lo transforma en _Circulo__pi cuando se define el atributo / método
    Es decir __NombreAtributo lo combierte en _NombreClase__NombreAtributo
    Realmente lo hace para evitar nombre de atributos/métodos de clases distintas colisiones
"""
print(f"La constante PI es {c1._Circulo__pi}") #La constante PI es 3.1415. Realmente no encampsula 

# Podemos simular la privacidad (por ejemplo de pi)
# Queremos que nadie nos toque PI aunque sepamos que es metinda.
class Circulo:
    def __init__(self, radio):
        self.radio = radio
        self.__pi = 3.1415

    def calcularPerimetro(self):
        return 2 * self.__pi * self.radio

    def calcularArea(self):
        return self.__pi * self.radio ** 2

    def getPi(self):
        return self.__pi

c1 = Circulo(2.5)
print(c1.calcularArea()) #19.634375000000002
print(c1.calcularPerimetro()) #15.707500000000001
print(f"La constante PI es {c1.getPi()}") #La constante PI es 3.1415


# Ahora vamos a proteger el radio.
class Circulo:
    def __init__(self, radio):
        self.__radio = radio
        self.__pi = 3.1415

    def calcularPerimetro(self):
        return 2 * self.__pi * self.__radio

    def calcularArea(self):
        return self.__pi * self.__radio ** 2

    def getPi(self):
        return self.__pi

    def setRadio(self, valor):
        if type(valor) == int or type(valor) == float:
            if valor > 0:
                self.__radio = valor
                print ("El radio se ha modificado")
            else: 
                print ("El radio no puede ser negativo")
        else:
            print ("El radio debe ser número positivo")


c1 = Circulo(2.5)
print(c1.calcularArea()) #19.634375000000002
print(c1.calcularPerimetro()) #15.707500000000001
print(f"La constante PI es {c1.getPi()}") #La constante PI es 3.1415
c1.setRadio(34)
c1.setRadio(-34)
c1.setRadio("hola que tal")
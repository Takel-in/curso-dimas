# Programación Orientada a Objetos.
"""
Que es la POO
    Es un paradigma de programación cuya intención es imitar los objetos de la vida real (físico o no), 
    con sus propiedades  y comportamiento, en los lenguajes de programación.
Que Aporta.
    Generar código mucho más modular.
    Reutilización del código.
    Encapsulamiento y simplificación.

Que es un objeto.
    Un objeto se forma principalemnte por dos elementos.
        Datos: Describen el estado o las características del objeto. A lospdatos de un objeto los 
        llamaremos propiedades o atributos.
        Código: ejecuta ciertas funcionalidades o comparamiento de dicho objeto. Los llamaremos métodos.
    ej. Objeto: Camiseta.
        Atributos: Una camiseta puede tener un precio, un marca, un color y una talla
        Métodos: Podemos rebajar el precio o teñirla para cambiar su color.

Las Clases
    Una clase es el modelo pra un grupo de objetos.
    La clase define losm étodos y atributos comunes de todos los objetos que pertenen a la misma clase.
    A un objeto que pertenece a una clase se le llama Instancia

    ej. 
    Clase: Camiseta. Todos los objetos de la clase camiseta tendrán un precio, una marca y un coor
    Cada instancia de Camisetas tednrá un precio, color y talla distintos.

    Pilares
    - Herencia
    - Polimorfismo
    - Encapsulación
    - Abstracción.

"""

class Camiseta:
    #En pyton existe un método que se llama __init__ que se ejecuta por defecto cuando generamos una instancia.
    # El método init se encarga de hacer la construcción del objeto.
#    def __init__(self): #sel pasa una referencia a la instancia actual de la clase.
#        self.talla = "XL"
#        self.color = "Rojo"
#        self.precio = 20.99
#        self.marca = "Adimas"

    def __init__(self, marc, preci, tall, colo): #sel pasa una referencia a la instancia actual de la clase.
        self.talla = tall
        self.color = colo
        self.precio = preci
        self.marca = marc
        self.rebajada = False


    #Los métodos que se crean dentro de la clase tiene que recibir el parámetros self obligatoriamente.
    def aplicarDescuent(self, porcentaje):
        self.precio = self.precio - self.precio * porcentaje / 100
        if porcentaje < 100:
            self.rebajada = True

    def infoProduct(self):                                                    #:.2f -> Que no ponga más de 2 decimales.
        info = f"Descripción de la camiseta:\nMarca: {self.marca}\nPrecio: {self.precio:.2f}\nTalla: {self.talla}\nColor: {self.color}"
        if self.rebajada:
            info += "\nEste producto está rebajado."
        return info
        



#camisetaRoja = Camiseta() #Es como generar una instancia de la clase que hemos creado.
#print (camisetaRoja.color) #Rojo

#camiseta = Camiseta()
#print (camiseta.precio) #20.99

camiseta2 = Camiseta("Nike", 19.99, "S", "rojo")
print (camiseta2)
print (camiseta2.color) #rojo

print (camiseta2.precio)#19.99
camiseta2.aplicarDescuent(50)
print (camiseta2.precio)#9.995

print (camiseta2.infoProduct()) #Descripción de la camiseta:
                                #Marca: Nike
                                #Precio: 9.995
                                #Talla: S
                                #Color: rojo
                                #Este producto está rebajado.
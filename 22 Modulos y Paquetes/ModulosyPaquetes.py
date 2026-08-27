# Modulos y paquetes.
#1 Los módulos son archivos python (o de Cpython o de C)
#   Estos archivos pueden contener funciones, clases y variables.
#   Podemos imporatarlas a nuestros archivos para hacer uso de estas
#   sin tener que volver a escribir el código.

import calcularArea #Esto es un fichero donde hemos escrito las funciones.

print(calcularArea.PI) #3.1415
print(calcularArea.areaCirculo(5)) #78.53750000000001

from calcularArea import areaCuadrado   #importamos específicamente esa función.
print(areaCuadrado(3)) #9
#print(areaTriangulo(5, 5)) #Da error  porque no está definido.

from calcularArea import areaCuadrado, areaTriangulo   #importamos específicamente esas 2 funciones.
print(areaTriangulo(5, 5)) #12.5

from calcularArea import * #Importa todas las funciones del módulo.
print(areaCirculo(5)) #78.53750000000001


# 2 Los paquetes son conjuntos de móduclos, relacionados entre si, en un mismo directorio.
# vamos a importar nuestro paquete (que es el nombre del directorio)
from Paquete import calcularPerimetros #Del paqute nos traemos el modulo Calcular perímtros.
cp = calcularPerimetros.CalcularPerimetros()

#Se puede tambien.
from Paquete.calcularPerimetros import CalcularPerimetros
cp = CalcularPerimetros()

#Se puede igualmente. 
from Paquete.calcularPerimetros import CalcularPerimetros as CP  #aQUÍ RENOMBRAMOS
cp = CP()
print(cp.perimteroCirculo(2)) #12.566370614359172

from Paquete.calcularArea import * #trameos todo lo de geometria.
print(calcularArea.areaCirculo(3))

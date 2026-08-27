# Funciones LAMBDA
"""
Funciones LAMBDA:
Son funciones anónimas (sin nombre):
- Permiten múltiples argumentos.
- Solo pueden tener una expresión.
- Estructura: lambda arg1, arg2 : Expresión
"""

# 1 Definir una función lambda
suma = lambda a, b : a+b
print (suma (5, 5)) #10
print (suma(3,2)) #5

saludar = lambda nombre: f"hola {nombre}"
print(saludar("juan"))#hola juan

saludar = lambda nombre: print(f"hola {nombre}")
saludar ("juan") #hola juan


# 2 LLamar funciones dentro de lambda.
# Dentro de la expresión de una función lambda podemos llamar otras funciones.
maximo = lambda a, b, c : f"el máximo entre {a}, {b}, {c} es {max(a,b,c)}"
print(maximo (1, 2, 3)) #el máximo entre 1, 2, 3 es 3


# 3 Funciones lambda dentro de funciones.
# Podemos definir funciones lambda dentro de funciones convencionales.

# Esto nos permite generar funciones lambda con distintos párametros.

def ponerPrefijo(prefijo):
    return lambda nombre: f"{prefijo} {nombre}"

addMr = ponerPrefijo("Mr")  #Lo que hace aquí es retornar la función lambda pero ya rellena el campo prefijo de manera que devuelve  lambda nombre: f"Mr {nombre}"
addSr = ponerPrefijo("Sr")
addMiss = ponerPrefijo("Miss")

print(addMr("Juan")) #Mr Juan
print(addSr("Julian"))#Sr Julian
print(addMiss("Nerea"))#Miss Nerea

def elevarA(exponente):
    return lambda base : base**exponente

elevarCuadrado = elevarA(2) # Aqui lo que hace es que elevarcuadrado es una función con valor lambda base : base**2
elevarCubo = elevarA(3)

print (elevarCuadrado(3)) #9  Ejecuta la función LAMBDA con el parámetro. 
print (elevarCubo(2)) #8

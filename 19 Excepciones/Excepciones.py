# Excepciones
"""

    Las excepciones son errores que ocurren durante la ejecucción del programa.
    Estos errores surgen a pesar de que la sintaxis sea correcta.
    ejemplos.
        - Acceder a una posición de una lista superior a la longitud de esta.
        - Intentar abrir un fichero que no existe.
        - Convertir "ldasfldj" a int.
    IMPORTANTE: Gestionar las excepcioens nos permite que el código se siga ejecutanto 
                a pesar de que ocurran errores.

"""

# a = 20/0 # Esto produce la excepción siguiente -> ZeroDivisionError  . El programa finaliza y no ejecuta ya ninguna línea.
#"""
#Exception has occurred: ZeroDivisionError
#division by zero
#  File "C:\Users\frjoma\python-learning\curso-dimas\19 Excepciones\Excepciones.py", line 15, in <module>
#    a = 20/0
#        ~~^~
#ZeroDivisionError: division by zero
#"""

# Apartdo 1: Bloque try: except:
# Dentro del bloque try, ejecutamos el código que queremos evaluar (ver si lanza algún error). Dentro del bloque catch
def division(a, b):
    try:
        res = a/b
        print (res)
    except ZeroDivisionError:
        print("No se puede dividir por 0")

division(5, 5) #1.0
division(5, 0) #No se puede dividir por 0
print ("Hola que tal") #Hola que tal


# Apartado 2 Gestión de distintos tipo de excepciones.

frutas = ["0-Platano", "1-Manzana", "2-Pomelo", "3-Melocoton"]

def elegirFruta(listaFurtas):

    try:
        print (listaFurtas)
        index = int(input("Elige una fruta (Pon el número): "))
        print (f"Su fruta favotia es {listaFurtas[index]}")
    except IndexError:
        print(f"Indice incorrecto, debe estar entre 0 y {len(listaFurtas)-1}")
    except ValueError:
        print (f"Debes poner un número entero")

elegirFruta(frutas) #['0-Platano', '1-Manzana', '2-Pomelo', '3-Melocoton']
                    #Elige una fruta (Pon el número): 
                    # Si indico 1 -> Su fruta favotia es 1-Manzana

elegirFruta(frutas) #['0-Platano', '1-Manzana', '2-Pomelo', '3-Melocoton']
                    #Elige una fruta (Pon el número): 
                    # Si indico Pomelo -> Debes poner un número entero

elegirFruta(frutas) #['0-Platano', '1-Manzana', '2-Pomelo', '3-Melocoton']
                    #Elige una fruta (Pon el número):
                    # Si indico 88 -> Indice incorrecto, debe estar entre 0 y 3

# Apartado 3: Excpción Exception.
# Las excepciones son objetos que heredan de la clase Exception.


frutas = ["0-Platano", "1-Manzana", "2-Pomelo", "3-Melocoton"]

def elegirFruta(listaFurtas):

    try:
        print (listaFurtas)
        index = int(input("Elige una fruta (Pon el número): "))
        print (f"Su fruta favotia es {listaFurtas[index]}")
    except Exception:
        print(f"Ha ocurrido un error, algo ha salido mal")
    
elegirFruta(frutas) #['0-Platano', '1-Manzana', '2-Pomelo', '3-Melocoton']
                    #Elige una fruta (Pon el número): 
                    # Si indico 90 -> Ha ocurrido un error, algo ha salido mal

#LAS EXCEPCIONES SE PUEDEN RENOMBAR.  
# Donde poner except Exception:   se puede poner except Excepcion as errorgenerico:

# Podemos saber la descripción si renombramos el error con as....

frutas = ["0-Platano", "1-Manzana", "2-Pomelo", "3-Melocoton"]

def elegirFruta(listaFurtas):

    try:
        print (listaFurtas)
        index = int(input("Elige una fruta (Pon el número): "))
        print (f"Su fruta favotia es {listaFurtas[index]}")
    except Exception as errorcito:
        print(errorcito)
    
elegirFruta(frutas) #['0-Platano', '1-Manzana', '2-Pomelo', '3-Melocoton']
                    #Elige una fruta (Pon el número): 
                    # Si indico 90 -> list index out of range

# Nos podemos traer el módulo loggin.
import logging

frutas = ["0-Platano", "1-Manzana", "2-Pomelo", "3-Melocoton"]

def elegirFruta(listaFurtas):

    try:
        print (listaFurtas)
        index = int(input("Elige una fruta (Pon el número): "))
        print (f"Su fruta favotia es {listaFurtas[index]}")
    except Exception as errorcito:
        logging.exception("El error es el siguiente") #Imprime una descripción detallada del error.1
    
elegirFruta(frutas) #['0-Platano', '1-Manzana', '2-Pomelo', '3-Melocoton']
                    #Elige una fruta (Pon el número): 
                    # Si indico 90 -> ERROR:root:El error es el siguiente
                                    # Traceback (most recent call last):
                                    #   File "c:\Users\frjoma\python-learning\curso-dimas\19 Excepciones\Excepciones.py", line 115, in elegirFruta
                                    #     print (f"Su fruta favotia es {listaFurtas[index]}")
                                    #                               ~~~~~~~~~~~^^^^^^^
                                    #IndexError: list index out of range


# Apartado 4: Else, Finally, Raise
# Vamos a sumar los números que nos pase el usuario sepradosp or espacios:

while True:
    try:
        total = 0
        sumandos = input("Ponme numeros separados por espacios: ")
        sumandos = sumandos.split()
        for num in sumandos:
            if num.isnumeric():
               total += float(num) 
            else:
                #Yo puedo lanzar una excepción.
                raise ValueError(" El valor no es un número ")
    except ValueError:
        print ("Los datos son incorrectos")
        print ("Vuelve a introducir los números")

    else: #Se ejcuta si el bloque true se ha comprado con ninguna excepción.
        print (f"El valor de la sum es {total}")
        break

    finally: # ejecuta este bloque independientemente de si hay o no la excepción.
        print ("Ha terminado el ejercicio.")

#   LA EJECUCION DEL WHILE SALE POR PANTALLA 
# Ponme numeros separados por espacios: 1 2 3 4 5
# El valor de la sum es 15.0
# Ha terminado el ejercicio.

# Ponme numeros separados por espacios: 1 2 a 3 4
# Los datos son incorrectos
# Vuelve a introducir los números
# Ha terminado el ejercicio.
#Capitulo 11 Args y Kwargs


# Argumentos arbitrarios:
# Los argumentos arbitrarios se utilizancuando no sabemos de forma exacta el número de parámetros quue
# la función va a recibir.

# Función de ejemplo para mostrar los argumentos arbitrarios. La función busca el maximo elemento de los que se introducen.
def maximo (*args):  # EL ASTERISCO INDICA QUE SE PASARÁN X ARGUMENTOS.  Python genera una lista con los valores que pasa
    maximo = args[0]
    for numero in args[1:]:
        if maximo < numero: 
            maximo = numero
        
    return maximo

print (maximo (10, 20, 30, 20, 90, -110, 22.3, 9.2)) #90
print (maximo (1, 2, 3, 4)) # 4

# Lo de arriba sería lo mismo si pasamos una lista de números.
def maximo2 (listaNumeros):  # EL ASTERISCO INDICA QUE SE PASARÁN X ARGUMENTOS.  Python genera una lista con los valores que pasa
    maximo = listaNumeros[0]
    for numero in listaNumeros[1:]:
        if maximo < numero: 
            maximo = numero
        
    return maximo
print(maximo2([10, 20, 30, 20, 90, -110, 22.3, 9.2])) #90
print(maximo2([1, 2, 3, 4])) # 4

# Ejemplo porque es interesante *args Porque depende de los que se quies argumentos que dependen de otros argumenos.
def formatoDescarga(tipo, *args):
    numArgs = len(args)

    if tipo == "video":
        if numArgs == 0:
            print (f"El formato seleccionado:\n-Tipo de arhcivo: {tipo}")
        elif numArgs == 1:
            print (f"El formato seleccionado:\n-Tipo de arhcivo: {tipo}\n-La resolución:{args[0]}")
        elif numArgs == 2:
            print (f"El formato seleccionado:\n-Tipo de arhcivo: {tipo}\n-La resolución:{args[0]}\n-FPS:{args[1]}")
    elif tipo == "audio":
        print (f"El formato seleccionado:\n-Tipo de arhcivo: {tipo}")
    else:
        print (f"Tipo de formato incorrecto")

formatoDescarga("video", 720)   #El formato seleccionado:
                                #-Tipo de arhcivo: video
                                #-La resolución:720
formatoDescarga("video", 1080,60)   #El formato seleccionado:
                                    #-Tipo de arhcivo: video
                                    #-La resolución:1080
                                    #-FPS:60
formatoDescarga("audio")    #El formato seleccionado:
                            #-Tipo de arhcivo: audio



# Keyword ARguments
# Podemos pasar los argumentos de una función mediante keywords. De esta forma conseguimos que el 
# orden de los argumentos sea indiferente.

def crearPersonajes (clase, raza, nombre):
    print(f"{nombre.upper()} es un {clase} de raza {raza}")

# Para pasar desordenados los argumentos pasamos utilizando las mismas palabras que hemos usado en la 
# deficicion de la función
crearPersonajes(nombre="Tantaleon", clase="leñador", raza="humano") # TANTALEON es un leñador de raza humano
crearPersonajes("leñador", "elfo", "pepito") # PEPITO es un leñador de raza elfo




# Keword arbitrary arguments.
# Se utilizan cuando no sabemos cúantos argumentos de vlabra clave vamos a recibir.
def printKwargs(**kwargs):  #Hay que poner los dos ** .  
    print("\n")
    print("Los atributos del personaje son: ")
    for clave, valor in kwargs.items():
        print (f"{clave} --> {valor}")

printKwargs(nombre="Tantaleon", clase="leñador", raza="humano", mascota="perrito", clant="tv")  #
                                                                                                #Los atributos del personaje son:
                                                                                                #nombre --> Tantaleon
                                                                                                #clase --> leñador
                                                                                                #raza --> humano
                                                                                                #mascota --> perrito
                                                                                                #clant --> tv

printKwargs(nombre="Tantaleon", clases="elfo", razas="humano")  #
                                                                #Los atributos del personaje son:
                                                                #nombre --> Tantaleon
                                                                #clases --> elfo
                                                                #razas --> humano

# Combinación de todos los anteriores.
# Se puede usar conjuntamente en unamisma función 

def crearPersonaje2 (nombre, *args, **kwargs): #Nombre Olbigatorio, *args para características, **wargs para otros aspecto del personaje.
    descripcion = f"### {nombre.upper()} ###\n\n"
    descripcion += "### DESCRIPCION \n\n"
    for clave, valor in kwargs.items():
        descripcion += f"-{clave} --> {valor}\n"
    descripcion += "### HABILIDADES ###\n\n"
    for habilidad in args:
        descripcion += f"-{habilidad}\n"
    return descripcion

print (crearPersonaje2 ("pepito", "ataque fuerte", "bola de fuego", clase="mago", raza="elfo", mascota = "serpiente"))

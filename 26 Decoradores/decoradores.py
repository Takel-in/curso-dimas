#Decoradores
"Los decoradores sirven para modificar el comportamiento de una función."

"""
1 Las funciones son objetos:
Por tanto:
    - Es una instancia de tipo objeto
    - Podemos almacenar una función en una variables
    - Podemos pasar una función como parámetro de otra función
    - Una función puede retornar otra función
    - Se puden almacenar en estructuras de datos, tablas, listas...
"""
def funcionExterna (nombre):

    def funciónEnvoltorio():
        print ("Empieza la función envoltorio")
        print (nombre)
        print ("Final de la función envoltorio\n")

    return funciónEnvoltorio

funcionExterna("Dimas") #REalmente no hace nada porque solamente se ha definnido las funciones pero no está llamando al envoltorio y además devuelvo el objeto

def funcionExterna (nombre):

    def funciónEnvoltorio():
        print ("Empieza la función envoltorio")
        print (nombre)
        print ("Final de la función envoltorio\n")

    return funciónEnvoltorio()

funcionExterna("Dimas") #Empieza la función envoltorio      Aquí si se ejecuta porque el return llama a la función envoltorio 
                        #Dimas
                        #Final de la función envoltorio


def funcionExterna (nombre):

    def funciónEnvoltorio():
        print ("Empieza la función envoltorio")
        print (nombre)
        print ("Final de la función envoltorio\n")

    return funciónEnvoltorio

instanaciafuncion = funcionExterna("Dimas") #Aqui lo que hacemos el pasar el objeto a la variable por lo que la variable se convierte
instanaciafuncion() #Empieza la función envoltorio      Aquí si se ejecuta porque se llama a la función.
                    #Dimas
                    #Final de la función envoltorio

otrafuncion = funcionExterna("Maria") 
otrafuncion() #Empieza la función envoltorio
              #Maria
              #Final de la función envoltorio

print(otrafuncion.__name__) # funciónEnvoltorio


"""
2 Función como argumento de otra función.
En vez de pasar la variable "nombre", pasaremos otra función
"""

from datetime import datetime  #Módulo que sirve para manipular la fecha.

def fecha():
    print(datetime.today().strftime("%d-%m-%Y"))

fecha() # 01-09-2026

def hora():
    print(datetime.now().strftime("%H:%M:%S"))

hora() #20:48:06

def funcionExterna(funcionInterna):

    def funcionEvnoltorio():
        print("\nEmpieza la función")
        funcionInterna()
        print("fin de la funcion\n")

    return funcionEvnoltorio

mostrarHora = funcionExterna(hora) # Empieza la función
                                   # 20:52:08
                                   # fin de la funcion
mostrarFecha = funcionExterna(fecha) # Empieza la función
                                     # 01-09-2026
                                     # fin de la funcion
mostrarHora()
mostrarFecha()



"""
3 Sintaxis de los decoradors.
Vamos hacer lo mismo del punto 2 pero con síntaxis de Python.
"""

def funcionExterna(funcionInterna):

    def funcionEvnoltorio():
        print("\nEmpieza la función")
        funcionInterna()
        print("fin de la funcion\n")

    return funcionEvnoltorio

@funcionExterna
def saludar(): # Esto sería la función interna
    print ("Hola crack.") 
@funcionExterna
def despedirse(): # Esto sería la función interna
    print ("Adios máquina.") #Empieza la función
                             #Adios máquina.
                             #fin de la funcion

saludar() #Empieza la función
                          #Hola crack.
                          #fin de la funcion

despedirse()#Empieza la función
                             #Adios máquina.
                             #fin de la funcion



"""
4 Funciones con argumentos
Veremos cómo podemos usar decoradores con funciones que reciban diferentes números de argumentos
"""

def sumarNumeros(*args, **kwargs):
    res = 0
    for num in args:
        res += num
    return res

print(sumarNumeros(1,2,3,4,5,6,7,8,9,10)) #55

def operaConPares(operacion):

    def wrapper(*args, **kwargs ): 
        soloPares = list(filter(lambda num : num%2 == 0, args))
        res = operacion(*soloPares, **kwargs)
        print (f"El resutlado de la operación es: {res}")
        return res

    return wrapper

sumarPares = operaConPares(sumarNumeros)
sumarPares(1,2,3,4,5,6) # El resutlado de la operación es: 12


@operaConPares
def multiplicar(*args, **kwargs ):
    res = 1
    for num in args:
        res *= num
    return res

multiplicar(1,2,3,4) #El resutlado de la operación es: 8



#Vamos hacer el ejercicio y tenemos que devolver el resultado de la multiplicación siempre y cuando no supere un valor máximo.
#Si pasa del valor máximo devolvemos el valor máximo.
#Hay que hacelor con kwars

def operaConPares(operacion):

    def wrapper(*args, **kwargs ): 
        soloPares = list(filter(lambda num : num%2 == 0, args))
        res = operacion(*soloPares, **kwargs)
        print (f"El resutlado de la operación es: {res}")
        return res

    return wrapper

@operaConPares
def multiplicar(*args, **kwargs ):
    res = 1
    for num in args:
        res *= num
    if "max" in kwargs.keys():
        return min(kwargs["max"], res)
    return res

multiplicar(1,2,3,4) #El resutlado de la operación es: 8
multiplicar(1,2,3,4, max=50) #El resutlado de la operación es: 8
multiplicar(1,2,3,4, max=6) #El resutlado de la operación es: 6


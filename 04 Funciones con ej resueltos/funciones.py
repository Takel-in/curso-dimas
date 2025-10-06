# Capítulo 4 Funciones
# Definición de las funciones, se usa la palabra reservada def y es toda la función.
def saludar():
    print("saludo dentro de la función. ")

saludar()
saludar() #A esto se le llama llamar a la función
saludar()

#Funciones con argumentos
def saludar2(nombre):
    print(" Saludamos dentro de la función con el valor -> " + nombre + " <-") # los  + se usan para concatenar cadenas de texto
    saludar()

saludar2("Maria ")
saludar2("Marta " + "Manueala ")
saludar2("123456789")

#Funciones con reteornos
def suma (a, b):
    resultado = a + b
    return resultado #Resultado al estar definida dentro de la función es local.

valor = suma (10, 5) #valor al estar definida fuera de la función es global.
print (valor)
print (suma (2.3, 4))

def suma2(a, b):
    return a+ b

valor = suma2 (10, 5) #valor al estar definida fuera de la función es global.
print (valor)
print (suma2 (2.3, 4))

def sonIguales(num1, num2):
    return num1 == num2

print (sonIguales(2,4))
print (sonIguales(4,4))

verdad = sonIguales(2,4)
if (verdad):
    print ("Son iguales")
else:
    print ("Son diferentes. ")

#Funciones con argumentos con valor por defecto.

    #sonIguales() #Da Error he indica que falta 1 argumento.
    #sonIguales(1) #Da error he indica que falta unargumento.
def saludaPorDefecto(nombre="nombre por defecto"):
    print ("hola " + nombre + " escrito")


saludaPorDefecto()
saludaPorDefecto("este es otro nombre que no es por defecto ")


#Funciones que teronan varios valores
def sumaYResta(a, b):
    suma = a + b
    resta = a - b
    #return suma, resta 
    return a + b, a - b

resultado1, resultado2 = sumaYResta(10, 5)
print ("resultados:\nSuma: " + str(resultado1) +"\nResta: " + str(resultado2) )


"""
EJERCICIO 1: Función máximo -> Dados dos números, la función de encontrar cual del os dos
es el más grande y retornalo.
Extra: Se debe comprobar que los aargumentos de la función sean de tipo int o float. 
Si alguno de los dos no lo es, mostrar un error y retornar false.
"""
def maximo(n1, n2):
    if ((type(n1) == int or type(n1) == float)and (type(n2) == int or type(n2) == float) ):
        return n1 if n1 > n2  else n2
    else :
        print ("Algunos de los valores no es numérico. n1 -> " + str(n1) + " n2 -> " + str(n2))
    return False

print ( maximo(1, 2) if maximo(1, 2) != bool else "El valor no es adecuado" )
print (maximo(1, 1))
print (maximo(2, 1))
print (maximo("uno", 2))
print (maximo("dos", 2))
"""
EJERCICIO 2: Mini calculadora. Pedir al usuario una operación y dos números.
Las operaciones pueden ser suma, resta, potencia. Si introducie una opración diferente
a estas, mostrar un mensaje de error. Si la operación es correcta, mostrar el resutlado.
"""
def sumaej2(a, b):
    return a + b

def restaej2 (a, b):
    return a - b

def potenciaej2 (a, b):
    return a ** b

def calculadora ():
    ope = input("Introduce una operación. ")
    if (ope != "+" and ope != "-" and ope != "*"):
        print ("Selecciona un tipo de operación válido '+', '-', '*'")
        return
    
    n1 = input ("Introduce el primer valor. ")
    n2 = input ("Introduce el segundo valor. ")
    if (n1.isnumeric() and n2.isnumeric() ):
        n1 = int(n1)
        n2 = int(n2)
        if (ope == "+"):
            print (sumaej2(n1, n2)) # Si solo es una variable o el resultado de una operación aunque se numérico podrá imprimirlo
        elif (ope == "-"):              #No podría hacerlo si estuviera concadenado cosas.
            print (restaej2 (n1, n2))
        elif (ope == "*"):    
            print (potenciaej2 (n1, n2))
    else:
        print ("Algunos de los valores no es numérico. n1 -> " + n1 + " n2 -> " + n2)

calculadora()
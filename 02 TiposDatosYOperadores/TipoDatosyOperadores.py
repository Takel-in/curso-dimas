# Variables, Tipo de datos y Operadores Aritméticos.
""" Comentarios
    de varias líneas """

# VARIABLES

"""
numero = 1
numeroUno = 1 # Es una variable distinta porque python diferencia entre mayúsculas y minúsculas
numero1dos = 2 # No se pueden poner número al inicio de la variable.
"""

# TIPOS DE DATOS NÚMÉRICOS
numero_entero = 1 #int
print (numero_entero)  #Imprimer el valor. 1
print("numero_uno") #Imprime el texto. numero_uno

numero_decimal = 2.46 #float
print (numero_decimal) #2.46

numero_entero = numero_entero + 2
print(numero_entero) #3

numero = numero_entero + numero_decimal #Poemos sumar enteros + decimales.
print(numero) #5.46

numero_entero+= 2 # versión abreviada de numero_entero = numero_entero + 2
print (numero_entero) #5

variable_numerica = 20
variable_numerica = variable_numerica - 10
print(variable_numerica) #10

variable = 10 
variable = variable / variable_numerica #Al dividirlos pasa a ser un float.
print (variable) #1.0

numero = 2/2 + 3
print (numero) #4.0

mutiplicacion = 2 * 3
print (mutiplicacion) #6

mutiplicacion = numero_entero * numero_decimal
print (mutiplicacion) #12.3

potencia = 2 ** 3
print(potencia) #8

modulo = 11/2 #valor de la división y no el resto
print (modulo) #5.5
modulo = 11%2 #El resto de una división
print (modulo) #1

# Tipos de datos de texto
texto1 = "Esta es nuestra frase"
print (texto1) #Esta es nuestra frase
texto2 = "texto 'entre comillas simples' guay"
print (texto2) #texto 'entre comillas simples' guay
texto3 = 'Texto "entre Comillas dobles" guay'
print (texto3) #Texto "entre Comillas dobles" guay
texto4 = 'texto'
print (texto4) #texto

Texto5_con_formato = """ Esto es un texto 
texto con formato y 
Saltos de líneas"""

print (Texto5_con_formato) # Esto es un texto 
                            #texto con formato y
                            #Saltos de líneas
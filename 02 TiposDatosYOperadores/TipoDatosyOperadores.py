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
print (numero_entero)  #Imprimer el valor
print("numero_uno") #Imprime el texto

numero_decimal = 2.46 #float
print (numero_decimal)

numero_entero = numero_entero + 2
print(numero_entero)

numero = numero_entero + numero_decimal #Poemos sumar enteros + decimales.
print(numero)

numero_entero+= 2 # versión abreviada de numero_entero = numero_entero + 2
print (numero_entero)

variable_numerica = 20
variable_numerica = variable_numerica - 10
print(variable_numerica)

variable = 10 
variable = variable / variable_numerica #Al dividirlos pasa a ser un float.
print (variable)

numero = 2/2 + 3
print (numero)

mutiplicacion = 2 * 3
print (mutiplicacion)

mutiplicacion = numero_entero * numero_decimal
print (mutiplicacion)

potencia = 2 ** 3
print(potencia)

modulo = 11/2 #valor de la división y no el resto
print (modulo)
modulo = 11%2 #El resto de una división
print (modulo)

# Tipos de datos de texto
texto1 = "Esta es nuestra frase"
print (texto1)
texto2 = "texto 'entre comillas simples' guay"
print (texto2)
texto3 = 'Texto "entre Comillas dobles" guay'
print (texto3)
texto4 = 'texto'
print (texto4)

Texto5_con_formato = """ Esto es un texto 
texto con formato y 
Saltos de líneas"""

print (Texto5_con_formato)
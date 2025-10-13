# Capitulo 8 Cadenas de texto o string
# Repaso conceptos básicos
texto = "Hola mundo"
print ("Hola Mundo") # Hola Mundo

texto = 'Hola mundo'
print (texto) # Hola mundo

#Esto nos permite poder introducir las comillas contrarias dentro de la propia string sin falta de caracteres de excepción.
comillasSimples = "Hola 'Mundo' " # Hola 'Mundo' 
print (comillasSimples)
comillasDobles = 'Hola "Mundo"' # Hola "Mundo"
print (comillasDobles)

stringConFormato = """ 
Hola 
               Mundo 
    Se muestra como se haya definido.
"""
print (stringConFormato)
#  Aqui es como se muestra en la pantalla al imprimir. Exactamente igual.
#Hola
#               Mundo
#    Se muestra como se haya definido.
#

# Convertir valores a string.
valorEntero = 5
ValorDecimal = 3.14
valorBooleano = False
print(type(valorEntero)) # <class 'int'>
print(type(ValorDecimal)) # <class 'float'>
print(type(valorBooleano)) # <class 'bool'>

valorEntero = str(valorEntero)
valorDecimal = str(ValorDecimal)
valorBooleano = str(valorBooleano)
print(type(valorEntero)) # <class 'str'>
print(type(valorDecimal)) # <class 'str'>
print(type(valorBooleano)) # <class 'str'>


# Longitud de una str.
texto="0123456789"
print ("La longitud del texto es " + str(len(texto))) #La longitud del texto es 10

# concadenar str

texto1 = "01234"
texto2 = "56789"
texto3 = texto1 + texto2
print(texto3) # 0123456789


#Los string son listas (No es realmente así, pero comparten algunas similitudes)
#En este apartado descubriremos que realmente los stringo son Arrays o vectores (similar a las listas)
texto = "0123456789"
primerCaracter = texto[0]
substring = texto [1:5]
print (texto) # 0123456789
print (primerCaracter) # 0
print (substring) # 1234

ultimoCaracter = texto[-1]
print (ultimoCaracter) # 9

for c in texto:  #0 1 2 3 4 5 6 7 8 9 (Va imprimiento caracter a caracter. cada uno de ellos en una nueva línea.)
    print(c)


"Ejercicio (mini): Tenemos un string únicamente compuesto por números enteros."
"Debemos sumar su valor uno a uno y mostrar por pantalla la suma total de todos los números."

Texto ="123456789"
suma = 0
for c in texto:
    suma += int(c)
else: #REcordar que else aquí se ejecuta si se ha realizado una salida sin break del for. Es mo un punto final del for.
    print ("El resultado total es " + str(suma))

#Format String
# Nos  permiten generar string cominando texto con otras variables de forma sencilla y legible.
#Ej. Tenemos 5 Garrafas a un precio de 1.50 euros cada garrafa. Vamos a presentarlo de varias formas.
cantidad = 5
precio = 1.50

print("Forma de concatenación: Has comprado " + str(cantidad) + " garrafas a un preción de " + str(precio) + " por garrafa lo que da: " + str(cantidad * precio))
# Forma de concatenación: Has comprado 5 garrafas a un preción de 1.5 por garrafa lo que da: 7.5

texto = "Format String Basico:  Has comprado {} garrafas a un preción de {} por garrafa lo que da: {}".format(cantidad, precio, cantidad * precio)
print (texto) # Format String Basico:  Has comprado 5 garrafas a un preción de 1.5 por garrafa lo que da: 7.5

print(f"Format String Basico:  Has comprado {cantidad} garrafas a un preción de {precio} por garrafa lo que da: {cantidad * precio}")

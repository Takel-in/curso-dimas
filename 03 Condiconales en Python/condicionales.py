# Capítulo 3: Booleanos, condicones y entrada de usuario.

# Entrada de datos del usuario. Identificación del tipo de dato.

edad = input("introducie la edad.")
print (edad)
tipo_de_datos = type(edad) #Te dice el tipo de dato que es edad.
print (tipo_de_datos)

#BOOLEANOS, IF   ( Comparadores == != > < >= <= )
verdadero = True
falso = False
if (verdadero==True): #Recordar que ==  es para decir igual,
    #Se generan unos espacios y se alinea así para indicar que se ejecute todo lo que cumpla la condición.
    #Si no se cumple simplemente sigue con la siguiente instrucción que esté alineada a la misma altura.
    print("Soy verdadero") #La identación se hace con espacios.

#Cuando ya no queremos que se ejecute lo que hay dentro simplemente volvemos a la identación anterior para que el sitema
#siga ejecutando.  

#Esto no debería ejecutarse.
if (falso == True): #En esta ocasión no se cumplirá la condición
        print ("Son iguales")

if (falso == False):
    print ("Es cierto que falso == False")


#Operadores de Comparación, elif, else
edad = input("Introducie la edad")
edad = int(edad) #Convertimos el str de número a un numero realmente.

if(edad >=18):
    print("Eres mayor de edad, pasa")
elif(edad < 0):
    print("No es posible")
elif(edad < 14):
    print ("eres muy pequeño")
else:
    print("No eres mayor de edad, no pasas")
     
   
#Operadores lógico   and -> Se tienen que cumplir todos, or -> se tiene que complir una, not -> invierte la lógica   (se usan para coprobar varias expresiones a la vez.)
edad = input("Introducie la edad")
edad = int(edad) #Convertimos el str de número a un numero realmente.

if (type (edad) == int ):
    if (edad > 120 or edad < 0):
        print ("Esto no es posible")
    elif (edad >= 18 and edad < 40):
        print ("Puedes entrar")
    elif (edad < 18 and edad > 15):
        print ("Todavía eres menor")
    else:
        print ("no ha sucedido ninguan de las condiciones")
else:
    print("La edad no es un número entero")

if(not(edad < 18)):
    print ("Puedes pasar")



""" 
Ejercicio: Comprobar si el usuario introduce un número, si no es un número
indicar que debe introducir un entero. Si es un número, deberemos comprobar
si es o no par y notificarlos al usuario.

PISTAS:
is numeric, num%2=0
"""

numero = input("introduce un numero para el ejercicio")
if (not numero.isnumeric()):
    print ("Debes introducir un número")
else:
    if (int(numero) % 2 == 0):
        print("Es par")
    else:
        print ("Es impar")

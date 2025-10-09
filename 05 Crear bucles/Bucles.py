#Capítulo 5: Bucles

#Introducción a las listas.
# Es un tipo de dato que agrupa información.
# Posicones empiezan en la posición 0 y va a la n-1
# Longitud es el número de elementos que tiene la lista.
numeros = [1, 2, 3, 4, 5]

print (numeros[0]) #pongo la posición a la que quiero acceder. #1
print (numeros) #imprimido todos los números. #[1, 2, 3, 4, 5]
print (len(numeros)) #Imprime el número de elementos que contiene #5

texto = ["juan", "botella", "taza"]
print (texto) #['juan', 'botella', 'taza']
print (texto[0]) #juan
print (len(texto)) #3

variada = [1, 2.3, False, "hola "]
print (variada) # [1, 2.3, False, 'hola ']
print (variada[0]) #1
print (len(variada)) # 4
print (variada[len(variada)-1]) #Impresión del último elemento. #hola 

# Bucles : for
for i in range(5):    #Range empieza a valer desde 0 y por defecto aumenta en 1.
    print(i) #0 1 2 3 4
print ("Final del bucle")

for x in range(1, 7): #Límite inferior y superior, el superior no es inclusivo.
    print (x) #1 2 3 4 5 6
print ("Final del bucle")

for x in range(1, 7, 2):  #indicamos el aumento de valores 
    print (x) # 1 3 5
print ("Final del bucle")


# Mini ejemplo, imprimir solo las volcales de una palabra
for x in "cadena de texto a revisar":    #Itersa sobre los caracteres de la palabra que se le pasa.
    if (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'):
        print (x) #a e a e e o a e i a

# Mini ejemplo, iterar sobre una lista
numeros = [22, 33, 44, 55]
for numero in numeros:
    print (numero) # 22 33 44 55
    numero+=10
    print(numero) #34 43 54 65
print (numeros)   #Comprobamos que no se modifica la lista porque numero es una variable local dentro del for. [22, 33, 44, 55]

for i in range(len(numeros)):   #No hace falta hacer n-1 porque ya lo hace en range por si solo. Si se pone n-1 en range estaría mal, no se haría el último elemento.
    numeros[i]+=10   #Acceso a cada valor de la lísta de número que no es interna al bucle.
print (numeros) #[32, 43, 54, 65]

#Bucle While.
#Ejecutar el código hasta que se cumpla una condición.
cnt = 0
while(cnt < 10):
    print(cnt) # 0 1 2 3 4 5 6 7 8 9
    cnt +=1

#Encontrar la primea a en una frase.
letraEncontrada = False
letra ="a" #letra a encontrar.
frase = "En este momento estoy buscando la letra a"
indice = 0
while (not(letraEncontrada) and indice < len(frase)-1):
    if (frase[indice] == letra):
        letraEncontrada = not(letraEncontrada)
        print(f"letra encontrada en el indice  {indice}")
    else:
        indice +=1

        
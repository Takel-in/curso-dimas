# Del capítulo anterior.
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

#Capitulo 6  Bules -> Break, continue, pass
#break. Rompe el bucle, va a la primera instrucción después del bucle.
frase = "En este momento estoy buscando la letra a"
letra ="y" #letra a encontrar.
indice = 0
for caracter in frase:
    if (caracter == letra):
        print(f"letra {letra} encontrada en el indice  {frase.index(caracter)}")  #En el fondo con frase.index(caracter) ya tendríamos el resultado de todo sin falta del for.
        print(caracter)
        break
    else:
        pass
    print(caracter)


#Continue. Va a la siguiente iteracción obviando todo lo domas.
frase = "En este momento busco todas las letras a"
letra = "a"
cnt = 0

for caracter in frase:
    if (caracter == letra):
        cnt +=1
        print (f"Letra {letra} encontrada {cnt} veces")
        continue
        print("Aqui nunca debería llegar")
    print(f"no he encontrado {caracter}")

#Pass No hace nada.  Sigue tan campante donde le toque.
lista = [0, 10, 20, 43]

for pepito in lista:
    if (pepito == 10):
        pass
    print (f"El valor de jose es: {pepito}")

# por ejemplo si quiero definir una función y luego ya la rellenaré pongo pass
def funcion(arg1, arg2):
    pass


#else
frase = "Todos los caracteeres de una frase los contamos"
count = 0
for caracter in frase:
    count +=1
    if (caracter == "l"):
        break
else: # Cuando se ejecuta todas las intereaciones ejecutas al sugiente intrucción siempre no se haya ejecutado un break
    print (f"la frase contiene {count} caracteres")



""" Ejerdcicio: El usuario debe adivinar un número entre 0 y 10.
    El programa deberá pedir que el usuario introduzca un número
    y debe decir si ha acertado, si el número a adivinar es menor
    o mayor que el que ha introducido """


acertado = False
valor = 5
while (not(acertado)):
    numero = input ("Introduce un número entre 0 y 10 o 99 para salir")
    if not(numero.isnumeric()):
        print (f"{numero} No es un valor válido")
        continue
    numero = int (numero)
    if (numero == 99):
        print("Adios")
        break
    if (numero < 0 or numero > 10):
        print (f"{numero} no es un valor entre 0 y 10")
    elif (numero < valor):
        print (f"{numero} es menor que el buscado")   
    elif (numero > valor):
        print (f"{numero} es mayor que el buscado")
    elif (numero == valor):
        print (f"Numero encontrado")
        acertado = True
    else:
        print (f"Nunca debería a ver llegado aquí.")
        break


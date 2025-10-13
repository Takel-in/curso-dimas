# Capitulo 7  Listas

# Repaso conceptos básicos
numeros = [1, 2, 3, 4, 5]  #En python podemos mezclar disintos tipos de datos en la misma lista.
print (numeros) #imprime la lista completa. [1, 2, 3, 4, 5]
primeraPosición = numeros[0] # En python el indice empieza desde 0. el primer valor es 1,
longitud = len(numeros) # Número de elementos en la lísta. la longitud es 5
print(f"el primer valor es {primeraPosición}, \nla longitud es {longitud}") # el primer valor es 1, la longitud es 5

for num in numeros:
    print (num)

# Indexado y subblistas  #acceder a elementos individuales o varios a la vez de la lista.
#indice+   0       1      2      3         4
#indice-  -5      -4     -3     -2        -1
lista = ["dale", "un", "buen", "like", "crack"]
print (lista)  #['dale', 'un', 'buen', 'like', 'crack']

    # Uso de indices negativos.
ultimaPosicion = lista[-1] # Si hacemos en valores negativo empieza desde el último elemento.
print (ultimaPosicion) #crack
penultimo = lista[-2]
print (penultimo) # like

    # Uso de varios elementos a la vez. se indica el límite inferior y superior !!! CUIDADO ¡¡¡¡. El superior siempre coge el anterior 
sublita = lista[1:4] # Recordar el límite superior siempre hay que indicar hasta el elemento + 1 del que queremos realmente ya que el útlimo no lo usa.
print (sublita) #['un', 'buen', 'like']
sublita = lista[:4] # va del primer elemento (indice 0) hasta el elemento 4-1  
print (sublita)  #['dale', 'un', 'buen', 'like']
sublita = lista[2:] # va desde el 3 elemento (recordar que empezamos desde 0 ) hasta el final de la lista.
print(sublita) #['buen', 'like', 'crack']
sublita = lista[-4:-1] # Si usamos indices negativos.
print (sublita) #['un', 'buen', 'like']. Recordar eque el de arriba llega solo hasta el elemento anterior.
sublita = lista[-4:] # Si usamos indices negativos.
print (sublita) #['un', 'buen', 'like', 'crack']. Va desde la posición -4 hasta el final de la lista.
sublita = lista[:-1] # Si usamos indices negativos.
print (sublita) #['dale', 'un', 'buen', 'like']. Recordar eque el de arriba llega solo hasta el elemento anterior.

# Comprobar si una lista contiene o no un elemento.
#indice+   0       1      2      3         4
#indice-  -5      -4     -3     -2        -1
lista = ["dale", "un", "buen", "like", "crack"]
palabra1 = "like"
palabra2 = "melocotón"

if palabra1 in lista: #Mira si un elemento está contenido en la lista.
    print (f"La palabra {palabra1} pertenece a la lista")

if palabra2 not in lista: # pregunto si una palabra no está en la lista.
    print (f"la palabra {palabra2} no está en la lista.")

# Modificar elementos en una lista
lengaujes = ['C', "java", "python", "JavaScript", "Kotlin"]
print(lengaujes) # ['C', 'java', 'python', 'JavaScript', 'Kotlin']
lengaujes[1] = "Angular"
print(lengaujes) # ['C', 'Angular', 'python', 'JavaScript', 'Kotlin']
lengaujes[0] = lengaujes[0] + "++"
print(lengaujes) #['C++', 'Angular', 'python', 'JavaScript', 'Kotlin']

    # Remplazar varios elementos a la vez.
lengaujes[2:4] = ["Anaconda", "TypeScript"] # posición 2 y 4 son python y JavaScript
print(lengaujes) #['C++', 'Angular', 'Anaconda', 'TypeScript', 'Kotlin']

    # Si introducimos varios valores que superan el número de elementos a suprimir, lo que hace es añadirlos a continuación del que si puede añadir y luego coloca el resto de valores que tenía en la lista.
lengaujes[2:3] = ["Varios", "Valores", "botella"] # posición 4 es Ktlin
print(lengaujes) #['C++', 'Angular', 'Varios', 'Valores', 'botella', 'TypeScript', 'Kotlin']  //Como no hay posiciones 



"""# Métodos de la listas: Añadir elementos.
   En python podemos utilizar métodos con las listas.
   Para ejecutar estos métodos: variableDeTipoLista.metodo()"""
#Añadir elementos.  
lenguajes = ['C', "java", "python", "JavaScript", "Kotlin", "Ruby", "Rust"]
    #En una posición indicada
lenguajes.insert(1, "c++") #Añade un elemento en la posición que hems indicado sin eliminar el elemento que exista en esa posición.
print (lenguajes) #['C', 'c++', 'java', 'python', 'JavaScript', 'Kotlin', 'Ruby', 'Rust']
    #Allfinal de la lista.
lenguajes.append("TypeScript") #Añade un elemento al final de la lsita
print (lenguajes) #['C', 'c++', 'java', 'python', 'JavaScript', 'Kotlin', 'Ruby', 'Rust', 'TypeScript']

    # Unir varias listas.
lenguajes2= ["Angular", "Vue", "React"] 
lenguajes.extend(lenguajes2) #Lenguajes2 no se ve afectado.
print(lenguajes) #['C', 'c++', 'java', 'python', 'JavaScript', 'Kotlin', 'Ruby', 'Rust', 'TypeScript', 'Angular', 'Vue', 'React']
print(lenguajes2) # ['Angular', 'Vue', 'React']

lenguajes2.extend(lenguajes)
print (lenguajes2) # ['Angular', 'Vue', 'React', 'C', 'c++', 'java', 'python', 'JavaScript', 'Kotlin', 'Ruby', 'Rust', 'TypeScript', 'Angular', 'Vue', 'React']

#Métodos de las listas: Elminar elementos 
frutas = ["plátano","kiwi","papaya","melocotón","cereza"]
print (frutas) # ['plátano', 'kiwi', 'papaya', 'melocotón', 'cereza']

    # El último elemento
frutas.pop()
print (frutas) # ['plátano', 'kiwi', 'papaya', 'melocotón']

    # Un determinado elemento
valoreliminar = frutas.pop(0)
print (frutas) # ['kiwi', 'papaya', 'melocotón']
print (valoreliminar) #plátano

    # Eliminar un elemento por el valor 
frutas.remove("kiwi")
print (frutas) # ['papaya', 'melocotón']

#frutas.remove ("jajaj") #ERR
#frutas.pop(33) #ERR

    # otra forma de eliminar un elemento, pero creo que esta vez no retorna el elemento eliminado.
del frutas[0]
print (frutas) # ['melocotón']

    # devuelve la posición donde se encuentra un valor
indice = frutas.index("melocotón")
print (indice) #0


# Ejercicios
""" Tenemos un texto donde queremos encontrar palabras clave.
Las palabras clave pueden ser hasta 5 y deberemos pedirselas al usuario 
y guardarlas en una lista.

Si el usuario quiere poner menos de 5 palabras clave, deberá escribir "fin"
para terminar de introducir datos. Si el usuario introduce números o nada, 
debermos eliminarlos de la lista antes de la búsqueda.

En otra lista, debermos guardar el número de veces que aparece da palabra
clave en nuestro texto. Por ejemplo, si la palabras claves son  ordenador y 
portátil y aparecen 5 y 7 veces respectivamente, nuestra línes deberín ser 
así:
    - keyword = ["ordenador", "portatil"]
    - ocurrencias = [5, 7]
    
Pista: Podemos pasar de una cadena de texto a una lista de palabras mediante el método texto.split(). 
Por ejemplo: 

texto = "hola que tal"
print (texto.split())
Texto = ['hola', 'que', 'tal']

    """

texto = """Seguramente hayas notado que tu productividad ha bajado desde que trabajas desde casa. 
Es muy importante que logremos teletrabajar efectivamente y de manera autorregulada.
Esto se traduce en finalizar antes nuestras tareas y evitar jornadas laborales interminables.
El primer consejo y uno de los más importantes ya te lo he dado en el apartado anterior.
Tenemos que construir un espacio de trabajo en el que nos sintamos cómodos y dispongamos de todas las herramientas neecesarias para teletrabajar.
En la medida de los posible, es importante teletrabajar siempre en el mismo lugar.
De esta forma, nuestro cerebro asocia el sitio con la acción de trabajar y nos hará estar más focalizados en nuestras tareas."""

# Resolución.

""" 
Si el usuario quiere poner menos de 5 palabras clave, deberá escribir "fin"
para terminar de introducir datos. 
Si el usuario introduce números o nada, debermos eliminarlos de la lista antes de la búsqueda.
"""

palabrasClaves = [] #Almacenamos palabra claves
cnt = 0 #Contado de iteracciones 

# Mientras no tengamos 5 palabra claves.
while cnt < 5:
    palabra = input("Introduce una palabra clave a buscar: ")

    # Si deseamos acabar antes de tener las 5 palabras.
    if (palabra == "fin"):
        break

    # Añadimos la palabra a la lista.
    palabrasClaves.append(palabra)
    cnt +=1 # Aumentamos el contador de iteracciones.

# Eliminar aquellos elementos de la lista que son número o "".
# Recordar que cuando queremor ir desde el último elemento siemproe lo ferenciamos como n-1 hasta el elemento -1 que el limite superior siempre es uno inferior al elemento que queremos ir -1 es el salto.
for index in range(len(palabrasClaves)-1, -1, -1):
    if (palabrasClaves[index] == "" or palabrasClaves[index].isnumeric() ):
        palabrasClaves.pop(index)        
    
"""  LA FORMA EN QUE LO HACE EL.
posición = 0
while (if poaisicón < (keywords))   #Comprobar si en vez de < es <=
    if (keyword[posicion] == '' or keyword[posicion].isnumeric()):
        keyword.pop(posición)
    else
        posición +=1
"""    


# Preparamos la siguiente parte del ejercicio.
palabrasABuscar = texto.split()
coincidencias = [] #Lista que contiene el número de veces que aparecen los elementos en el texto.



# Buscamos una palabra dentro del texto clave.
for palabra in palabrasClaves:
    cnt = 0
    for palabraABuscar in palabrasABuscar:
        if palabra == palabraABuscar:
            cnt +=1          # El cambia un poco y lo que hace es en palabras clave poner .index(palabra clave) que ya sabemos que existe.
    coincidencias.append(cnt)

# Se imprime los resultados.
cnt = 0
for valor in palabrasClaves:
    print (f"El valor {palabrasClaves[cnt]} se reipte {coincidencias[cnt]} veces.\n")
    cnt +=1

print (palabrasClaves)
# Capítulo 9 Métodos de Cadena
# Find, index y count

# Los métodos find e index sirven para encontrar conjunto de caracteres de un string
# Ej. (una palabra dentro de una frase)


mail = "correo@dominio.com"

#Quiero comprobar si mail tiene un @
posicion = mail.index('@') 
print (posicion) #6

posicion = mail.find('@')
print (posicion) #6

posicion = mail.find('dominio')
print (posicion) # 7

posicion = mail.find('*')
print (posicion) # -1

# posicion = mail.index('*') 
# print (posicion) # Da excepción.

# La diferencia entre index y finid es que index si no lo encuentra da exeption y find devuelve -1

# count devuelve la cantidad de veces que encuentra una substring o caracter en el texto buscado.
apariciones = mail.count('r')
print (f"La letra r apare {apariciones} veces") # La letra r apare 2 veces


# Metodos split, replace y join

# El método split sirve para dividir un string medianto un delimitador y convertir ada división en un elemento de la lista.
compra = "chocolate, pan, agua, platano, pipas, veduras"
listaCompra = compra.split(", ") #El delimitador se lo come, es decir quita la coma y el espacio.
print (listaCompra) # ['chocolate', 'pan', 'agua', 'platano', 'pipas', 'veduras ']

compra2 = "chocolate pan agua platano pipas veduras"
listaCompra2 = compra2.split() # Si no se pasa ningún argumento separa por espacios. 
print (listaCompra2) # ['chocolate', 'pan', 'agua', 'platano', 'pipas', 'veduras']

print(f"En la lista de la compra hay: {len(listaCompra)} productos") #En la lista de la compra hay: 6 productos

# El método replace sirve apra reemplazar un substring por otro.
compra = "chocolate, pan, agua, platano, pipas, veduras"
reemplazado = compra.replace(', ', ' - ')
print (reemplazado) # chocolate - pan - agua - platano - pipas - veduras


# El método join sirve para unir una lista de string enun único string mediante un caracter determinado.
compra = ", ".join(listaCompra)  #Esto ya lo habíamos separado y ahora lo volvemos a unir
print (compra) # chocolate, pan, agua, platano, pipas, veduras

"""
Ejerciio. Tenemos unas descripciones de algunos productos. En ellas se incluye el precio de cada producto.
Debemos encontrar el precio en € y mostrarlo en Pantalla. El precio puede Tener: 0,1 o 2 decimales y siempre
va seguido del símbolo '€'. Por ejemplo:
   - 9.99€
   - 10€
   - 10.5€

Bonus: Debemos modiicar las descripciones para eu el precio se muestre en dólares. La conversión es: 1€ = 1.21$. 
No hace falta modificar la variable original de la decripción, podemos retornar una copia en el precio convertido.

"""
des1 = "Este bolso de cuero de la marca: Miguel cors tiene un precio de 199.99€. Es una oferta especial."
des2 = "Las botas de la marca: Nque Valen 89€. Nunca han estado tan rebajadas."
des3 = "¡Tenemos el bambú en oferta! Cómpralo ahora por 1.2€ el kg ¡No lo dejes pasar!"

def encontrarCantidad(texto):

    # Localizo el caracter deseado que es un €
    posEuro = texto.find('€')
    if posEuro == -1:
        return -1 #Devolvemos un error.
    
    # Desde la posición hacia atras hasta que encontremos el primer espacio
    posEspacio = posEuro - 1
    while (posEspacio >=0 and texto[posEspacio] != ' '):
        posEspacio -=1

    # devolvemos lo que hayamos encontrado.
    return texto[posEspacio+1:posEuro+1]

def remplazarAdolares(texto):
    # Recogemos el valor.
    valor = encontrarCantidad(texto)

    #Si lo encuentra
    if valor == -1:
        return -1
    
    # Hacemos la conversión de moneda.
    aux = valor.replace('€','')
    aux = float(aux)
    aux = aux * 1.21
    aux = str(aux) + '$'

    return texto.replace(valor, aux)
    

print (encontrarCantidad(des1)) #199.99€
print (encontrarCantidad(des2)) #89€
print (encontrarCantidad(des3)) #1.2€

print (remplazarAdolares(des1)) #Este bolso de cuero de la marca: Miguel cors tiene un precio de 241.9879$. Es una oferta especial.
print (remplazarAdolares(des2)) #Las botas de la marca: Nque Valen 107.69$. Nunca han estado tan rebajadas.
print (remplazarAdolares(des3)) #¡Tenemos el bambú en oferta! Cómpralo ahora por 1.452$ el kg ¡No lo dejes pasar!


# Otros métodos útiles para manitular strings.
Texto = "Esto es un texto de ejemplo"
print ("Metrodo startWith:")
print (Texto.startswith('Esto'))  #True -> Poque es cierto que la frase comienza conesa palabra.
print (Texto.startswith('esto'))  #False
print ("Metrodo upper:") # Convierte todo a mayúsculas
print (Texto.upper())  # ESTO ES UN TEXTO DE EJEMPLO
print ("Metrodo Title:") # Convierte la primera letra de cada palabra y la pone en mayúsculas
print (Texto.title()) # Esto Es Un Texto De Ejemplo
print ("Metrodo Capitalize:") # Convierte la primera letra de trodo el string y la pone en mayúsculas.
print (Texto.capitalize()) # Esto es un texto de ejemplo
print ("Metrodo rjust:") # Alineación de caracteres e indica los caracteres en blanco que tiene que poner al inicio.
print (Texto.rjust(len(Texto)+8)) #Esto es un texto de ejemplo
print ("Metrodo rjust:") # Alineación de caracteres e indica los caracteres en blanco que tiene que poner al inicio.
print (Texto.rjust(len(Texto)+8, '*')) # ********Esto es un texto de ejemplo



""" Formatear  texto. 
    Debemos formatear el siguiente texto
    Normas.
    - '#' a princiio de línea signifca que es un título y debemos convertirlo todo a mayúsculas.
    - '##' a rpincpio de línea significa ue es un subtítulo y debemosponer la primera letra de cada palabra en mayúsculas.
    - '###' deberemos poner únicamente la primera letra en mayúsculas.
    - si la línea empieza con '-' debermos añadir una sangría.

    NOTA: El método splitlines() retorna una lsita de srings, Seprada mediante saltos de línea.
    Las almuadillas hay que eliminarlas y los guiones mantenerlos.
"""
Texto = """
#este es el título principal

- Esto es una lista.
- De cosas que podemos hacer.

##este es un subtítulo

Esto es una pequeña introducción.
- Esto es otra lista.
- De más cosas que podemos hacer.
"""

def trabajarTexto( texto ):
    # Dividimos las líneas
    lineas = texto.splitlines()
    restexto = ""
    # Por cada líena.
    for linea in lineas:

        # Si la líena comienza con ### entonces Capital
        if (linea.startswith('###') == True ):
            linea = linea.capitalize()
            restexto = restexto + linea[3:] + '\n' 
        elif linea.startswith('##') == True : #Si la línea comienza con ## entonces título.
            linea = linea.title()
            restexto = restexto + linea[2:] + '\n' 
        elif linea.startswith('#') == True :      #Sino, sila línea comienza con # encontes todo mayúsclas
            linea = linea.upper()
            restexto = restexto + linea[1:] + '\n' 
        elif linea.startswith('-') == True :         #Sino, si la línea empieza con '-' sangría.
            linea = linea.rjust(len(linea) + 5,' ')
            restexto = restexto + linea + '\n' 
        else:
            # Volcamos el resto de las lienas tal y como se encuentre.
            restexto = restexto + linea + '\n' 
    
    # Devolvemos el texto
    return restexto

print(trabajarTexto(Texto)) #Imprime todo lo que hay abajo.
#
#ESTE ES EL TÍTULO PRINCIPAL
#
#     - Esto es una lista.
#     - De cosas que podemos hacer.
#
#Este Es Un Subtítulo
#
#Esto es una pequeña introducción.
#     - Esto es otra lista.
#     - De más cosas que podemos hacer.


"""Esto es como lo hace él."""

def formatText(Texto):
    listaTexto = Texto.splitlines()
    for indx in range(len(listaTexto)):
        if (listaTexto[indx].startswith('###')):
            listaTexto[indx] = listaTexto[indx].replace('###','')
            listaTexto[indx] = listaTexto[indx].capitalize()
        elif (listaTexto[indx].startswith('##') ):
            listaTexto[indx] = listaTexto[indx].replace('##','')
            listaTexto[indx] = listaTexto[indx].title()
        elif (listaTexto[indx].startswith('#') ):
            listaTexto[indx] = listaTexto[indx].replace('#','')
            listaTexto[indx] = listaTexto[indx].upper()
        elif (listaTexto[indx].startswith('-') ):
            listaTexto[indx] = listaTexto[indx].rjust(len(listaTexto[indx])+8)
            
    return  '\n'.join(listaTexto)

print(formatText(Texto))
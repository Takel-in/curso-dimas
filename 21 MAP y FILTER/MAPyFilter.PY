# Funciones MAP y FILTER
"""
    Son funciones que sirven para trabajar con objetos iterables .
    Vienen incoporadas por defecto en python.

    Ej.  objetos iterables ->  listas, tuplas, string....
    """

    #1 Funcion filter.
    #Filter (function, iterable). Devuelve un iterador con los valores
    #del iterable que cumplan la función.

emails = ['juan@hotmail.es', 'javier@gmail.com', 'mandarinas', 'wikipedia.com' ]

emailsValidos =  []
#Forma 1 A la antigua usanza.
for email in emails:
    if '@' in email:
        print (f"El email {email} es válido")
        emailsValidos.append (email)
    else:
        print (f"El email {email} es inválido")

# Al ejecutar 
# El email juan@hotmail.es es válido
# El email javier@gmail.com es válido
# El email mandarinas es inválido
# El email wikipedia.com es inválido

print (emailsValidos) # ['juan@hotmail.es', 'javier@gmail.com']

#Forma 2 con filters
def evaluarEmail(email): # Creamos la función de evaluación.
    if '@' in email:
        return True
    else:
        return False 

#Uso de la función filter para comprbar emails válidos de una lista.
emailsValidos = filter( evaluarEmail, emails) #Coge la lista emails y lo val pasando elemento por elemento a la función de evaluación.
print(emailsValidos) #Si hacemos esto al imprimir nos muestra -> <filter object at 0x00000210C267C670>

# emailsValidos Ahora sería un objeto iterador.
print (next(emailsValidos)) #Devuelve el primer valor #juan@hotmail.es
print (next(emailsValidos)) #Devuelve el siguiente  valor  #javier@gmail.com
#print (next(emailsValidos)) #Devuelve Exception StopIteration ya que ha mostrado todos los elementos 

# Lo que podemos hacer es convertillo en lista una vez que se llama al filter.
emailsValidos = list(filter( evaluarEmail, emails)) 
print(emailsValidos) #['juan@hotmail.es', 'javier@gmail.com']

# Podíamos haber definido la función de evaluación 
def evaluarEmail(email): 
     return '@' in email #Si contiene devolver true y no contiene devolverá false.

emailsValidos = list(filter( evaluarEmail, emails)) 
print(emailsValidos) #['juan@hotmail.es', 'javier@gmail.com']

# Como la función evaluarEmail se una línea la podriamso haber definido como una función LAMBDA.
emailsValidos = list(filter( lambda email : '@' in email , emails)) 
print(emailsValidos) #['juan@hotmail.es', 'javier@gmail.com']


# 2 Funcion MAP
#   map(funcion, iterable),   Aqui no evaluo una función simplemente se la paso a la función. 
#   ejecuta la función pasando parámetro cada elemento del iterable.
#
palabras = ('dale', 'un', 'buen', 'like', 'y', 'suscríbete')

#Usando map quiero sable la longitud de cada palabra de la tupla.
longitudes = list(map(lambda palabra: len(palabra), palabras)) #Aqui no se devuelve un valor booleano, sino el valor que se sea. 
print(longitudes) # [4, 2, 4, 4, 1, 10]

# Vamos a hacer un ejemplo y necesitamos math
# Vamos a calcular a partir de un eje x los valores de una función matemática.
import math 

eje_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
eje_xs = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
eje_y = list(map(lambda x, y : round(math.cos(x) + math.exp(y), 3), eje_x, eje_x)) #Sumamos el coseno de x a la exponencia de y. Al resultado lo redondeamos con 3 decimales de precisión. 
                                                                                    #en map paso dos iterable uno para x y otro para Y. 
print (eje_y) #[2.0, 3.259, 6.973, 19.096, 53.945, 148.697, 404.389, 1097.387, 2980.812, 8102.173]                                                                                   







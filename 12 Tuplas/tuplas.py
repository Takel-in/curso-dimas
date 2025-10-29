#Capitulo 11  Tuplas

#Las tuplas son conjunto ordenados de datos que no se pueden modificar.
# la tuplas no se pueden modifica, añadir, eliminar.......
# Aqui también se pueden mezclar tipos de datos.
mitupla = ("Babunny", "Anuel", "Daddy Yankee", "Algun capuyo") 
print (mitupla) # ('Babunny', 'Anuel', 'Daddy Yankee', 'Algun capuyo')
print (f"la longitud de la tipla es {len(mitupla)}") # la longitud de la tipla es 4

for cantante in mitupla:
    print (f"Cantente {mitupla.index(cantante)} es {cantante}") #Cantente 0 es Babunny
                                                                #Cantente 1 es Anuel
                                                                #Cantente 2 es Daddy Yankee
                                                                #Cantente 3 es Algun capuyo


# Indexado de tuplas.
# Se pueden indexar los elementos de una tupla de la misma forma que las listas.
mitupla = ("Babunny", "Anuel", "Daddy Yankee", "Algun capuyo") 
print (mitupla[0]) #Babunny
print (mitupla[-1]) #Algun capuyo
subtupla = mitupla[1:3] #Recordar que nunca llega a la última posición.
print (subtupla) # ('Anuel', 'Daddy Yankee')


# Modificar tuplas.
# No se puede modificar una dupla directamente. Veremos que érroees ocurren y como transformas una tupla a
# una lista y viceversa.
mitupla = ("Babunny", "Anuel", "Daddy Yankee", "Algun capuyo") 

#del mitupla[1] # Genera excepción.
#mitupla.append ("Elemento nuevo") #No existe este método.
#mitupla[2] = "Dom Omar" #Excepción 

milista = list(mitupla) #Convierte una tupla en lista.
print (milista) #['Babunny', 'Anuel', 'Daddy Yankee', 'Algun capuyo']
print (type(milista)) #<class 'list'>

milista.append("Don Omar")
print (milista) # ['Babunny', 'Anuel', 'Daddy Yankee', 'Algun capuyo', 'Don Omar']

mitupla = tuple(milista) 
print (mitupla) #('Babunny', 'Anuel', 'Daddy Yankee', 'Algun capuyo', 'Don Omar')
print ( type (mitupla)) #<class 'tuple'>


# Empaquetar y desempaquetar tuplas. 
# De la misma forma que podemos agrupar mutiples variables en una tupla (empaquetar), también podemos 
#asignar cada elemento de una tupla a una variable distinta.

mitupla = ("Babunny", "Anuel", "Daddy Yankee", "Algun capuyo")  # Esto es empaquetar.

artista1 = "cTangana"
artista2 = "duki"
nuevaTupla = (artista1, artista2) # ESto es empaquetar.
print (nuevaTupla) #('cTangana', 'duki')

(cantante1, cantante2, cantante3, cantante4) = mitupla #Esto es DESEMPATECAR
print(f"{cantante1} {cantante2} {cantante3}") #Babunny Anuel Daddy Yankee

(cantante1, *cantantevarios) = mitupla #esto también es DESEMPAQUETAR. El primer valor lo asigna a un valor y el resto a una lista.
print (cantante1) #Babunny
print (cantantevarios) #['Anuel', 'Daddy Yankee', 'Algun capuyo']


mitupla2 = mitupla + nuevaTupla #Con esto creo una nueva tupla con valors de otras tuplas.
print (mitupla2) #('Babunny', 'Anuel', 'Daddy Yankee', 'Algun capuyo', 'cTangana', 'duki')
(primercantante, *varios, ultimocantante) = mitupla2 #Puedo hacer un DESEMPAQUE así.
print (primercantante) #Babunny
print (varios) #['Anuel', 'Daddy Yankee', 'Algun capuyo', 'cTangana']
print (ultimocantante) #duki


#Extra -- Listas de tuplas.
# Podemos crear listas cuyos elementos sean tuplas. De esta forma, podemos iterar sobre las diversas tuplas
# y además desempaquetar sus elementos.

comida = [("primer","macarrones"), ("segundo","pollo"), ("postre","flan")]    
print ("El menu de hoy es:")#El menu de hoy es:

for numer, plato in comida:
    print (f"{nuevaTupla} -> {plato}")  #('cTangana', 'duki') -> macarrones
                                        #('cTangana', 'duki') -> pollo
                                        #('cTangana', 'duki') -> flan

#Como se hizo conlos dicciónarios.
artistas = {1: "C.Tangana", 2:"Duki"}
print (artistas) #{1: 'C.Tangana', 2: 'Duki'}
elementos = artistas.items()
print (elementos) #dict_items([(1, 'C.Tangana'), (2, 'Duki')])
for clave, valor in elementos:
    print (f"{clave} -> {valor}")
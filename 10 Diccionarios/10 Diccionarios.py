# Capitulo 10: Diccionarios
# Conceptos básicos.

# Declaración de diccionarios.
# Los diccioanrios son conjuntos de elementos con la estructura clave: valor.
# Cada elemento de un diccionario contiene una clave y un valor asociado a esta.
# Las Claves pueden ser de tipo String o int. Los valores pueden ser cualquier tipo de datos.

miDiccionario = {"nombre" : "alejandro"} #Diccionario de 1 elemento.
alejandro = {"nombre" : "alejandro", "edad": 32, "ciudad" : "Barcelona", "afficiones" : ["lectura", "cine", "videojuegos"] } #Diccionario de varios elementos.
print (alejandro) # {'nombre': 'alejandro', 'edad': 32, 'ciudad': 'Barcelona', 'afficiones': ['lectura', 'cine', 'videojuegos']}

ana = {"nombre":"ana", "Edad":32, "Affciones":["pesca", "natacion", "escritura", "cantar"]}
print (ana) #{'nombre': 'ana', 'Edad': 32, 'Affciones': ['pesca', 'natacion', 'escritura', 'cantar']}

    #Diccionario de diccionarios.
trabajadores = {0:alejandro, 1:ana}
print (trabajadores) # {0: {'nombre': 'alejandro', 'edad': 32, 'ciudad': 'Barcelona', 'afficiones': ['lectura', 'cine', 'videojuegos']}, 1: {'nombre': 'ana', 'Edad': 32, 'Affciones': ['pesca', 'natacion', 'escritura', 'cantar']}}

    # La longitud es el número de pares clave:valor tiene.
print (f"Longitud diccionar alejandro: {len(alejandro)}") #Longitud diccionar alejandro: 4
print (f"Longitud diccionar trabajadores: {len(trabajadores)}") # Longitud diccionar trabajadores: 2

    # No pueden existir claves duplicadas.  Si se duplica coje el último valor.
a = {"año" : 1990, "año": 2003} 
print (a) # {'año': 2003}
print (f"Longitud diccionar alejandro: {len(a)}")  # El diccionario solo tendrá 1 elemento ya que esta repetido la clave. 

# Añadir, eliminar y modificar elementos de un diccionario.
alejandro = {"nombre" : "alejandro", "edad": 32, "ciudad" : "Barcelona", "afficiones" : ["lectura", "cine", "videojuegos"] } #Diccionario de varios elementos.
print (alejandro) # {'nombre': 'alejandro', 'edad': 32, 'ciudad': 'Barcelona', 'afficiones': ['lectura', 'cine', 'videojuegos']}

    # Añadir un clave valor.
alejandro["cargo"] = "CEO"
print(alejandro) # {'nombre': 'alejandro', 'edad': 32, 'ciudad': 'Barcelona', 'afficiones': ['lectura', 'cine', 'videojuegos'], 'cargo': 'CEO'}

alejandro.update({"sueldo" : 90000})
print(alejandro) # {'nombre': 'alejandro', 'edad': 32, 'ciudad': 'Barcelona', 'afficiones': ['lectura', 'cine', 'videojuegos'], 'cargo': 'CEO', 'sueldo': 90000}

alejandro.update({"Vacaciones" : "muchas", "Otro elemento": "otro"})
print(alejandro) # {'nombre': 'alejandro', 'edad': 32, 'ciudad': 'Barcelona', 'afficiones': ['lectura', 'cine', 'videojuegos'], 'cargo': 'CEO', 'sueldo': 90000, 'Vacaciones': 'muchas', 'Otro elemento': 'otro'}

    #  Eliminar un elemento.
del alejandro["Vacaciones"]
print(alejandro) # {'nombre': 'alejandro', 'edad': 32, 'ciudad': 'Barcelona', 'afficiones': ['lectura', 'cine', 'videojuegos'], 'cargo': 'CEO', 'sueldo': 90000, 'Otro elemento': 'otro'}

valor = alejandro.pop("cargo")
print (alejandro) #{'nombre': 'alejandro', 'edad': 32, 'ciudad': 'Barcelona', 'afficiones': ['lectura', 'cine', 'videojuegos'], 'sueldo': 90000, 'Otro elemento': 'otro'}
print (f"valor eliminado {valor}") # valor eliminado CEO

    # Acceso elemento de un diccionario.
edad = alejandro["edad"]
print (f"la edad de alejandro: {edad}") #la edad de alejandro: 32

    # Actualizar el valor de un diccionario.
alejandro["edad"] = 33
alejandro.update({"ciudad":"Zaragoza"}) # {'nombre': 'alejandro', 'edad': 33, 'ciudad': 'Zaragoza', 'afficiones': ['lectura', 'cine', 'videojuegos'], 'sueldo': 90000, 'Otro elemento': 'otro'}
print (alejandro)

# Listas de claves y valores.
# Podemos obtener una lista tanto de las claves como de los valores que conforman un diccionario




"""
Ejercicio
Buscador de productos: Tenemos varios productos, el usuario mediante el nombre de un producto 
puede consultar su precio y sus unidades en stock
"""
producto1 = {"Nombre" : "Producto 1", "Precio" : 100, "Stock" : 10}
producto2 = {"Nombre" : "Producto 2", "Precio" : 200, "Stock" : 20}
producto3 = {"Nombre" : "Producto 3", "Precio" : 300, "Stock" : 30}
producto4 = {"Nombre" : "Producto 4", "Precio" : 400, "Stock" : 40}


# Puedo generar una lista con los diccionarios sueltos, en vez de hacer un diccionario  de diccionarios.
almacen = [producto1, producto2, producto3, producto4]

# Busca la información de un producto.
def infoProducto (nombreProducto):
    
    # Buscamos el producto entre todos los productos de la lista.
    for producto in almacen:

        #Si cooincide.
        if (producto["Nombre"] == nombreProducto):
            print(f"El producto {nombreProducto} tiene un precio de {producto["Precio"]} y tiene un stock de {producto["Stock"]}")
            break
    else: #Se ejecuta solo si ha terminado todo el bucle sin ejecutar el break.
        print(f"No se ha encontrado el producto {nombreProducto}.")

# Preguntamos el producto que deseamos.
val = input ("Introduce el nombre del producto -> ")

#Busamos el producto y mostrams algunos datos.
infoProducto (val)



#Iterar sobre claves y valors.
alejandro = {"nombre" : "alejandro", "edad": 32, "ciudad" : "Barcelona", "afficiones" : ["lectura", "cine", "videojuegos"] } #Diccionario de varios elementos.

    #Forma de hacerlo 1.
# keys devuelve las claves del diccionario y values los valores.
# La función ZIP va devolviendo valor de Keys y values. Además está función en caso que las listas tuvieran 
#    una longitud distinta pararía el bucle al acabar la más corta.
for clave, valor in zip(alejandro.keys(), alejandro.values()):
    print (f"{clave} -> {valor}") #nombre -> alejandro
                                  #edad -> 32
                                  #ciudad -> Barcelona
                                  #afficiones -> ['lectura', 'cine', 'videojuegos']


    #Forma de hacerlo 2.
# usando items()
# Hace lo mismo pero lo hace sobre dos valores a la vez. 
for clave, valor in alejandro.items():
    print (f"{clave} == {valor}") #nombre == alejandro
                                  #edad == 32
                                  #ciudad == Barcelona
                                  #afficiones == ['lectura', 'cine', 'videojuegos']
                                  
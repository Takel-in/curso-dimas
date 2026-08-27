# Archivos externos
# Por defecto, el modo de abrir un fichero es lectura como texto. Por tanto para
# leer su contenido no es necesario especificar el segundo argumento.

import os

print(os.getcwd()) #C:\Users\frjoma\python-learning\curso-dimas

fichero1 = open('./23 Archivos externos/prueba.txt', 'rt', encoding='utf-8') #utf-8 es para poder añadir ñ acentos......

# r -> read  Lo abre en solo lectura.
# w -> write  si existe lo sobre escribe, si no existe lo crea
# a -> append  añade contenido al final del fichero.
# x -> create  si no existe lo crea.  

# t -> text-mode  cuando queramos trabajar con ficheros de texto.
# b -> bytes - para archivos como fotos. 

primeralinea = fichero1.readline()
print (primeralinea) # Fichero de prueba para demostrar como trabajar con archivos externos.
                     #                            El salto de línea también lo pone python.
print(fichero1.readline()) #Línea de prueba 2
                        # 
print(fichero1.readline()) #Línea de prueba 3   porque ya no hay un salto de línea no escribe otra línea.



fichero2 = open('./23 Archivos externos/prueba.txt', 'rt', encoding='utf-8') #utf-8 es para poder añadir ñ acentos......
todasLasLineas = fichero2.readlines()   #-> Nos genera una lista con todas las líneas.
print (todasLasLineas) #['Fichero de prueba para demostrar como trabajar con archivos externos.\n', 'Línea de prueba 2\n', 'Línea de prueba 3']


fichero3 = open('./23 Archivos externos/prueba.txt', 'rt', encoding='utf-8') #utf-8 es para poder añadir ñ acentos......
print (fichero3.readline()) # Fichero de prueba para demostrar como trabajar con archivos externos.
                     #                            El salto de línea también lo pone python.
todasLasLineas = fichero3.readlines()
print (todasLasLineas) #['Línea de prueba 2\n', 'Línea de prueba 3']   #Solo genera la lista con el resto de las líenas pendientes.
#
fichero1.close
fichero2.close
fichero3.close


# 2  Escribir en un fichero existente.
# Si un fichero ya tiene contenido hay dos opciones.
# Sborescribir el contenido o a
fichero = open('./23 Archivos externos/prueba.txt', 'w', encoding='utf-8') #utf-8 es para poder añadir ñ acentos......
fichero.write('Me cargo todo lo que había.\n')
fichero.close()


fichero = open('./23 Archivos externos/prueba.txt', 'w', encoding='utf-8') #utf-8 es para poder añadir ñ acentos......
fichero.write('Me cargo todo lo que había.\n')
             # Hay que especificar los saltos de línea para que las cree.
listaContenido = ['Dimas es el pero Youtuber.\n', 'Aunque estoy aprendiendo', 'con su curso de Python.\n', 'Fin de la cita.\n']
fichero.writelines(listaContenido)
fichero.close()


#Si no quiero poner los \n
fichero = open('./23 Archivos externos/prueba.txt', 'w', encoding='utf-8') #utf-8 es para poder añadir ñ acentos......
fichero.write('Me cargo todo lo que había.\n')
             # Hay que especificar los saltos de línea para que las cree.
listaContenido = ['Dimas es el pero Youtuber.', 'Aunque estoy aprendiendo con su curso de Python.', 'Fin de la cita.']
    #NOTA -> No hace falta que le pongamos list porque map ya es un iterador
listaContenido = list(map(lambda line : line +'\n' , listaContenido))
fichero.writelines(listaContenido)
fichero.close()

# 3  Escribir en un fichero existente.
# Si un fichero ya tiene contenido hay dos opciones.
# ... añadir al fichero existente sin eliminar el contenido previo.

#Si no quiero poner los \n
fichero = open('./23 Archivos externos/prueba.txt', 'a', encoding='utf-8') #utf-8 es para poder añadir ñ acentos......
fichero.write('\n\n\nEsto es una nueva línea..\n')
fichero.close()


# 4  Como crear un nuevo fichero.
#    Cuando usamos open en modo create podemos escribir tras crearlo pero no leerlo.
try:
    fichero = open('./23 Archivos externos/prueba2.txt', 'x', encoding='utf-8') #utf-8 es para poder añadir ñ acentos......
    fichero.write('soy nuevo.\n')
    fichero.close()
except FileExistsError:
    print ("no se puede crear porque ya existe.")

#fichero = open('./23 Archivos externos/prueba2.txt', 'x', encoding='utf-8') #utf-8 es para poder añadir ñ acentos......  Da error porque ya existe.
#Por lo tanto hay que hacer.  LO PONGO EN EL ANTERIOR SIMPLEMENTE POR NO DEJARLO EN COMENTARIO.
try:
    fichero = open('./23 Archivos externos/prueba2.txt', 'x', encoding='utf-8') #utf-8 es para poder añadir ñ acentos......
    fichero.write('soy nuevo.\n')
    fichero.close()
except FileExistsError:
    print ("no se puede crear porque ya existe.")


#    Cuando usamos open en modo create podemos escribir tras crearlo pero no leerlo.
try:
    fichero = open('./23 Archivos externos/prueba3.txt', 'x', encoding='utf-8') #utf-8 es para poder añadir ñ acentos......
    fichero.write('soy nuevo.\n')
    print (fichero.readable() ) #Nos indica  si se puede leer. #False
    print (fichero.writable() ) #Nos indica  si se puede escribir..#True
    fichero.close()
except FileExistsError:
    print ("no se puede crear porque ya existe.")


# 5 Metodo SEEK. Podemos controlar la posición desde la cual empezamos a leer.

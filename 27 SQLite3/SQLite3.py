#SQLite3
#Si se instala en el Visual Estudio Code el plugion de SQLITE al pulsar en el código CTRL+Shift+P sale una ventana donde podemos seleccionar SQLite: Open Database
#       esto nos muestra abajo la base de datos.
"""
Base de datos SQL
    Una base de datos puede contenter mutiples tablas
    Cada tabla, guara elementos con un mismo modelo
    Una tabla tiene filas y columnas.
        Las columnas son los campos de los elementos
        Las filas contienen los datos de cada elemento.

    EL CURSOR. (Objeto de python para trabajar las base de datos).
        El cursos selecciona los elementos de una tabla
        contiene los datos seleccionados
        Es el "encargado"de leer o escribir en la tabla.

    Comunicación con la base de datos.

    Python -> Abrir Conexión   -> BBDD
              Generar Petición ->
                  Ejecuta petición
            <- Respuesta
                   Realizar Cambios
            -> Cerrar Conexión ->  

""" 

import sqlite3 as sql

def createDB():
    conn = sql.connect("streamers.db")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE streamers (
           name text,
           followers integer,
           subs integer
        )"""
    )
    conn.commit()
    conn.close()


def insertRow(nombre, follower, subs):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO streamers VALUES ('{nombre}', {follower}, {subs})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def readRow():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def insertRows(streamerList): #INSERTAR Varos elementos
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO streamers VALUES (?, ?, ?)"
    cursor.executemany(instruccion, streamerList)
    conn.commit()
    conn.close()

def readOrdered(field):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers ORDER BY {field}"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)


def readOrderedDesc(field):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers ORDER BY {field} DESC"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def search():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers WHERE name ='AlexElCapo' "
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def search2():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers WHERE name like 'Alex%' "
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def updateFields():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"UPDATE streamers SET followers=12000000 WHERE name like 'Elokas' "
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def deleteRow():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"DELETE FROM streamers WHERE name like 'Auro%' "
    cursor.execute(instruccion)
    conn.commit()
    conn.close()


if __name__ == "__main__":  #Esto es una comprobación que hace cuando ejecutamos este fichero como si fera el principal 
    Aqui pondriamos cosas que solo se ejecuta cuando ejecutamos este fichero como principal.
    createDB()  #Crea el fichero quehemos dicho.
    createTable()
    insertRow("Ibai", 7000000, 25000)
    insertRow("AlexElCapo", 8000000, 10000)
    readRow() #[('Ibai', 7000000, 25000), ('AlexElCapo', 8000000, 10000)]
    streamers = [
       ('Elokas', 10000000, 9500), 
       ('Cristinini', 3000000, 5500),
       ('Auronplay', 8000000, 20000)
               ]
    insertRows(streamers) 
    readRow() #[('Ibai', 7000000, 25000), ('AlexElCapo', 8000000, 10000), ('Elokas', 10000000, 9500), ('Cristinini', 3000000, 5500), ('Auronplay', 8000000, 20000)]
    readOrdered("subs") #[('Cristinini', 3000000, 5500), ('Elokas', 10000000, 9500), ('AlexElCapo', 8000000, 10000), ('Auronplay', 8000000, 20000), ('Ibai', 7000000, 25000)]
    readOrderedDesc("subs") # [('Ibai', 7000000, 25000), ('Auronplay', 8000000, 20000), ('AlexElCapo', 8000000, 10000), ('Elokas', 10000000, 9500), ('Cristinini', 3000000, 5500)]
    search() # [('AlexElCapo', 8000000, 10000)]
    search2() #[('AlexE', 8000000, 10000)]   #LIKE no hace distinción enre mayucuas y minúsculas.
    updateFields()
    deleteRow()
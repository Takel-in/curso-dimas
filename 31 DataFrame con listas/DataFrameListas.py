# Datframe con listas.
import pandas as pd

#Metodos 1 Lista de Listas
columnas = ["marca", "precio", "Disponibilidad"]
cocheA = ["Mercedes", 10e3, True ]
cocheB = ["BMW", 20e3, False]

df = pd.DataFrame([cocheA, cocheB], columns=columnas)
print(df) #      marca   precio  Disponibilidad
          # 0  Mercedes  10000.0            True
          # 1       BMW  20000.0           False

# Metodo 2 usando ZIP.
marcas = [ "audi", "mercedes", "bmw", "mercedes"]          
precio = [20e3, 30e3, 40e3, 25e3]
disponibilidad = [True, False, False, True]

df = pd.DataFrame(zip(marcas, precio, disponibilidad), columns=["marca", "precio", "Disponibilidad"])
print(df)   #      marca   precio  Disponibilidad
            #0      audi  20000.0            True
            #1  mercedes  30000.0           False
            #2       bmw  40000.0           False
            #3  mercedes  25000.0            True

# Si una de las lsitas es más corta se para cuando llegue al último elementno de esa lista.
print (list(zip(marcas, precio, disponibilidad)))  #[('audi', 20000.0, True), ('mercedes', 30000.0, False), ('bmw', 40000.0, False), ('mercedes', 25000.0, True)]          

# 3 usando diccionario.
marcas = [ "audi", "mercedes", "bmw", "mercedes"]          
precio = [20e3, 30e3, 40e3, 25e3]
disponibilidad = [True, False, False, True]

diccionario = {
    "marcas" : marcas,
    "precio" : precio,
    "disponibilidad" : disponibilidad
}

df = pd.DataFrame(diccionario)
print(df)  #      marca   precio  Disponibilidad
            #0      audi  20000.0            True
            #1  mercedes  30000.0           False
            #2       bmw  40000.0           False
            #3  mercedes  25000.0            True


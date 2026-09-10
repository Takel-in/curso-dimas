# Agregar columnas a un DF
import pandas as pd

personas = {
    "nombre": ["dimas", "Juan", "Ana"],
    "edad" : [23, 24, 25],
    "país" : ["España", "Mexico", "Chile"]
}

df = pd.DataFrame(personas)
print (df)
#  nombre  edad    país
#0  dimas    23  España
#1   Juan    24  Mexico
#2    Ana    25   Chile

# 1 Sintaxis básica
#Añadimos profesiones.
df["profesiones"] = ["Ingeniero", "Maestro", "Bombero"]
print(df)
#  nombre  edad    país profesiones
#0  dimas    23  España   Ingeniero
#1   Juan    24  Mexico     Maestro
#2    Ana    25   Chile     Bombero

# 2 Assing
#Añadimos sueldos
df = df.assign(sueldo=[20000,30000,40000])
print(df)
#  nombre  edad    país profesiones  sueldo
#0  dimas    23  España   Ingeniero   20000
#1   Juan    24  Mexico     Maestro   30000
#2    Ana    25   Chile     Bombero   40000

# 3 insert
#Añadimos la columna donde nos de la gana

df.insert(3,"email",["dimas@email","fuan@email","jose@email"])
print(df)
#  nombre  edad    país        email profesiones  sueldo
#0  dimas    23  España  dimas@email   Ingeniero   20000
#1   Juan    24  Mexico   fuan@email     Maestro   30000
#2    Ana    25   Chile   jose@email     Bombero   40000
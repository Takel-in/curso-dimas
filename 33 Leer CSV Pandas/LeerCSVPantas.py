#Leer archivo CSV en Python con pandas.

import pandas as pd
#df = pd.read_csv("./33 Leer CSV Pandas/avocado_full.csv", index_col=0) #En este caso le indicamos que columnas es el indice para que no la genere él.
df = pd.read_csv("./33 Leer CSV Pandas/avocado_full.csv", index_col=["Date"]) #Aquí le decimos que use la fecha como índice.
print(df) #Esto imprimre todo el DF
print(df.head(5)) # Esto imprimle las líneas que queremos. 

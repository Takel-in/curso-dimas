#Panda con MATPLOLIB

"""
En este scrip nos aseguramos de tener todo el setup montado,
liberias, datasets, etx. y que lo podemos ejecutar correctamente.

 pip install pandas matplotlib numpy -> En la consola de comandos



"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#Verificas si están instaladas.
print ("Si me imprimo es que todo está ok") #Si me imprimo es que todo está ok

df = pd.read_csv("./34 Pandas y MATPLOTLIB/data/avocado_full.csv")
print(df.head(5))#Que nos muestre las 5 primeras filas y el nombre de las columnas

print(df["region"][:49]) #Esto me imprime las 49 primera filas.(de la 0 a la 48)

# Como no queremos trabar con todo, vamos a coger la región de chicado y lo vamos 
# a ordenador por fecha. 
chicago = df[df["region"] == "Chicago"]
print(chicago.head(5)) # Imrpime los 5 primeras filas cuya región es chicago.
#           Date  AveragePrice  Total Volume      4046       4225      4770  Total Bags  Small Bags  Large Bags  XLarge Bags          type  year   region
#416  2015-12-27          0.93     661137.13  42799.00  445218.79  78378.25    94741.09    83066.75     1617.67     10056.67  conventional  2015  Chicago
#417  2015-12-20          0.91     690669.34  35724.99  464574.15  96306.30    94063.90    76241.25     9592.65      8230.00  conventional  2015  Chicago
#418  2015-12-13          1.07     668601.50  40380.09  451470.42  94162.53    82588.46    76829.42     5693.75        65.29  conventional  2015  Chicago
#419  2015-12-06          1.14     664020.49  53173.18  455048.11  92888.37    62910.83    62473.12      420.95        16.76  conventional  2015  Chicago
#420  2015-11-29          1.11     602481.22  42851.47  422479.32  74988.97    62161.46    61862.57      298.89         0.00  conventional  2015  Chicago

# Ahora queremos que el índice sea la fecha.
chicago = chicago.set_index("Date")

#Queremos que lo ordene por la fecha.
chicago = chicago.sort_values(by="Date")

print (chicago.head(5))
#            AveragePrice  Total Volume      4046       4225       4770  Total Bags  Small Bags  Large Bags  XLarge Bags          type  year   region
#Date                                                                                                                                                
#2015-01-04          1.11     783068.03  30270.26  550752.19  124506.10    77539.48    72888.46     4651.02         0.00  conventional  2015  Chicago
#2015-01-04          1.49      17723.17   1189.35   15628.27       0.00      905.55      905.55        0.00         0.00       organic  2015  Chicago
#2015-01-11          1.15     802874.94  31239.94  558487.79  133848.57    79298.64    74716.43     4539.25        42.96  conventional  2015  Chicago
#2015-01-11          1.79      12915.74   1426.75   10900.10       0.00      588.89      588.89        0.00         0.00       organic  2015  Chicago
#2015-01-18          1.14     797741.43  24917.77  533717.99  140239.95    98865.72    95516.44     3311.71        37.57  conventional  2015  Chicago


#Vamos a trabajar con la librería mapplotlib.  que poemos hacer gráficos 
MAX_SAMPLES = 100

precio = chicago["AveragePrice"][:MAX_SAMPLES]
cantidad = chicago["Total Volume"][:MAX_SAMPLES]

plt.plot(precio, label="precio medio")
plt.plot(cantidad, label="Volumen total")
plt.title ("precios de los aguacates a lo largo de los tiempos")
plt.xlabel("Fecha")
plt.xticks(rotation=90) #para que se vean las fechas de la leyenda en vertical.
plt.ylabel("Precio")
plt.legend()
plt.show()
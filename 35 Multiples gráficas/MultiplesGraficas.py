# Multiples Gráficas.
""" En este scritp seguiremos trabajando con la librería MatPlotLib. En concreto 
aprenderemos a trabajar con subplots.

Los subplots nos permite trabajar con múltiples ejes en una misma figura. De esta forma,
podemos graficar varis funciones en ejes distintos.

Seguiremos extrayendo los datos del dataset de los aguacates.
"""

import pandas as pd
import matplotlib.pyplot as plt

#Abrimos el fichero.
df = pd.read_csv("./35 Multiples gráficas/data/avocado_full.csv")

#Nos quedamos con las filas de Atlanta.
atlanta = df[df["region"]=="Atlanta"]
print (atlanta.head(5))

#Cogemos los datos que nos interesa.
precio = atlanta["AveragePrice"]
volumen = atlanta["Total Volume"]

#Como los datos del precio medio salen bastante mal. Lo unico que hacemos es coger las primera 25 y  hacer la media, se mueve una a la siguiente y coge 25 y otra vez la media
#Con esto se hace que la oscilación sea menor.
precioPromediado = precio.rolling(25).mean()

#Aquí indico que si no llega a la muestra 30 vaya cogiendo las muestras que tiene hasta esa posición.
precioPromediado2 = precio.rolling(25, min_periods=1).mean() 


bolsasAguacate = atlanta["Total Bags"]
sbolsas = atlanta["Small Bags"]
lbolsas = atlanta["Large Bags"]
xbolsas= atlanta["XLarge Bags"]

# Se indicamos el número de filas, columnas y el orden del eje.
# Indicamos el número de filas columnas y el orden del eje
plt.subplot(221)
plt.title("Precio aguacate")
plt.plot(precio, label="Prcio", color="green")
plt.legend()

plt.subplot(221)
plt.title("Precio aguacate")
plt.plot(precioPromediado2, label="PrcioPromediado2", color="Red")
plt.legend()

plt.subplot(221)
plt.title("Precio aguacate")
plt.plot(precioPromediado, label="PrcioPromediado", color="Orange")
plt.legend()




# Indicamos el número de filas columnas y el orden del eje
plt.subplot(222)
plt.title("volumen de aguacates")
plt.plot(volumen, label="columen total", color="red")
plt.legend()

plt.subplot(223)
plt.title("Bolsas totales de aguacatea")
plt.plot(bolsasAguacate, label="bolsas totales", color="blue")
plt.legend()

plt.subplot(224)
plt.title("Bolsas por tamaño")
plt.plot(sbolsas, label="bolsas - S", color="black")
plt.plot(lbolsas, label="bolsas - L", color="cyan")
plt.plot(xbolsas, label="bolsas - XL", color="yellow")
plt.legend()



#Como hacer cuando sale todo apelotonado.
plt.tight_layout()


plt.show()
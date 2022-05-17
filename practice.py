import numpy as np
import pandas as pd

listaUna = [1,2,3,4,5,6,7,8]
listaDos = [[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12]]

newArray = np.array(listaUna)
newArray2 = np.array(listaDos)

#Traer de 2 en 2
newArray3 = newArray[::2]
#Traer todos
newArray4 = newArray[:]
#Traer los ultimos tres, de atras para adelante
newArray5 = newArray[-3:]
#Taer a partir de la fila 1, desde la columna 0 a la 2
newArray6 = newArray2[1:,0:2]
#Especificar tipo de array
newArray7 = np.array(listaUna, dtype='float64')
#Cambiar tipo desde la libreria numpy
newArray8 = newArray7.astype(np.bool_)
#Numero de dimensiones
newArray9 = newArray2.ndim
#Agregar dimensiones
newArray10 = np.array(newArray, ndmin=10)
#Expandir la dimension, en el eje 0 -> Fila / 1 -> Col
newArray11 = np.expand_dims(newArray2, axis=0)
#Aplicar squeeze, llevar el array a las dimensiones correectas
newArray12 = np.squeeze(newArray10)
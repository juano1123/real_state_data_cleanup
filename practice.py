import numpy as np

listaUna = [1,2,3,4]
listaDos = [
    #[1,2,3,4],
    [5,6,7,8]
]

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
#Maximo del array
maxUna = newArray.max()
#Indice donde se encuentra el maximo del array
argMaxUna = newArray.argmax()
#Diferencia entre el pico mas grande y pico mas chico
ptpArray = newArray.ptp()
#Obtener el percentile
percentilArray = np.percentile(newArray, 50)
#Obtener la mediana del array
medianaArray = np.median(newArray)
#Obtener la desviacion standar del array
desviacionStandarArray = np.std(newArray)
#Obtener la varianza del array, que es igual a la desviacion standar elevada al cuadrado
varianzaArray = np.var(newArray)
#Obtener la media, suma de todos divididos la cantidad
mediaArray = np.mean(newArray)
#Concatenar arrays
arraysConcatenados = np.concatenate((np.expand_dims(newArray, axis=0), newArray2), axis=0)
#Transpuesta, si tenia un array de 2x3, pasa a ser de 3x2
transpuestaArray = newArray2.T
#Crear array de 0 a 10
arrayNuevo = np.arange(0, 11)
#Copia de array para trabajar tranquilo
arrCopy = arrayNuevo.copy()
#Modifico los valores del array copy, les doy valor 1 a todos
arrCopy[:] = 1
#print(arrCopy)
linspaceArray = np.linspace(1, 10, 10,dtype='float64')
#Aplicar condicion y filtrar array
arrayCondicion = np.arange(0, 10)
arrayCondicion[(arrayCondicion > 5) & (arrayCondicion < 9)] = 23
#arrayOperaciones = newArray * 2
arrayOperaciones = newArray
arrayOperaciones2 = newArray2
#print(np.expand_dims(arrayOperaciones, axis=0))
#print(arrayOperaciones2)
#print(np.expand_dims(arrayOperaciones, axis=0) * arrayOperaciones2)
#print(arrayOperaciones2)
arrayReshape = arrayOperaciones2.reshape(2,2)
arrayReshape2 = arrayReshape.copy()
#print(arrayReshape)
#print(arrayReshape2)
#print(arrayReshape - arrayReshape2)
#print(np.matmul(arrayReshape, arrayReshape2))
arr1 = np.array([[4,1,2]])
arr4 = np.array([[4],
                 [1],
                 [2]
                ])
arr3 = np.array([[3,4,5]])
arr2 = arr1.reshape(3,1)
#Producto matricial de dos arreglos
print(np.matmul(arr1, arr4))
print(arr1 == arr4.T)
#El producto punto es la multiplicacion de las matrices por su tranpuesta
print(arr1 @ arr4)
#array equal
print(np.array_equal(arr1,arr4.T))
#shape devuelve una tupla que explica la matriz (x,y)
print(arr3.shape)
arr5 = np.array([[4,1,2,6,6]])
#quitar valores repetidos con unique
arr6 = np.unique(arr5)
print(arr6)

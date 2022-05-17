import numpy as np
import pandas as pd

#Obtengo el data_frame
data_frame = pd.read_csv('./assets/real_estate.csv', sep=";")

#Columnas
columns = data_frame.columns

#Datos Price
columnPrice = data_frame["price"]
max_index_price = columnPrice.idxmax()
min_index_price = columnPrice.idxmin()

#Datos Surface
columnSurface = data_frame["surface"]
max_index_surface = columnSurface.idxmax()
max_value_surface = columnSurface.max()
min_index_surface = columnSurface.idxmin()
min_value_surface = columnSurface.min()

#Solutions
print(columns)
print(f"The id of the most expensive house is {max_index_price}")
print(f"The id of the cheapest house is {min_index_price}")
print(f"The id of the smallest house is {min_index_surface} and has a surface of {min_value_surface}")
print(f"The id of the biggest house is {max_index_surface} and has a surface of {max_value_surface}")
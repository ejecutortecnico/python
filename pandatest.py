import pandas as pd
import numpy as np
# Crear diferentes tipos de datos
labels = ['a','b','c'] # lista de etiquetas
my_list = [10,20,30] # lista con valores
arr = np.array([10,20,30]) # Convertir ista de valores en arreglo NumPy
d = {'a':10,'b':20,'c':30} # Creacion de un diccionario

# Convertir una lista en series usando el método pd.Series
# observe que se crean los nombres con las posiciones de cada elemento
arr = pd.Series(data=my_list)
arr = pd.Series(data=my_list,index=labels)
arr = pd.Series(my_list,labels)

arr = np.array([10,20,30]) # Convertir ista de valores en arreglo NumPy
arr1 = pd.Series(arr)
arr1 = pd.Series(arr,labels)
arr1 = pd.Series(d)
arr1 = pd.Series(data=labels)


# Creacion de una serie con sus labels o indices
ser1 = pd.Series([1,2,3,4],
index = ['Colombia', 'Peru','Chile', 'Brazil'])
ser2 = pd.Series([1,2,5,4],
                 index = ['Venezuela', 'Ecuador','Nicaragua', 'Mexico'])

print(ser1 + ser2)


import pandas as pd
import numpy as np
# Importar la función de NumPy para crear arreglos de números enteros
from numpy.random import randn
np.random.seed(101) # Inicializar el generador aleatorio

# Forma rapida de crear una lista de python desde strings
'A B C D E F'.split()

['A', 'B', 'C', 'D', 'E', 'F']

# Crear un dataframe con números aleatorios de 4 Columnas y 5 Filas
# Crear listas rapidamente usando la función split 'A B C D E'.split()
# Esto evita tener que escribir repetidamente las comas

df = pd.DataFrame(randn(6,4),
                  index='A B C D E F'.split(),
                  columns='W X Y Z'.split())

print(df.describe())
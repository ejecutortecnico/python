import pandas as pd
import matplotlib.pyplot as plt


lista1 = [1,2,3,4,5,6,7]
lista2 = [2,4,9,16,25,36,49]
df = pd.Series(lista1)
print(df)
datos = {"Nombre": ["Ana", "Juan", "Pedro"], "Edad": [25, 30, 35]}
print(datos)
data = pd.DataFrame(datos)
print(data)

plt.plot(lista1, lista2)
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Gráfico de Líneas")
plt.show()
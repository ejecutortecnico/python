import pandas as pd
import matplotlib.pyplot as plt

serie1 = pd.Series([1, 2, 3, 4, 5])
serie2 = pd.Series([1, 4, 9, 15, 25])



df = pd.DataFrame([serie1,serie2])

print(df)

plt.plot(serie1, serie2)
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Gráfico de Líneas")
plt.show()

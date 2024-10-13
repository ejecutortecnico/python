# Las Listas son Variables Mutables
H = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
P = H # copiar todo el contenido de H a P
P[0] = 333
print("Observar el que ocurre con 'H' cuando se cambia el valor de 'P', si P = H")
print(f'P = {P}') # uso de f-strings para imprimir los resultados
print(f'H = {H}') # uso de f-strings para imprimir los resultados

suma = lambda x, y: x + y
print(suma(4, 7))

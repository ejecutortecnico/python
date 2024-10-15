tamano = input("Ingrese el tamaño de la lista")
lista = []
for i in range(int(tamano)):
    valor = input(f"ingrese el elemento {i + 1} de la lista ")
    lista.append(valor)
print(lista)


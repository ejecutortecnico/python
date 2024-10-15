tamano = int(input("Ingrese el tamaño de la lista"))
lista = []
i=0
while tamano != 0:
    i+=1
    valor = input(f"ingrese el elemento {i} de la lista ")
    lista.append(valor)
    tamano-=1
print(lista)
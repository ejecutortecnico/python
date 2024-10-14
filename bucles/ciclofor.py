
tamano = input("ingrese el tamaño de la lista")
lista = []
for i in range(int(tamano)):
    print(f'el valor a ingreser es: {i} ')
    valor = input()
    lista.append(valor)
print(lista)
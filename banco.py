nombres = []
apellidos = []
edades = []
telefonos = []
saldos = []
global opcion
opcion = 100

def editar():
    print("ingrese el nombre del cliente a editar")
    nombre = input()
    for i in range(len(nombres)):
        if nombres[i] == nombre:
            nombres.remove(nombre)
            apellidos.remove(apellidos[i])
            edades.remove(edades[i])
            telefonos.remove(telefonos[i])
            saldos.remove(saldos[i])

def borrar():
    print("ingrese el nombre a borrar")
    nombre = input()
    for i in range(len(nombres)):
        if nombres[i] == nombre:
            nombres.remove(nombre)
            apellidos.remove(apellidos[i])
            edades.remove(edades[i])
            telefonos.remove(telefonos[i])
            saldos.remove(saldos[i])

def inicio():
    print("Banco de TalentoTech")
    print("ingrese 1 para agregar clientes")
    print("ingrese 2 para ver clientes")
    print("ingrese 3 para borrar clientes")
    print("ingrese 4 para editar clientes")
    print("ingrese 0 para Salir")
    opcion = int(input("ingrese la opcion"))
    if opcion == 1:
        print("Ingrese el nombre")
        nombre = input()
        nombres.append(nombre)
        print("Ingrese el Apellido")
        apellido = input()
        apellidos.append(apellido)
        print("Ingrese la edad")
        edad = input()
        edades.append(edad)
        print("Ingrese el telefono")
        telefono = input()
        telefonos.append(telefono)
        print("Ingrese el saldo")
        saldo = input()
        saldos.append(saldo)
    elif opcion == 2:
        print("eligio la opcion 2")
        for i in range(len(nombres)):
            print(f"nombres: {nombres[i]} {apellidos[i]} Saldo: {saldos[i]}")
    elif opcion == 3:
        print("eligio la opcion 3")
        borrar()
    elif opcion == 4:
        print("eligio la opcion 4")
        editar()
    elif opcion == 0:
        return opcion
    else:
        print("no eligio una opcion valida")

while True:
    opcion = inicio()
    if opcion == 0:
        break
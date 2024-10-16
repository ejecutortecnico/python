cliente = {
    "nombre":"jorge",
    "apellido":"Rodriguez",
    "telefono": "3236315530",
    "saldo":"50000",
    "edad": "40"
}
print(cliente)
valor = cliente.get("nombre")
print(valor)
cliente["profesion"] = "ingeniero"
print(cliente)
print(cliente["telefono"])
del cliente["telefono"]
print(cliente)
print(cliente.keys())
print(cliente.values())
cajero = {
    "nombre":"juan",
    "apellido":"ramirez"
}
cliente.update(cajero)
print(cliente)
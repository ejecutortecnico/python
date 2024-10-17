import random
numero = random.randint(1, 10)
intentos=0
while True:
    valor = input("ingrese su numero")
    if int(valor) == numero:
        print("Has acertado y ganado")
        break
    else:
        print("has fallado")
        intentos+=1
    if intentos > 5:
        print("Game Over")
import random

numero_secreto = random.randint(1,100)
cantidad_inicial_de_intentos = 0
# -------------------------------------------------------------------------------------------------------------------------
cantidad_max_de_intentos = 5 # Coloque la cantidad de intentos. Cuanto mayor la cantidad, mayor sera el reto
adivinado = False

print("Bienvenido al Juego de Adivinar el Numero Secreto")

while not adivinado and cantidad_inicial_de_intentos < cantidad_max_de_intentos:
    entrada = input("Introduce a continuacion un numero del 1 al 99: ") # TODO (pendiente en ingles): Convertir a numero
    numero = int(entrada)
    
    if numero == numero_secreto:
        print("Felicitaciones, has ganado el juego!!")
        adivinado = True
    elif numero < numero_secreto:
        print("El numero es mayor al numero ingresado")
    else:
        print("El numero es menor al numero ingresado")

    cantidad_inicial_de_intentos += 1

if not cantidad_inicial_de_intentos < cantidad_max_de_intentos:
    print(f"GAME OVER - No has podido adivinar dentro de los {cantidad_max_de_intentos} intentos")
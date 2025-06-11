cantidad_turnos_comienzo = 0
cantidad_turnos_de_juego = 3

print ("Vamos a Jugar al Piedra Papel o Tijeras?")

nombre_j1 = input("Hola Jugador 1, que nombre elijes? : ")
nombre_j2 = input("Hola Jugador 2, que nombre elijes? : ")

puntos_del_j1 = 0
puntos_del_j2 = 0

while cantidad_turnos_comienzo < cantidad_turnos_de_juego:

    jugador_1 = input(f"{nombre_j1}, que elijes? Piedra, Papel o Tijeras? : ")
    jugador_2 = input(f"{nombre_j2}, que elijes? Piedra, Papel o Tijeras? : ")
    
    elemento_juego1 = jugador_1.lower()
    elemento_juego2 = jugador_2.lower()
    
    condicion1 = elemento_juego1 == "piedra" and elemento_juego2 == "tijeras" # Condicion que gana Jugador 1
    condicion2 = elemento_juego1 == "papel" and elemento_juego2 == "piedra" # Condicion que gana Jugador 1
    condicion3 = elemento_juego1 == "tijeras" and elemento_juego2 == "papel" # Condicion que gana Jugador 1
    
    if elemento_juego1 == elemento_juego2:
        print("Ha sido un empate!!")
    elif condicion1 or condicion2 or condicion3:
        print (f"Ha ganado {nombre_j1}") # Condicion que gana Jugador 1
        puntos_del_j1 += 1
    else:
        print (f"Ha ganado {nombre_j2}") # Condicion que gana Jugador 2
        puntos_del_j2 += 1
    
    cantidad_turnos_comienzo += 1

if cantidad_turnos_comienzo == cantidad_turnos_de_juego:
    print ("¡GAME OVER! - ¡Juego Terminado!")
    print ("Tabla de Puntos: " \
    "-----------------------------------------")
    print (f"Los puntos de {nombre_j1} son: {puntos_del_j1}") 
    print (f"Los puntos de {nombre_j2} son: {puntos_del_j2}") 
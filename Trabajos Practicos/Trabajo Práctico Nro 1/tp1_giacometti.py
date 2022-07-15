import random
import time
def tennis_match():
    """
    En este trabajo práctico se busca implementar un programa con la capacidad 
    de manejar el indicador de puntaje de cada jugador durante un game de tenis.
    El programa cuenta con 2 modalidades: El modo manual,que debe permitir que el usuario 
    ingresar el ganador de cada punto y el modo simulación, que debe poder simular el 
    ganador del punto en tiempo real o determinar directamente el ganador del game. 
    ----------
    Returns
    -------
    None.

    """
    print('''** Welcome to the Super Tennis Annotator app **

How do you want to use it?

1. Manual input
2. Simulation''')
    
    game_mode = int(input('Mode: ')) #El usuario ingresa el modo de juego del programa
    mode = 0
    while (True):  #Sistema para evitar la seleccion de un modo inexistente
        if game_mode == 1 or game_mode == 2:
            break
        elif game_mode != 1 or game_mode != 2:
            print("\nInvalid Mode")
            game_mode = int(input("Insert a valid mode: "))    
    print('\n** Super Tennis Annotator **')
    player1 = input("Insert Player 1's name: ") #Almacena el nombre del jugador 1
    player2 = input("Insert Player 2's name: ") #Almacena el nombre del jugador 2
    while (True):  #Sistema para evitar la repeticion de nombres de jugadores
        if player1 != player2:
            break
        elif player1 == player2:
            print("\nBoth players have the same name")
            print ('Please put different names')
            player1 = input("Insert Player 1's name: ")
            player2 = input("Insert Player 2's name: ")
    if game_mode == 2: #Si ingresa al modo de juego 2 ("Simulation"), el usuario tendra que eleguir un modo de simulación
        print('''\nSelect a Simulation Mode

1. Real Time Match
2. Only Result''')
        mode = int(input('Mode: ')) #El usuario ingresa el modo de simulación
        while (True):  #Sistema para evitar la seleccion de un modo inexistente
            if mode == 1 or mode == 2:
                break
            elif mode != 1 or mode != 2:
                print("\nInvalid Mode")
                mode = int(input("Insert a valid mode: "))
    player1_score = 0
    player2_score = 0 
    players = (player1,player2)
    if mode == 1 or game_mode == 1:
        print('''\nScore:\n''',
        player1, ': 0\n',
        player2, ': 0')
    while ((player1_score < 4 and player2_score < 4) or #Bucle donde se computa el game
          (player1_score == 4 and player2_score == 3) or
          (player1_score == 3 and player2_score == 4)):
        new_score = {0:0,1:15,2:30,3:40,4:"AD"} #Asocio nuevos valores a los numeros con diccionario
        if mode == 1:
            time.sleep(1) #Agrega un retraso al bucle de 1 segundo
        if game_mode == 1: 
            point = input('Who score ?: ') #Usuario ingresa quien anoto el punto
        elif game_mode == 2:
            point = random.choice(players) #Se selecciona de manera aleatoria el nombre de los jugadores
            if mode == 1:
                print('\nWho score ?:', point)
        if point == player1: 
            player1_score += 1
        elif point == player2:
            player2_score += 1 
        if player1_score <=3 and player2_score <=3:
            if mode == 1 or game_mode == 1:
                print('''Score:\n''',
                player1, ':' ,new_score[player1_score],'\n',
                player2, ':', new_score[player2_score])
        elif player1_score == player2_score:
            player1_score, player2_score = 3,3
            if mode == 1 or game_mode == 1:
                print('''Score:\n''',
                player1, ':' ,new_score[player1_score],'\n',
                player2, ':', new_score[player2_score])
        elif player1_score == 4 and player2_score == 3:
            if mode == 1 or game_mode == 1:
                print('''Score:\n''',
                player1, ':' ,new_score[4],'\n',
                player2, ':', new_score[3])
        elif player1_score == 3 and player2_score == 4:
            if mode == 1 or game_mode == 1:
                print('''Score:\n''',
                      player1, ':' ,new_score[3],'\n',
                      player2, ':', new_score[4]) 
    if player1_score > player2_score: #Determina quien de los jugadores fue el ganador
            print(player1, 'wins the game')
    else:
            print(player2,'wins the game')
tennis_match()
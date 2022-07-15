'''
Suponga que tiene dos dados, asumiendo en ambos la misma probabilidad de ocurrencia por
cada número (1/6). El juego consiste en dos participantes que, por turno, deben tirar los dos dados
simultáneamente y seguir las siguientes reglas:

1. Si ambos dados salen con diferente número (ej: 3 y 6), se suman y se le asigna ese valor como
puntaje al jugador. Luego pasa a jugar el siguiente participante.

2. Si ambos dados salen con el mismo número (ej: 4 y 4), se suman y se le asigna ese valor como
puntaje al jugador, pero en este caso el jugador puede volver a tirar, de manera tal que el
nuevo puntaje se acumule con el anterior, concluyendo su turno al sacar los dos números
distintos (caso 1).

El jugador que haya obtenido mayor puntaje será el ganador de la mano.

En base a este reglamento, implemente un algoritmo que le solicite a cada jugador que tire los dados
oprimiendo una tecla, luego genere dos números aleatorios entre 1 y 6 (simulando los dos dados)
siguiendo las reglas del juego. Al concluir el turno de cada jugador, deberá indicarse el puntaje de ese
participante y pasar al otro.
'''
import random
def dados():
    dados1 = int(input('Jugador Nro 1 presione la tecla 1 para tirar los dados '))
    while (True):
        if dados1 == 1:
            break
        else:
            dados1 = int(input('Error. Por favor presione la tecla 1 para tirar los dados '))
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    player1_score = dado1 + dado2
    print('\nTus puntos fueron',dado1,'y',dado2,'.En  total tus puntos son',player1_score)
    while dado1 == dado2:
        dados1 = int(input('Al ser el resultado el mismo en ambos dados, tienes un nuevo tiro. Presiona el 1 para tirar nuevamente '))
        while (True):
            if dados1 == 1:
                break
            else:
                dados1 = int(input('Error. Por favor presione la tecla 1 para tirar los dados '))
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        player1_score += (dado1 + dado2)
        print('\nTus puntos fuero',dado1,'y',dado2,'.En total tus puntos son',player1_score)
    dados2 = int(input('Jugador Nro 2 presione la tecla 2 para tirar los dados '))
    while (True):
        if dados2 == 2:
            break
        else:
            dados2 = int(input('Error. Por favor presione la tecla 2 para tirar los dados '))
    dado1_2 = random.randint(1,6)
    dado2_2 = random.randint(1,6)
    player2_score = dado1_2 + dado2_2
    print('\nTus puntos fueron',dado1_2,'y',dado2_2,'.En total tus puntos son',player2_score)
    while dado1_2 == dado2_2:
        dados2 = int(input('Al ser el resultado el mismo en ambos dados, tienes un nuevo tiro. Presiona el 2 para tirar nuevamente '))
        while (True):
            if dados2 == 2:
                break
            else:
                dados2 = int(input('Error. Por favor presione la tecla 2 para tirar los dados '))
        dado1_2 = random.randint(1,6)
        dado2_2 = random.randint(1,6)
        player2_score += (dado1 + dado2)
        print('\nTus puntos fuero',dado1_2,'y',dado2_2,'.En  total tus puntos son',player2_score)
    print('\nResultado final: Jugador Nro 1:',player1_score,'puntos y Jugador Nro 2:',player2_score,'puntos')
    if player1_score > player2_score:
        print('\nJugador Nro 1 gano la partida')
    else:
        print('\nJugador Nro 2 gano la partida')
    
dados()
        
                    
                
                
        
        
        
    
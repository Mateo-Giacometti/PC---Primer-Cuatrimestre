'''
Escriba un programa que juegue al piedra, papel o tijera contra el humano.
'''
import random
def rock_paper_scissor():
    print("Welcome to 'Rock, Paper and Scissor'")
    player = int(input('Rock, paper and scissor ? Press 1 for Rock, 2 for Paper and 3 for Scissor: '))
    while True:
        if player == 1 or player == 2 or player == 3:
            break
        else:
            print('\nError, you select a wrong numbre.')
            player = int(input('Press 1 for Rock, 2 for Paper and 3 for Scissor: '))
    selection = (1,2,3)
    machine = random.choice(selection)
    if machine == 1:
        print('\nPC select Rock')
    elif machine == 2:
        print('\nPC select Paper')
    else:
        print('\nPC select Scissor')
    if machine == player:
        print('\nBoth players select the same element. This is a draw')
    elif (machine == 1 and player == 2) or (machine == 2 and player == 1):
        print('\nPaper beats Rock')
        if machine == 2:
            print('\nPC wins')
        else:
            print('\nHuman wins')
    elif (machine == 1 and player == 3) or (machine == 3 and player == 1):
        print('\nRock beats Scissor')
        if machine == 1:
            print('\nPC wins')
        else:
            print('\nHuman wins')
    elif (machine == 2 and player == 3) or (machine == 3 and player == 2):
        print('\nScissor beats Paper')
        if machine == 3:
            print('\nPC wins')
        else:
            print('\nHuman wins')      
rock_paper_scissor()
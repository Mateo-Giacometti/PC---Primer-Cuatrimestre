#Decidir si una letra es vocales 
def es_vocal(letra):
    if (letra == 'a' or letra == 'A' or letra == 'e' or letra == 'E' or
        letra == 'i' or letra == 'i' or letra == 'o' or letra == 'O' or
        letra == 'u' or letra == 'u'):
        return True
    else:
        return False
#Decir si una palabra tiene vocal o no 
def tiene_vocales(p):
    s = False
    for i in p:
        s = s or es_vocal(i)
    return s
#Contar cuantas vocales tiene una palabra
def contar_vocales(p):
    s = 0
    for i in p:
        if es_vocal(i):
            s = s + 1
    return s
#Jugar al piedra, papel o tijera
def reglas(player1, player2):
    if player1 == 'piedra' and player1 == 'tijera':
        return 1
    elif player1 == 'piedra' and player1 == 'papel':
        return 2
    elif player1 == 'papel' and player1 == 'tijera':
        return 2
    elif player1 == 'papel' and player1 == 'piedra':
        return 1
    elif player1 == 'tijera' and player1 == 'papel':
        return 1
    elif player1 == 'tiejera' and player1 == 'piedra':
        return 2
    elif player1 == player2:
        return 0
  
        
    

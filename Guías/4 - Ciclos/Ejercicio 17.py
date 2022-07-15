'''
Escriba una función que calcule la raíz cúbica de un número utilizando ciclos. Si el número no
es un cubo perfecto, que devuelva el resultado aproximado e imprima un mensaje para dar aviso.
'''
def cubo_mas_cercano():
    number = int(input("Ingrese un numero: "))
    cubo = number ** (1/3)
    if cubo == int (cubo):
        print("Tu numero es un cubo perfecto")
    else:
        positive_number = number
        while True:
            positive_number += 1
            positive_cubo = positive_number ** (1/3)
            if positive_cubo == int(positive_cubo):
                break
        negative_number = number
        while True:
            negative_number -= 1
            negative_cubo = negative_number ** (1/3)
            if negative_cubo == int(negative_cubo):
                break
        comparative1 = abs(number - positive_number)
        comparative2 = abs(number - negative_number)
        if comparative1 < comparative2:
            print("El cubo perfecto mas cercano es el ",positive_number)
        else:
            print("El cubo perfecto mas cercano es el ",negative_number)
cubo_mas_cercano()
'''
Implementamos una agenda con un diccionario, donde almacenamos nombres y números
telefónicos. Escribir un programa que vaya solicitando al usuario que ingrese nombres, luego:
1. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, opcionalmente, permitir
modificarlo si no es correcto.
2. Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
El usuario puede utilizar la cadena ”*”, para salir del programa.
'''
def telephone_numbers(seguir):
    dic = {'Mateo Giacometti': 3364180261,'Fausto Pettinari':3364230854,'Colo Schuemer':3364357698}
    while seguir:
        busqueda = input('Ingrese el nombre de la persona cuyo numero de telefono quiere saber: ')
        for i in dic:
            if i == busqueda:
                print('El numero de la persona que esta buscando es: ')
        
        
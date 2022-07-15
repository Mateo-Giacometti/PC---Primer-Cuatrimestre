"""
Asignaciones con error de sintaxis:
    
2var-seg = 150
True = 17
a = b = la puerta azul está abierta
x = 5, y = 10
'suma' = 3

"""
#Correciones
var_seg = 150 # No se puede usar un numero al principio de una variable

Verdadero = 17 # True es una palabra reservada

a = b = 'la puerta azul está abierta' # No se le puede asignar texto sin estar definido como un str a una variable

x, y = 5, 10 # Esta es la forma correcta de asignarle valor a distintas variable en una misma linea

suma = 3 # No se puede usar un str para declarar una variable


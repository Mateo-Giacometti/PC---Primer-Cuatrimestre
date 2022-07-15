'''
Escriba una función que le pida al usuario ingresar un número y que devuelva dos enteros, root
y pwr, tal que 0 < pwr < 6 y root ** pwr sea igual al número ingresado. Si los dos enteros n existen, 
que imprima un mensaje de aviso.

'''
def devolucion(m):
     root = 0
     while root <= m:
         for pwr in range(1,6):
             if root**pwr == m:
                 return root, pwr
         root += 1
     return False
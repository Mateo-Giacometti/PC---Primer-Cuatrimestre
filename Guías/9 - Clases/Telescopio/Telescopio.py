'''
El archivo de texto "Registro" es un reporte de mediciones de aperturas de los telescopios de una estacion de observacion para un dia.

Se pide:

- Leer y procesar el archivo 
- Imprimir la suma de los angulos de apertura de cada telescopio durante el dia de reporte.
- Indicar los momentos del dia y el nombre del operador donde los telescopios austral y norte son iguales.
- Extra: Indicar los momentos del dia donde la diferencia de apertura del telescopio austral y norte sean menores a 10 min.

'''
from cmath import cos
from Sexagesimal import Sexagesimal

def telescopio(filename):
    with open(filename,'r') as f:
        registros = {}
        igualdades = {}
        reg_igualdades = []
        for line in f:
            reg_limpio = []
            lista = line.split(', ')
            for v in range(len(lista)):
                if v == 3:
                    if lista[v] == 'sin modificacion\n' or lista[v] == 'sin modificacion':
                        reg_limpio = []
                    else:
                        coso = lista[v].replace('\n','')
                        nuevo = coso.split(' ')
                        for r in range(len(nuevo)):
                            nuevo[r] = float(nuevo[r])
                        reg_limpio.append(nuevo)
                else:
                    reg_limpio.append(lista[v])
            if len(reg_limpio) > 1:
                if reg_limpio[2] in registros:
                    b = Sexagesimal(reg_limpio[3][0],reg_limpio[3][1],reg_limpio[3][2])
                    registros[reg_limpio[2]] = registros[reg_limpio[2]] + b
                    igualdades[reg_limpio[0] + '-' + reg_limpio[1]+ '-' + reg_limpio[2]] = registros[reg_limpio[2]]
                else:
                    result = Sexagesimal(reg_limpio[3][0],reg_limpio[3][1],reg_limpio[3][2])
                    registros[reg_limpio[2]] = result
                    igualdades[reg_limpio[0] + '-' + reg_limpio[1] + '-' + reg_limpio[2]] = result
        for j in igualdades:
            for d in igualdades:
                if j != d and igualdades[j] == igualdades[d]:
                    if d not in reg_igualdades and j not in reg_igualdades:
                        reg_igualdades.append(d)
                        reg_igualdades.append(j)
        apertura = str(registros).replace('{','').replace('}','')
        igual_ap = str(reg_igualdades).replace('[','').replace(']','')

    return print('Apertura de cada telescopio al final del dia:',apertura,'\nMomentos en que las aperturas son iguales:',igual_ap)
            

            
                
        

    
            





# %%

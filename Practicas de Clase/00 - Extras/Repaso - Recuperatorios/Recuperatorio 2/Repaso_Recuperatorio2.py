# %%
#Guia de archivos - Ejercicio 1
from hashlib import new


def less(filename: str):
    with open(filename,'r') as f:
        for line in f:
            print(line)

less('ejemplo.txt')
# %%
#Guia de archivos - Ejercicio 2
def head(filename: str, N: int):
    with open(filename, 'r') as f:
        for line in range(N):
            print(f.readline(), end="")

head('ejemplo.txt', 3)
#%%
#Guia de archivos - Ejercicio 3
def tail(filename: str, N: int):
    with open(filename, 'r') as f:
        lines = f.readlines()
        for i in range(len(lines) - N, len(lines)):
            print(lines[i], end="")
    
tail('ejemplo.txt', 2)
#%%
#Guia de archivos - Ejercicio 4
def touch(file_name: str):
    try:
        file = open(file_name, 'xt')
        file.close
        return f'The file "{file_name}" was created successfully.'
    except FileExistsError:
        return f'The file "{file_name}" already exists.'

print(touch('new_file.txt'))
#%%
#Guia de archivos - Ejercicio 5
def cp(filename1: str, filename2: str):
    with open(filename1, 'r') as f1:
        lines = f1.readlines()
        with open(filename2, 'w') as f2:
            f2.writelines(lines)

cp('ejemplo.txt', 'new_file.txt')
#%%
#Guia de archivos - Ejercicio 6
def wc(filename: str) -> str:
    words = 0
    caracters = 0
    with open(filename, 'r') as f:
        lines = f.readlines()
        for i in lines:
            new_i = i.rstrip('\n').split(' ')
            words += len(new_i)
            for v in new_i:
                caracters += len(v)
        print(f'El archivo posee {lines} lineas, {words} palabras y {caracters} caracteres')

wc('ejemplo.txt')
#%%
#Ejercicio de otro parcialito 1
def pedidos(filename: str) -> str:
    dic_bebidas = {}
    dic_principal = {}
    dic_postre = {}
    return_str = ''
    with open(filename, 'r') as f:
        for lines in f:
            lista = lines.rstrip('\n').split(', ')
            for i in range(len(lista)):
                if  i == 0 and lista[0] in dic_bebidas:
                    dic_bebidas[lista[0]] += 1
                elif i == 0 and lista[0] not in dic_bebidas:
                    dic_bebidas[lista[0]] = 1
                elif i == 1 and lista[1] in dic_principal:
                    dic_principal[lista[1]] += 1
                elif i == 1 and lista[1] not in dic_principal:  
                    dic_principal[lista[1]] = 1
                elif i == 2 and lista[2] in dic_postre:
                    dic_postre[lista[2]] += 1
                else:
                    dic_postre[lista[2]] = 1
        return_str += 'BEBIDAS:\n'
        for i in dic_bebidas.keys():
            return_str += i + ', ' + str(dic_bebidas[i]) + '\n'
        return_str += '\nPRINCIPAL:\n'
        for v in dic_principal.keys():
            return_str += v + ', ' + str(dic_principal[v]) + '\n'
        if len(dic_postre) == 0:
            return print(return_str)
        else:
            return_str += '\nPOSTRE:\n'
            for c in dic_postre.keys():
                return_str += c + ', ' + str(dic_postre[c]) + '\n'
            return print(return_str)

pedidos('pedidos.txt')
#%%
#Guia de archivos - Ejercicio 7
def grep(filename: str, string: str) -> str:
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if string in line:
                print(line.rstrip('\n'))

grep('ejemplo.txt', 'mi')
#%%
#Guia de archivos - Ejercicio 8
def cat(file1: str, file2: str):
    with open(file1, 'r') as f1:
        lines1 = f1.readlines()
        with open(file2, 'r') as f2:
            lines2 = f2.readlines()
            with open('both_files.txt', 'xt') as f3:
                f3.writelines(lines1)
                f3.writelines(lines2)

cat('ejemplo.txt', 'ejemplo2.txt')

# %%
#Ejercicio 1 - Para pensar de manera recursiva
"""
Una palabra es palíndroma si es capicúa, si leída de izquierda a derecha es igual de
derecha a izquierda.

palindroma(s: str) -> bool
"""
def palindromo(s: str):
    if len(s) == 0 or len(s) == 1:
        return True
    if s[0] == s[-1]:
        return palindromo(s[1:-1])
    else:
        return False
# %%
#Ejercicio 2 - Para pensar de manera recursiva
"""
dardos(n: int) -> bool
Acertar al centro vale 7, en el borde 5. Decir si un puntaje final de un partido de dardos
es válido o no. 

dardos(n: int) -> bool

dardos(5) True, dardos(12) True, dardos(0) True
dardos(8) False, dardos(11) False
"""
def dardos(n: int) -> bool:
    if n == 5 or n == 7:
        return True
    elif n > 5:
        return dardos(n-5) or dardos(n-7)
    else:
        return False
# %%
#Guia de recurcion - Ejercicio 1
def suma_recursiva(z: int, k: int) -> int:
    if k == 0:
        return z
    else:
        return  1 + suma_recursiva(z, k-1)

def mul_recursiva(z: int, k: int) -> int:
    if k == 1:
        return z
    else:
        return z + mul_recursiva(z, k-1)

def exp_recursiva(z: int, k: int) -> int:
    if k == 0:
        return 1
    elif k == 1:
        return z
    else:
        return z * exp_recursiva(z, k-1)
# %%
#Guia de recurcion - Ejercicio 2
def digitos(n: int) -> int:
    if len(str(n)) == 1:
        return 1
    else:
        return 1 + digitos(int(str(n)[:-1]))

digitos(123456)
# %%
#Guia de recurcion - Ejercicio 3
def espejo(n: int) -> int:
    if len(str(n)) == 1:
        return n
    else:
        return int((str(n)[-1]) + str(espejo(int(str(n)[:-1]))))

espejo(1234)
# %%
#Guia de recurcion - Ejercicio 4
def triangular(n: int) -> int:
    if n == 0:
        return 0
    else:
        return n + triangular(n-1)

triangular(5)
# %%
#Ejercicio de recursion del Parcialito 1
def juego(casilleros: int) -> str:
    if casilleros == 1:
        return 1.0
    elif casilleros % 2 == 0:
        return str(casilleros) + ' ' + str(juego((casilleros / 2)))
    else:
        return str(casilleros) + ' ' + str(juego((casilleros + 1)))

juego(104)
# %%
#Ejercicio de mi Parcialito 1
def reg_local(filename: str):
    reg_dic = {}
    return_str = ''
    with open(filename, 'r') as f:
        for lines in f:
            order = lines.rstrip('\n').split(', ')
            if int(order[0]) in (11,12,13,14,15,18,19,20,21,22,23):
                if order[1] in reg_dic:
                    reg_dic[order[1]] += int(order[2])
                else: 
                    reg_dic[order[1]] = int(order[2])
        return_str += 'Productos:\n'
        for i in reg_dic:
            return_str += i + ', ' + str(reg_dic[i]) + '\n'
    return print(return_str)

reg_local('ventas.txt')

# %%
#Ejercicio 1 de otro Parcialito 2
class Jornada(object):
    def __init__(self, nombre, horas, presupuesto, gremio):
        self.nombre = nombre
        self.horas = horas
        self.presupuesto = presupuesto
        self.gremio = gremio
        self.gremios_horas = {}
        self.gremios_presupuesto = {}
        self.registro = {}
        for i in self.gremio:
            self.gremios_horas[i] = self.horas
            self.gremios_presupuesto[i] = self.presupuesto

    def solicitud_de_tareas(self, other):
        if (self.gremios_horas[other.gremio] - other.horas) < 0 or (self.gremios_presupuesto[other.gremio] - other.presupuesto) < 0:
            return False
        else:
            return True
    
    def asignar_tareas(self, other):
        if other.gremio not in self.gremio:
            return 'Este gremio no puede desempeñar este tarea'
        elif self.solicitud_de_tareas(other) == True:
            if other.gremio in self.registro:
                self.registro[other.gremio] += [(other.descripcion, other.presupuesto, other.horas)]
            else:
                self.registro[other.gremio] = [(other.descripcion, other.presupuesto, other.horas)]
            self.gremios_horas[other.gremio] -= other.horas
            self.gremios_presupuesto[other.gremio] -= other.horas
        else:
            return 'No se puede realizar esta tarea'

    def vaciar_tareas(self):
        self.registro = {}
        self.gremios_horas = {}
        self.gremios_presupuesto = {}
    
    def __repr__(self):
        presupuesto_total = self.presupuesto * len(self.gremios_horas)
        presupuesto_util = presupuesto_total
        horas_utiles = self.horas
        presupuesto_total = self.presupuesto * len(self.gremios_horas)
        for v in self.gremios_presupuesto:
            presupuesto_util -= self.gremios_presupuesto[v]
        for c in self.gremios_horas:
            horas_utiles -= self.gremios_horas[c]
        return_str = '** Jornada ' + self.nombre + ' **' + '\nPresupuesto ' + str(presupuesto_util) + ' / ' + str(presupuesto_total) + '\n'
        for b in self.registro:
            horas_totales_g = self.horas - self.gremios_horas[b]
            presupuesto_total_g  = presupuesto_total - self.gremios_presupuesto[b] 
            return_str += '\n' + b + ': ' + str(horas_totales_g) + ' horas, $' + str(presupuesto_total_g)
            for v in self.registro[b]:
                return_str += '\n-' + v[0] + ', $' + str(v[1]) + ', ' + str(v[2])
            return_str += '\n'
        return return_str   

class Tarea(object):
    def __init__(self, descripcion, gremio, horas, presupuesto):
        self.descripcion = descripcion
        self.gremio = gremio
        self.horas = horas
        self.presupuesto = presupuesto        

pileta = Jornada('Cocina',8,150,('gardinero','panedero','taxista'))
p2 = Tarea('hacer caca','gardinero', 4, 56 )
p3 = Tarea('hacer pop','taxista', 4, 23)
pileta.asignar_tareas(p2)
pileta.asignar_tareas(p3)
print(pileta.registro)
print(pileta)
# %%
#Ejercicio 1 y 2 de mi Parcialito 2
class Encomienda(object):
    def __init__(self, ID, volumen, peso):
        self.ID = ID
        self.volumen = volumen
        self.peso = peso

class Camioneta(object):
    def __init__(self, nombre, carga_b1, carga_b2, peso):
        self.nombre = nombre 
        self.carga_b1_og = carga_b1
        self.carga_b1 = carga_b1
        self.carga_b2_og = carga_b2
        self.carga_b2 = carga_b2
        self.peso_og = peso
        self.peso = peso
        self.encomiendas_b1 = {}
        self.encomiendas_b2 = {}
    
    def __repr__(self):
        volumen_utilizado = (self.carga_b1_og + self.carga_b2_og) - (self.carga_b1 + self.carga_b2)
        volumen_total = self.carga_b1_og + self.carga_b2_og
        return_str = '** Camioneta ' + self.nombre + ' **' + '\nVolumen ' + str(volumen_utilizado) + ' / ' + str(volumen_total) + '\n\nBaul1 ' + str(len(self.encomiendas_b1)) + ' encomiendas'
        for i in self.encomiendas_b1:
            return_str += '\n-Encomienda ' + i
        return_str += '\n\nBaul2 ' + str(len(self.encomiendas_b2)) + ' encomiendas'
        for v in self.encomiendas_b2:
            return_str += '\n-Encomienda ' + v
        return return_str

    def ver_si_entra(self, other):
        if self.peso < other.peso or (self.carga_b1 < other.volumen and self.carga_b2 < other.volumen):
            return False 
        else:
            return True
        
    def cargar_encomienda(self, other):
        if self.ver_si_entra(other) == True:
            if self.carga_b1 >= self.carga_b2:
                self.encomiendas_b1[other.ID] = (other.volumen, other.peso)
                self.carga_b1 -= other.volumen
                self.peso -= other.peso
            else:
                self.encomiendas_b2[other.ID] = (other.volumen, other.peso)
                self.carga_b2 -= other.volumen
                self.peso -= other.peso
        else:
            return False

    def sacar_encomienda(self, other):
        if other.ID in self.encomiendas_b1:
            self.carga_b1 += self.encomiendas_b1[other.ID][0]
            self.peso += self.encomiendas_b1[other.ID][1]
            del self.encomiendas_b1[other.ID]
        
        elif other.ID in self.encomiendas_b2:
            self.carga_b1 += self.encomiendas_b2[other.ID][0]
            self.peso += self.encomiendas_b2[other.ID][1]
            del self.encomiendas_b2[other.ID]
        
        else:
            return print('La encomienda que esta buscando no se encuentra cargada')

    def vaciar_camioneta(self):
        self.carga_b1 = self.carga_b1_og 
        self.carga_b2 = self.carga_b2_og
        self.peso = self.peso_og
        self.encomiendas_b1 = {}
        self.encomiendas_b2 = {}

    def plan_viajes(self, filename):
        enco_dic = {}
        enco_list = []
        final_enco_dic = {}
        viajes = 'Viejes 1:'
        viaje = 1
        with open(filename, 'r') as f:
            for lines in f:
                new_line = lines.rstrip('\n').split(', ')
                enco_dic[new_line[1]] = (int(new_line[2]), int(new_line[3]))
                enco_list.append(int(new_line[2]))
            enco_list.sort(reverse=True)
            for i in enco_list:
                for v in enco_dic:
                    if i == enco_dic[v][0] and (v not in final_enco_dic):
                        final_enco_dic[v] = enco_dic[v]
            for c in final_enco_dic:
                i = Encomienda(c, final_enco_dic[c][0], final_enco_dic[c][1])
                if self.ver_si_entra(i) == True:
                    self.cargar_encomienda(i)
                    viajes += '\n' + c
                else:
                    viaje += 1
                    viajes += '\n\nViajes ' + str(viaje)
                    viajes += '\n' + c
                    self.vaciar_camioneta
        return print(viajes)

camioneta = Camioneta('Kangoo', 800, 2000, 650)
camioneta.plan_viajes('martes.txt')             
# %%
#Guia de recursividad - Ejercicio 6
def vector(vec: list) -> int:
    if len(vec) == 1:
        return vec[0]
    elif vec[0] >= vec[-1]:
        return vector(vec[:-1])
    else:
        return vector(vec[1:])
# %%
#Recursive Selction Sort
def rec_ord(lista):
    if len(lista) == 1:
        return lista
    else:
        maximo = max(lista)
        lista.remove(maximo)
        return [maximo] + rec_ord(lista)

rec_ord([1,3,6,9,4])
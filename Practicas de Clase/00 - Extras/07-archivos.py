#%% Ejercicio 1


def less(archivo: str):
    with open(archivo, 'rt', newline = '\n') as file:
        print(file.read())


less('text.txt')


#%% Ejercicio 2


def head(archivo: str, n: int):
    with open(archivo, 'rt', newline = '\n') as file:
        for line in range(n):
            print(file.readline(), end = '')


head('text.txt', 8)


#%% Ejercicio 3


def tail(archivo: str, n: int):
    with open(archivo, 'rt', newline = '\n') as file:
        lines = file.readlines()
        for i in range(len(lines) - n, len(lines)):
            print(lines[i], end = '')


tail('text.txt', 3)


#%% Ejercicio 4


def touch(file_name: str):
    try:
        file = open(file_name, 'xt')
        file.close
        return f'The file "{file_name}" was created successfully.'
    except FileExistsError:
        return f'The file "{file_name}" already exists.'


print(touch('file.txt'))


#%% Ejercicio 5


def cp(archivo_1: str):
    with open(archivo_1, 'rt', newline = '\n') as file:
        with open(f'copy_{archivo_1}', 'xt', newline = '\n') as file_2:
            file_2.writelines(file.readlines())
    

cp('text.txt')
            

#%% Ejercicio 6


def wc(archivo: str) -> str:
    words = characters = []
    with open(archivo, 'rt', newline = '\n') as file:
        lines = file.readlines()
        for line in lines:
            words.extend(line.rstrip('\r\n').split(' '))
        characters = ''.join(words)
        print(f'Nombre: "{file.name}"\nLíneas: {len(lines)}\nPalabras: {len(words)}\nCaracteres: {len(characters)}')


wc('text.txt')


#%% Ejercicio 7


def grep(archivo: str, string: str) -> str:
    with open(archivo, 'rt', newline = '\n') as file:
        lines = file.readlines()
        for line in lines:
            if string in line:
                print(line.rstrip('\r\n'))


grep('text.txt', 'Aristoteles')


#%% Ejercicio 8


def cat(archivo_1: str, archivo_2: str):
    try:
        with open(archivo_1, 'rt', newline = '\n') as file, open(archivo_2, 'rt', newline = '\n') as file_2, open(f'{archivo_1}_{archivo_2}', 'xt', newline = '\n') as file_3:
            file_3.write(f'{file.read()}\n{file_2.read()}')
    except FileExistsError:
        print(f'The file {archivo_1}_{archivo_2} already exists.')
        

cat('text.txt', 'copy_text.txt')


#%% Ejercicio 9


from string import ascii_lowercase as abc, punctuation


def rot13(archivo_og: str, archivo_dt: str):
    with open(archivo_og, 'rt', newline = '\r\n') as file_og, open(archivo_dt, 'wt', newline = '\r\n') as file_dt:
        line = file_og.readline().rstrip('\r\n')
        while line != '':
            for character in line:
                if character.lower() in abc:
                    file_dt.write(abc[(abc.find(character.lower()) + 13) % 26])
                else:
                    file_dt.write(character.lower())
            file_dt.write('\n')
            line = file_og.readline().rstrip('\r\n')


def rot13_(archivo: str, archivo_: str):
    with open(archivo, 'rt', newline = '\r\n') as file, open(archivo_, 'wt', newline = '\r\n') as file_:
        line = file.readline().rstrip('\r\n')
        while line != '':
            for character in line:
                if character.lower() in abc:
                    file_.write(abc[(abc.find(character.lower()) + 13) % 26])
                else:
                    file_.write(character)
            file_.write('\n')
            line = file.readline().rstrip('\r\n')


rot13('text.txt', 'destiny.txt')
rot13_('destiny.txt', 'destiny_.txt')


#%% Ejercicio 10


def load_data(archivo: str) -> dict:
    data = {}
    with open(archivo, 'rt', newline = '\r\n') as file:
        for line in file:
            if line != '\r\n':
                item = line.rstrip('\r\n').split(':')
                data[item[0]] = item[1]
    return data


print(load_data('diccionario.txt'))


#%% Ejercicio 11


def save_data(diccionario: dict):
    if diccionario != {}:
        with open('diccionario.txt', 'wt', newline = '\n') as file:
            for key, value in diccionario.items():
                file.write(f'{key}:{value}\n')

save_data({'1':'hola', '2':'chau', 'papa':'hijo', 'mama':'hija', 'queso':'jamon', 'arbol':'planta', 'benja':'queso', 'utopia':'moro'})


#%% Ejercicio 12

def sed(archivo: str, str1: str, str2: str):
    with open(archivo, 'rt', newline = '\n') as file:
        text_to_write = file.read().replace(str2, str1)

    with open(archivo, 'wt', newline = '\n') as file:
        file.write(text_to_write)


sed('text.txt', 'Aristoteles', 'Platon')


#%% Ejercicio 13


def csv(datos: list[list]):
    with open('datos.csv', 'at', newline = '\n') as f:
        for lista in datos:
            f.write(f'{",".join(lista)}\n')


csv([
["First Name","Last Name","Country","Date of Birth"],
["Emanuel","Ginobili","Argentina","1977"],
["Donald","Trump","USA","1946"],
["Carl","Gauss","Germany","1855"]
])


#%% Ejercicio 14


def csv(datos: list[list]):
    with open('datos.tsv', 'at', newline = '\n') as f:
        for lista in datos:
            f.write(f'{f"{chr(9)}".join(lista)}\n')


csv([
["First Name","Last Name","Country","Date of Birth"],
["Emanuel","Ginobili","Argentina","1977"],
["Donald","Trump","USA","1946"],
["Carl","Gauss","Germany","1855"]
])


#%% Ejercicio 15

from string import punctuation as p

def script(archivo: str):
    with open(archivo, 'rt', newline = '\n') as f:
        text = archivo.read()
        new_text = ''
        for character in text:
            if not character in p:
                new_text += character 
        

                
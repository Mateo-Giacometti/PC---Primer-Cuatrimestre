'''
Escriba una función, llamada tail, que reciba un archivo y un número N e imprima las últimas
N líneas del archivo.
'''
#%%
def tail(filename, num_line):
    with open(filename, 'r') as f:
        line = f.readlines()
        for i in range(num_line,len(line)):
            print(line[i])
            

def main():
    tail('Text',2)

if __name__ == '__main__':
    main()

'''
Escriba una función, llamada less, que reciba un archivo e imprima el contenido del archivo
'''
def less(Text):
    with open(Text, 'r') as f:
        for line in f:
            print(line)

def main():
    less('Text')

if __name__ == '__main__':
    main()

    
    
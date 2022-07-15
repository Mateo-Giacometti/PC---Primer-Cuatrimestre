'''
Escriba una función, llamada head, que reciba un archivo y un número N e imprima las
primeras N líneas del archivo
''' 
def head(filename, num_lines):
    with open(filename, 'r') as f:
        for i in range(num_lines):
            print(f.readline())
            
def main():
    head('Text',4)

if __name__ == '__main__':
    main()

    
    
'''
Hoy trabgajo con el puto de Bryan
'''
def less(Text):
    provincias = []
    final = {}
    with open(Text, 'r') as f:
        l = f.readline()
        while l:
            prov = l.split(',')[2]
            provincias.append(prov)
            f.readline()
        for persona in provincias:
                for i in range(len(provincias)):
                    repete = 1
                    if provincias[i] == persona:
                        repete += 1
                final[persona].append(repete)
        print(final)    

def main():
    less('Text')

if __name__ == '__main__':
    main()
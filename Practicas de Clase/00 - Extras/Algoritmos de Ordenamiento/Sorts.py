l = [27, 12, 12, 4, 13,65,4,765,6,3,5,3,1]
 
def bubble_sort(seq):
    ordenada = False
    j = 1
    while not ordenada:
        ordenada = True
        for i in range(len(seq)-j):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i] #ordenamiento in place
                ordenada = False
        j += 1
    return seq

def selection_sort(seq):
    j = 0
    while j != len(seq)-1:
        v = seq[j]
        x = j
        for i in range(j, len(seq)-1):
            if v > seq[i+1]:
                v = seq[i+1]
                x = i+1
        seq[j], seq[x] = seq[x], seq[j]
        j += 1
    return seq

def sort(seq):
    if len(seq) == 1:
        return seq
    elif len(seq) == 2:
        if seq[0] > seq[1]:
            seq[0], seq[1] = seq[1], seq[0]
        return seq
    l = len(seq)//2
    return merge(sort(seq[:l]), sort(seq[l:]))
    
def merge(seq1, seq2):
    r = []
    i = 0
    j = 0
    while i<len(seq1) and j<len(seq2):
        if seq1[i] < seq2[j]:
            r.append(seq1[i])
            i+= 1
        else:
            r.append(seq2[j])
            j += 1
    while i <len(seq1):
        r.append(seq1[i])
        i+=1
    while j<len(seq2):
        r.append(seq2[j])
        j+=1
    return r
    """dadas dos secuencias, las ordena"""
                 
print(l)
print(selection_sort(l))
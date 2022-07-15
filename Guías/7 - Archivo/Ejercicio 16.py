'''
Dado dos archivos en formato CSV, dinosaurs1.csv y dinosaurs2.csv, escribir un
programa que lea los dos archivos guardados en disco, y luego imprima los nombres de los
dinosaurios bípedos, desde el más lento al más rápido.
'''
import math

def dinosaurios(file1,file2):
    with open(file1,'r') as f1, open(file2,'r') as f2:
        lista = []
        for line in f1:
            lista.append((line.split(','))[0:2])
    return lista 
        
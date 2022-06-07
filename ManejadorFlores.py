import csv
import numpy as np
from Flor import Flor


class ManejadorF:
    __flores = None
    __cantidad = 0
    __dimension = 0
    __incremento = 0

    def __init__(self, dimension, incremento=5):
        self.__flores = np.empty(dimension, dtype=Flor)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento

    def __str__(self):
        s = ' '
        for lista in self.__flores:
            s += str(lista) + ' '
        return s

    def cargarArchivo(self):
        archivo = open('flores.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                '''saltear cabecera '''
                bandera = not bandera
            else:
                unaFlor = Flor(fila[0], fila[1], fila[2], fila[3])
                self.agregarFlor(unaFlor)
        archivo.close()

    def agregarFlor(self, unaFlor):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__flores.resize(self.__dimension)
        self.__flores[self.__cantidad] = unaFlor
        self.__cantidad += 1

    def longitudArreglo(self):
        return len(self.__flores)

    def buscarFlor(self, n):
        return self.__flores[n-1]

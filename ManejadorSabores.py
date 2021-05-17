import csv
from ClaseSabor import Sabor

class ManejadorS:

    __listaSabores = []

    def __init__(self):
        self.__listaSabores = []

    def __str__(self):
        s = ""
        for lista in self.__listaSabores:
            s += str(lista) + ''
        return s

    def agregarSabor(self, unSabor):
        self.__listaSabores.append(unSabor)

    def cargarSabores(self):
        archivo = open('Sabores.csv')
        reader = csv.reader(archivo,delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                '''saltear cabecera '''
                bandera = not bandera
            else:
              numero = fila[0]
              nombre = fila[1]
              descripcion = fila[2]
              unSabor = Sabor(numero, nombre, descripcion)
              self.agregarSabor(unSabor)
        archivo.close()

    def buscarSabor(self, n):
        for indice, Sabor in enumerate(self.__listaSabores):
            if int(Sabor.getNumero()) == int(n):
                return self.__listaSabores[indice]

    def getLista(self):
        return self.__listaSabores
from ClaseSabor import Sabor

class Helado:

    __gramos = 0
    __sabores = []

    def __init__(self, gramos = 0):
        self.__gramos = gramos
        self.__sabores = []

    def __str__(self):
        cadena =  '\nPeso: {}g\n'.format(self.__gramos)

        for s in self.__sabores:
            cadena += str(s)

        return cadena

    def getGramos(self):
        return self.__gramos

    def setGramos(self, peso):
        self.__gramos = peso

    def getSabores(self):
        return self.__sabores

    def agregarSabor(self,unSabor):
        self.__sabores.append(unSabor)
class Ramo:
    __tamaño = ''
    __flores = []

    def __init__(self, tamaño=''):
        self.__tamaño = tamaño
        self.__flores = []

    def __str__(self):
        s = '\nTamaño del Ramo: {}\n'.format(self.__tamaño)
        for lista in self.__flores:
            s += str(lista)
        return s

    def agregarFlor(self, unaFlor):
        self.__flores.append(unaFlor)

    def getTamaño(self):
        return self.__tamaño

    def setTamaño(self, tamaño):
        self.__tamaño = tamaño

    def getFlores(self):
        return self.__flores

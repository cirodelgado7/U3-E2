from Ramo import Ramo


class ManejadorR:
    __listaRamos = []

    def __init__(self):
        self.__listaRamos = []

    def __str__(self):
        s = "\n***** Ramos Vendidos *****"
        for lista in self.__listaRamos:
            s += str(lista)
        return s + ' '

    def registrarVenta(self, mf, c):
        unRamo = Ramo()
        if c == 1 or c == 2:
            unRamo = Ramo('Chico')
        elif c == 3 or c == 4:
            unRamo = Ramo('Mediano')
        else:
            if c == 5 or c == 6:
                unRamo = Ramo('Grande')
        i = 0
        while i < c:
            s = int(input('Número de Flor {}: '.format(i + 1)))
            flor = mf.buscarFlor(s)
            print(flor)
            unRamo.agregarFlor(flor)
            i += 1
        self.__listaRamos.append(unRamo)

    def masPedidas(self, mf):
        lista = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for ramo in self.__listaRamos:
            listaFlores = ramo.getFlores()
            for flor in listaFlores:
                n = int(flor.getNumero())
                lista[n - 1] += 1
        i = 0
        while max(lista) != 0 and i < 5:
            m = lista.index(max(lista))
            lista[m] = 0
            flor = mf.buscarFlor(m + 1)
            print(flor.getNombre())
            i += 1

    def masVendidas(self, t):
        for ramo in self.__listaRamos:
            if ramo.getTamaño() == t:
                listaFlores = ramo.getFlores()
                for flor in listaFlores:
                    nombre = flor.getNombre()
                    print(nombre)

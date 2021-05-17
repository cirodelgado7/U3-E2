from ClaseHelado import Helado
from ClaseSabor import Sabor

class ManejadorH:

    __listaHelados = []

    def __init__(self):
        self.__listaHelados = []

    def __str__(self):
        s = "\n***** Helado Vendido *****\n"
        for lista in self.__listaHelados:
            s += str(lista) + '\n'
        return s

    def registrarPedido(self, ms):
        peso = input('\nTipo de helado (100g - 150g - 250g - 500g - 1000g): ')
        unHelado = Helado(peso)
        print(ms)
        print('Puede elegir desde 1 hasta 4 sabores')
        k = int(input('¿Cuántos sabores desea elegir?: '))
        i = 0
        while i < k:
            s = input('Sabor {}: '.format(i+1))
            sabor = ms.buscarSabor(s)
            print(sabor)
            unHelado.agregarSabor(sabor)
            i += 1
        self.__listaHelados.append(unHelado)

    def mostrarMasPedidos(self, ms):
        print('\n ***** Sabores más pedidos *****\n')
        lista = [0,0,0,0,0,0,0,0,0,0]
        for helado in self.__listaHelados:
            listaSabores = helado.getSabores()
            for sabor in listaSabores:
                n = int(sabor.getNumero())
                lista[n - 1] += 1
        for i in range(0,6):
            while max(lista) != 0:
                m = lista.index(max(lista))
                lista[m] = 0
                sabor = ms.buscarSabor(m+1)
                print(sabor)

    def estimarGramosVendidos(self, ms):
        print(ms)
        acum = 0.0
        num = int(input('Numero de Sabor: '))
        for helado in self.__listaHelados:
            listaSabores = helado.getSabores()
            for sabor in listaSabores:
                n = int(sabor.getNumero())
                if num == n:
                    acum += float(helado.getGramos())/float(len(listaSabores))
        print('La cantidad de Gramos vendidos es: {}'.format(acum))

    def consultarSabores(self):
        g = int(input('\nTipo de helado (100g - 150g - 250g - 500g - 1000g): '))
        for helado in self.__listaHelados:
            if int(helado.getGramos()) == g:
                listaSabores = helado.getSabores()
                for sabor in listaSabores:
                    print(sabor)
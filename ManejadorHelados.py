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
        print('\n***** Listado de Sabores Disponibles *****')
        print(ms)
        print("\n***** 1. Registrar un helado vendido *****")
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
        print('\n***** 2. Mostrar 5 sabores mas pedidos *****')
        lista = [0,0,0,0,0,0,0,0,0,0]
        for helado in self.__listaHelados:
            listaSabores = helado.getSabores()
            for sabor in listaSabores:
                n = int(sabor.getNumero())
                lista[n - 1] += 1
        i = 0
        while max(lista) != 0 and i < 5:
            m = lista.index(max(lista))
            lista[m] = 0
            sabor = ms.buscarSabor(m+1)
            print(sabor.getNombre())
            i += 1

    def estimarGramosVendidos(self, ms):
        print('\n***** 3. Consultar gramos vendidos por sabor *****')
        acum = 0.0
        num = int(input('Numero de Sabor: '))
        for helado in self.__listaHelados:
            listaSabores = helado.getSabores()
            for sabor in listaSabores:
                n = int(sabor.getNumero())
                if num == n:
                    acum += float(helado.getGramos())/float(len(listaSabores))
        print('La cantidad de gramos vendidos es: {}'.format(acum))

    def consultarSabores(self):
        print('\n***** 4. Consultar sabores vendidos por tipo de helado *****')
        g = int(input('\nTipo de helado (100g - 150g - 250g - 500g - 1000g): '))
        for helado in self.__listaHelados:
            if int(helado.getGramos()) == g:
                listaSabores = helado.getSabores()
                for sabor in listaSabores:
                    nombre = sabor.getNombre()
                    print(nombre)

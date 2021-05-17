class Menu:

    __switcher = None

    def __init__(self):
        self.__switcher = {
            1: self.opcion1,
            2: self.opcion2,
            3: self.opcion3,
            4: self.opcion4,
            5: self.salir
            }

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op, mh, ms):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func(mh, ms)

    def opcion1(self, mh, ms):
        mh.registrarPedido(ms)

    def opcion2(self, mh, ms):
        mh.mostrarMasPedidos(ms)

    def opcion3(self, mh, ms):
        mh.estimarGramosVendidos(ms)

    def opcion4(self, mh, ms):
        mh.consultarSabores()

    def salir(self, mh, ms):
        print('Salir')

    def mostrarMenu(self, mh, ms):
        salir = False
        while not salir:
            print("\n---------Heladeria---------")
            print("------------Menu------------\n"
                  "1. Registrar un helado vendido"
                  "\n2. Mostrar 5 sabores mas pedidos"
                  "\n3. Consultar gramos vendidos por sabor"
                  "\n4. Consultar sabores vendidos por tipo de helado"
                  "\n5. Salir")
            op = int(input('Ingrese una opcion: '))
            if op in range(1, 6) and type(op) is not str:
                self.opcion(op, mh, ms)
                salir = op == 5
            else:
                print('La opción ingresada no es valida. Ingrese una opción válida')
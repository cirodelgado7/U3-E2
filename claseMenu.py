class Menu:

    __switcher = None

    def __init__(self):
        self.__switcher = {
            1: self.opcion1,
            2: self.opcion2,
            3: self.opcion3,
            4: self.salir
            }

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op, mf, mr):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func(mf, mr)

    def opciones(self, mf, mr):
        salir = False
        while not salir:
            print("\n----------Floreria----------")
            print("------------Menu------------\n"
                  "\n1. Registrar venta"
                  "\n2. Mostrar las 5 flores mas vendidas"
                  "\n3. Mostrar las flores más vendidas por tipo de ramo"
                  "\n4. Salir")
            op = int(input('Ingrese una opcion: '))
            if op in range(1, 5) and type(op) is not str:
                self.opcion(op, mf, mr)
                salir = op == 4
            else:
                print('La opción ingresada no es valida. Ingrese una opción válida')

    def opcion1(self, mf, mr):
        print('\n***** Listado de Flores Disponibles *****')
        print('Número\t\tNombre\t\tColor\t\tDescripción')
        print(mf)
        print("\n***** 1. Registrar venta de ramo *****")
        print('Puede agregar desde 1 hasta 6 flores')
        c = int(input('¿Cuántas flores desea agregar?: '))
        mr.registrarVenta(mf, c)

    def opcion2(self, mf, mr):
        print('\n***** 2. Mostrar 5 flores mas pedidas *****')
        mr.masPedidas(mf)

    def opcion3(self, mf, mr):
        print('\n***** 4. Consultar flores más vendidas por tipo de ramo *****')
        t = input('\nTipo de ramo (Chico - Mediano - Grande): ')
        mr.masVendidas(t)

    def salir(self, mf, mr):
        print('Salir')


from ManejadorFlores import ManejadorF
from ManejadorRamos import ManejadorR
from claseMenu import Menu


if __name__ == '__main__':
    mf = ManejadorF(10)
    mr = ManejadorR()
    mf.cargarArchivo()
    menu = Menu()
    menu.opciones(mf, mr)

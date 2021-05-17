from ManejadorHelados import ManejadorH
from ManejadorSabores import ManejadorS
from MenuHeladeria import Menu

if __name__ == '__main__':
    mh = ManejadorH()
    ms = ManejadorS()
    ms.cargarSabores()
    menu = Menu()
    menu.mostrarMenu(mh,ms)
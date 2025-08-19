from Pokemon_Game import game
from Pokemon_Inventario import Jugador 
from Pokemon_Tienda import tienda

import os
import time

global salir

mi_jugador = Jugador()


def menu():
    while True:
        os.system("cls")
        print("Capturar Pokemon (0): ")
        print("Ver Inventario (1): ")
        print("Tienda (2): ")
        Menu = int(input("Seleciones Una Opcion: "))
        if Menu==0:
            return game(menu,mi_jugador)
        elif Menu==1:
            Jugador.mostrar_inventario(mi_jugador)
            input("Salir")
            continue
        elif Menu==2:
            return tienda(menu,mi_jugador)
        else:
            print("no se puede we: ")
            time.sleep(1)
            continue



menu()
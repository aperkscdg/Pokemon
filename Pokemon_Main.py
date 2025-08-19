from Pokemon_Game import game
from Pokemon_Inventario import Jugador 

import os
import time


mi_jugador = Jugador()

def menu():
    while True:
        os.system("cls")
        print("Capturar Pokemon (0): ")
        print("Ver Inventario (1): ")
        Menu = int(input("Seleciones Una Opcion: "))
        if Menu==0:
            return game(menu,mi_jugador)
        elif Menu==1:
            return Jugador.mostrar_inventario(mi_jugador)
        else:
            print("no se puede we: ")
            time.sleep(1)
            continue

menu()
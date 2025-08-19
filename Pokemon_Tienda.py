import os
import time
import random
def tienda(menu,mi_jugador):
    os.system("cls")
    mi_jugador.imprimir_dinero()
    print("=================")
    print("Comprar Pokeball Normal: $5 (0)")
    print("Comprar Greatball: $25 (1)")
    print("Comprar Ultraball: $50 (2)")
    print("Comprar Masterball: $100 (3)")
    respuesta = int(input("Que vas A hacer?"))
    

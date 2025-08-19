import Pokemon_Game
import Pokemon_Inventario
import os
import time
def menu():
    while True:
        os.system("cls")
        print("Capturar Pokemon (0): ")
        print("Ver Inventario (1): ")
        Menu = int(input("Seleciones Una Opcion: "))
        if Menu==0:
            return "Sex"
        elif Menu==1:
            return Pokemon_Inventario.Inventario()
        else:
            print("no se puede we: ")
            time.sleep(1)
            continue

menu()
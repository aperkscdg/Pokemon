import os 
import time
def Inventario():
    os.system("cls")
    class Jugador:
        def __init__(self, dinero=500, pokemones=None, items=None, pokebolas=None):
            self.dinero = dinero
            self.pokemones = pokemones if pokemones is not None else []
            self.items = items if items is not None else []
            self.pokebolas = pokebolas if pokebolas is not None else []
        def mostrar_inventario(self):
            print("=== Inventario ===")
            print(f"Dinero: ${self.dinero}")
            print("Pokemones:", ", ".join(self.pokemones) if self.pokemones else "Ninguno")
            print("Items:", ", ".join(self.items) if self.items else "Ninguno")
            print("Pokébolas:", ", ".join(self.pokebolas) if self.pokebolas else "Ninguna")
            print("=================")
    jugador = Jugador()
    Jugador.mostrar_inventario(jugador)



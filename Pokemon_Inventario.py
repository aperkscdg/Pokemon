import os
import json
class Jugador:
    def __init__(self, dinero=500, pokemones=None, items=None, pokebolas=None):
        self.dinero = dinero
        self.pokemones = pokemones if pokemones is not None else []
        self.items = items if items is not None else []
        self.pokebolas = pokebolas if pokebolas is not None else []
    def mostrar_inventario(self):
        os.system("cls")
        print("=== Inventario ===")
        print(f"Dinero: ${self.dinero}")
        print("Pokemones:", ", ".join(self.pokemones) if self.pokemones else "Ninguno")
        print("Items:", ", ".join(self.items) if self.items else "Ninguno")
        print("Pokébolas:", ", ".join(self.pokebolas) if self.pokebolas else "Ninguna")
        print("=================")
    def agregar_pokemon(self, pokemones):
        self.pokemones.append(pokemones)
    def imprimir_dinero(self):
        print(f"Dinero: ${self.dinero}")
        #DATOSSSSSSSS
    def guardar(self, archivo="inventario.json"):
        with open(archivo, "w") as f:
            json.dump({
                "dinero": self.dinero,
                "pokemones": self.pokemones,
                "items": self.items,
                "pokebolas": self.pokebolas
            }, f)
        print("Juego guardado correctamente.")
    # Cargar desde archivo JSON
    def cargar(self, archivo="inventario.json"):
        try:
            with open(archivo, "r") as f:
                datos = json.load(f)
                self.dinero = datos.get("dinero", 500)
                self.pokemones = datos.get("pokemones", [])
                self.items = datos.get("items", [])
                self.pokebolas = datos.get("pokebolas", [])
            print("Juego cargado correctamente.")
        except FileNotFoundError:
            print("No se encontró archivo de guardado. Se iniciará un juego nuevo.")

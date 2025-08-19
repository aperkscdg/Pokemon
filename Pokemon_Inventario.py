import os
import json
class Jugador:
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
        if self.pokemones:
            print("Pokemones:")
            for p in self.pokemones:
                print(f"- {p['nombre']} | Vida: {p['vida']} | Daño: {p['daño']} | Defensa: {p['defensa']} | Valor: ${p['costo_venta']}")
        else:
            print("Pokemones: Ninguno")
        print("Items:", ", ".join(self.items) if self.items else "Ninguno")
        print("Pokébolas:", ", ".join(self.pokebolas) if self.pokebolas else "Ninguna")
        print("=================")
        input("Presiona ENTER para volver al menú...")

    def agregar_pokemon(self, pokemon_data):
        self.pokemones.append(pokemon_data)
        print(f"{pokemon_data['nombre']} se agregó a tu inventario.")

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

import os 
import time
import random
import json

from attr import s

with open("pokemones_stats.json", "r", encoding="utf-8") as f:
    pokemon_data = json.load(f)

pokemon_list = [p["nombre"] for p in pokemon_data]

def game(menu,mi_jugador):
    def nuevo(pokemon_nuevo):
        stats = next((p for p in pokemon_data if p["nombre"] == pokemon_nuevo), None)
        os.system("cls")
        if random.randint(0,100) <= 100:
            shiny = stats.copy()
            shiny["nombre"] += " ⭐"
            shiny["calidad"] = "shiny"
            # Multiplica los stats por 2 si es shiny
            for key in ["vida", "daño", "defensa", "costo_venta"]:
                if key in shiny and isinstance(shiny[key], (int, float)):
                    shiny[key] = shiny[key] * 2
            mi_jugador.agregar_pokemon(shiny)
            mi_jugador.guardar()
            print("Ahora tienes un:", shiny["nombre"])
            time.sleep(2)
            menu()
        else:
            stats_normal = stats.copy()
            stats_normal["tipo_captura"] = "normal"
            mi_jugador.agregar_pokemon(stats_normal)
            mi_jugador.guardar()
            print("Ahora tienes un:", stats_normal["nombre"])
            time.sleep(2)
            menu()
    def ruleta():
        if len(mi_jugador.pokebolas) == 0:
            os.system("cls")
            print("No Tienes Pokebolas")
            time.sleep(2)
            menu()
        else:
            while True:
                max_pokebola = len(mi_jugador.pokebolas)
                # Primero muestra las opciones
                for index, pokebola in enumerate(mi_jugador.pokebolas):
                    print(f"{index+1}: {pokebola}")
                # Luego pide la respuesta
                respuesta = int(input(f"¿Cuál Pokebola vas a usar? (1 a {max_pokebola}): "))
                if respuesta < 1 or respuesta > max_pokebola:
                    os.system("cls")
                    print("No tienes esa cantidad de pokebolas.")
                    input("Continuar")
                    continue
                uso_pokebolas = mi_jugador.pokebolas[respuesta - 1]
                mi_jugador.pokebolas.pop(respuesta - 1)
                frases_permitidas = ["Pokeball Normal", "Greatball", "Ultraball", "Masterball"]
                solo_permitidas = all(pokebola in frases_permitidas for pokebola in mi_jugador.pokebolas)
                if solo_permitidas:
                    os.system("cls")
                    cantidad = 0
                    Max = random.randint(2, 50)
                    while True:
                        os.system("cls")
                        pokemon_nuevo = random.choice(pokemon_list)
                        print(pokemon_nuevo)
                        time.sleep(0.1)
                        cantidad += 1
                        if cantidad == Max:
                            nuevo(pokemon_nuevo)
                            break
                else:
                    print("ACABAS DE PONER OTRA COSA???????")
    ruleta()
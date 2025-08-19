import os 
import time
import random
import json

pokemon_list = [
    "Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard",
    "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree",
    "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot",
    "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok",
    "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidoran♀", "Nidorina",
    "Nidoqueen", "Nidoran♂", "Nidorino", "Nidoking", "Clefairy", "Clefable",
    "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat",
    "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat",
    "Venomoth", "Diglett", "Dugtrio", "Meowth", "Persian", "Psyduck",
    "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag",
    "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop",
    "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel" "Tentacool",
    "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash",
    "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetch'd", "Doduo",
    "Dodrio", "Seel", "Dewgong", "Grimer", "Muk", "Shellder",
    "Cloyster", "Gastly", "Haunter", "Gengar", "Onix", "Drowzee",
    "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute",
    "Exeggutor", "Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung",
    "Koffing", "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela",
    "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu",
    "Starmie", "Mr. Mime", "Scyther", "Jynx", "Electabuzz", "Magmar",
    "Pinsir", "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto",
    "Eevee", "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte",
    "Omastar", "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno",
    "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mew"
]

def game(menu,mi_jugador):
    def nuevo(pokemon_nuevo):
        with open("pokemones_stats.json", "r") as file:
            pokemon_data = json.load(file)
        os.system("cls")
        if random.randint(0,100) <= 5:
            mi_jugador.agregar_pokemon(pokemon_nuevo + " " + "(Shiny)")
            mi_jugador.guardar()
            print("Ahora tienes Un:", pokemon_nuevo + " " + "(Shiny)")
            time.sleep(2)
            menu()
        else:
            mi_jugador.agregar_pokemon(pokemon_nuevo)
            mi_jugador.guardar()
            print("Ahora Tienes Un: ", pokemon_nuevo)
            time.sleep(2)
            menu()
    def ruleta():
        if len(mi_jugador.pokebolas)==0:
            os.system("cls")
            print("No Tienes Pokebolas")
            time.sleep(2)
            menu()
        else:
            while True:
                max_pokebola=len(mi_jugador.pokebolas)
                for index, pokemon in enumerate(mi_jugador.pokebolas):
                    print(f"{index+1}: {pokemon}")
                respuesta = int(input("Cual Pokebola vas A usar? : "))
                if respuesta < 1 or respuesta > max_pokebola:
                    os.system("cls")
                    print("No tienes esa cantidad de pokebolas: ")
                    input("Continuar")
                    continue
                else:
                    uso_pokebolas=mi_jugador.pokebolas[respuesta]
                    mi_jugador.pokebolas.pop(respuesta-1)
                    frases_permitidas = ["Pokeball Normal", "Greatball", "Ultraball", "Masterball"]
                    solo_permitidas = all(pokebola in frases_permitidas for pokebola in mi_jugador.pokebolas)
                    if solo_permitidas:
                        os.system("cls")
                        cantidad = 0
                        Max=random.randint(2,50)
                        while True:
                            os.system("cls")
                            pokemon_nuevo=random.choice(pokemon_list)
                            print(pokemon_nuevo)
                            time.sleep(0.1)
                            cantidad+=1
                            if cantidad == Max:
                                nuevo(pokemon_nuevo)
                                break
                    else:
                        print("ACABAS DE PONER OTRA COSA???????")
    ruleta()
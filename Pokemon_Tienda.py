import os
import time
import random

def tienda(menu,mi_jugador):
    paginas=0
    mi_jugador.imprimir_dinero()
    while paginas==0:
        os.system("cls")
        dinero=mi_jugador.dinero
        print("=================")
        print("Comprar Pokeball Normal: $5 (0)")
        print("Comprar Greatball: $25 (1)")
        print("Comprar Ultraball: $50 (2)")
        print("Comprar Masterball: $100 (3)")
        print("Mas Opciones (4): ")
        print("Salir de La tienda (5): ")
        respuesta = int(input("Que vas A hacer?: "))
        if respuesta==0:
            if dinero >=5:
                dinero-=5
                mi_jugador.dinero = dinero
                mi_jugador.pokebolas.append("Pokeball Normal")
                mi_jugador.guardar()
                print("Compraste Una Pokeball Normal Gracias!!! :D Roblitox Te lo agredece")
                input("Continuar")
                continue
            else:
                print("No Tienes Dinero Para Comprar este Item")
                input("Continuar")
                continue
        elif respuesta ==1:
            if dinero >=25:
                dinero-=25
                mi_jugador.dinero = dinero
                mi_jugador.pokebolas.append("Greatball")
                mi_jugador.guardar()
                print("Compraste Una Greatbal Gracias!!! :D Roblitox Te lo agredece")
                input("Continuar")
                continue
            else:
                print("No Tienes Dinero Para Comprar este Item")
                input("Continuar")
        elif respuesta == 2:
                if dinero >= 50:
                    dinero -= 50
                    mi_jugador.dinero = dinero
                    mi_jugador.pokebolas.append("Ultraball")
                    mi_jugador.guardar()
                    print("Compraste Una Ultraball Gracias!!! :D Roblitox Te lo agradece")
                    input("Continuar")
                    continue
                else:
                    print("No Tienes Dinero Para Comprar este Item")
                    input("Continuar")
                    continue
        elif respuesta == 3:
                if dinero >= 100:
                    dinero -= 100
                    mi_jugador.dinero = dinero
                    mi_jugador.pokebolas.append("Masterball")
                    mi_jugador.guardar()
                    print("Compraste Una Masterball Gracias!!! :D Roblitox Te lo agradece")
                    input("Continuar")
                    continue
                else:
                    print("No Tienes Dinero Para Comprar este Item")
                    input("Continuar")
                    continue
        elif respuesta==4 and paginas==0:
            paginas=1
            while paginas==1:
                os.system("cls")
                mi_jugador.imprimir_dinero()
                print("Vender Pokemones: (0) ")
                print("Comprar Cajas Misteriosas $200 (1)")
                print("Salir de Aqui (2): ")
                respuesta = int(input("Que vas A hacer?: "))
                if respuesta==0:
                    return print("vende")
                elif respuesta==1:
                    if dinero >=200:
                        print("Caja Comprada")
                        input("Continuar")
                        continue
                    else:
                        print("No tienes Dinero Para Este Item")
                        input("Continuar")
                        continue
                elif respuesta==2:
                    paginas=0
                    break
        elif respuesta==5:
            menu()
        else:
            print("Opción inválida. Intenta de nuevo.")
            input("Continuar")
            continue
    
import os
import time
import random
def tienda(menu,mi_jugador):
    mi_jugador.imprimir_dinero()
    while True:
        os.system("cls")
        dinero=mi_jugador.dinero
        print("=================")
        print("Comprar Pokeball Normal: $5 (0)")
        print("Comprar Greatball: $25 (1)")
        print("Comprar Ultraball: $50 (2)")
        print("Comprar Masterball: $100 (3)")
        respuesta = int(input("Que vas A hacer?: "))
        if respuesta==0:
            if dinero >=5:
                dinero-=5
                mi_jugador.dinero = dinero
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
                    mi_jugador.guardar()
                    print("Compraste Una Masterball Gracias!!! :D Roblitox Te lo agradece")
                    input("Continuar")
                    continue
                else:
                    print("No Tienes Dinero Para Comprar este Item")
                    input("Continuar")
                    continue
        else:
            print("Opción inválida. Intenta de nuevo.")
            input("Continuar")
            continue

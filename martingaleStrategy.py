import argparse
import math
import random
import time

initialPot = 0
winningPot = 0
loosingPot = 0
initialBet = 0
currentBalance = 0
currentBet = 1
iteraciones = 0
victorias = 0
derrotas = 0
games = 0

def iniciar():
    global initialPot, initialBet, currentBalance, currentBet, iteraciones, winningPot
    initialPot = 100 #int (input("Cuanto quieres apostar? "))
    initialBet = 1 # int(input("Con cuanto quieres empezar a apostar? "))
    currentBalance = 0
    currentBet = initialBet
    iteraciones = 0
    winningPot = 0

def empezar():
    return True #input("¿Quieres empezar? (si/no) ").lower() == "si"

def ruleta(color):
    resultado = random.choice(["rojo", "negro"])
    print(f"Resultado: {resultado}")
    return resultado == color

    
def jugar(color_fijo=None):
    global initialPot, initialBet, currentBalance, currentBet, iteraciones, winningPot
    if initialPot == 0:
        print("No tienes suficiente dinero para empezar.")
        return -1
    while abs(currentBalance) < initialPot:
        if winningPot >= initialPot*1.66:
            break

        if color_fijo:
            color_elegido = color_fijo
        else:
            color_elegido = input("¿Rojo o negro? ").lower()
        
        if ruleta(color_elegido):
            currentBalance = 0
            winningPot += initialBet
            currentBet = initialBet
            print(f"Has ganado {winningPot} hasta el momento.")
            iteraciones += 1
        else: 
            currentBalance -= currentBet
            currentBet = 2 * currentBet
            iteraciones += 1
            if abs(currentBalance) > initialPot:
                break
        print(f"Saldo actual: {currentBalance}, Apuesta actual: {currentBet}")
        #time.sleep(0.0002)  # Esperar 2 segundos entre cada jugada

while __name__ == "__main__" and games < 100:
    
    parser = argparse.ArgumentParser(description='Simulador de ruleta')
    parser.add_argument('-rojo', action='store_true', help='Si se especifica, siempre elige rojo')
    parser.add_argument('-negro', action='store_true', help='Si se especifica, siempre elige negro')
    args = parser.parse_args()

    iniciar()
    if empezar():
        if args.rojo:
            jugar(color_fijo='rojo')
        elif args.negro:
            jugar(color_fijo='negro')
        else:
            jugar()
        print(f"Juego terminado en {iteraciones} iteraciones. Saldo final: {currentBalance} con un winning pot de {winningPot}." )
        games += 1
        if winningPot >= 1.66*initialPot:
            victorias += 1
        else: derrotas += 1

    else:
        print("Has decidido no jugar.")

    print(f"Victorias: {victorias}, Derrotas: {derrotas}")
    if games == 1 or games == 99: input("Presiona Enter para salir...")



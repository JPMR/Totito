import random
import sys
#iniciamos variables
Movidas = {}
Teclas =""
jugadores = {}
#Creamos y guardamos qwerty de cordenadas y los jugadores
def iniciar():
    global Movidas, jugadores, Teclas
    #guardamos los jugadores
    jugador1 = input("ingresa nombre del jugador 1")
    jugador2 = input("ingresa nombre del jugador 2")
    jugadores = {"X":jugador1,  "O":jugador2}
    #Se piden los 9 caracteres
    Teclas = ""
    Teclas = input("ingresa, sin espacios, las teclas para las coordenadas\nDeben ser 9 en total\n")
    #se guardan los caracteres y creamos un diccionario con ellos
    for x in Teclas:
        Movidas.update({x:x})
    game_pvp()
def game_pvp():
    print_game()
    
def print_game():
    print("""
    \t-----------------------------
    \t         |         |
    \t    {}    |    {}    |    {}
    \t         |         |
    \t-----------------------------
    \t         |         |
    \t    {}    |    {}    |    {}
    \t         |         |
    \t-----------------------------
    \t         |         |
    \t    {}    |    {}    |    {}
    \t         |         |
    \t-----------------------------
    """.format(Movidas[Teclas[0]], Movidas[Teclas[1]], Movidas[Teclas[2]], Movidas[Teclas[3]],Movidas[Teclas[4]], Movidas[Teclas[5]], Movidas[Teclas[6]],
    Movidas[Teclas[7]], Movidas[Teclas[8]]))

iniciar()














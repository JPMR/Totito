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
    while(len(Teclas) != 9):
        print("----asegurate de ingresar un total de 9 teclas----")
        Teclas = input("ingresa, sin espacios, las teclas para las coordenadas\nDeben ser 9 en total\n")
    Teclas = Teclas.lower()
    #se guardan los caracteres y creamos un diccionario con ellos
    for x in Teclas:
        Movidas.update({x:x})
    game_pvp()
def game_pvp():
    global jugadores
    Termino = False
    rand = random.randint(0,1)
    if rand == 0:
        icono = "X"
        b = "O"
    elif rand == 1:
        icono = "O"
        b = "X"
    c = ""
    while (Termino == False):
        print_game()
        print("turno, jugador: " + jugadores[icono])
        pedir_posicion(icono)
        Termino = hay_ganador(icono)
        print(Termino)
        #cambiamos de turno
        c = icono
        icono = b
        b = c
    print_game()
    print("GANADOR: " + jugadores[Termino])
    while True:
        seguir = input("Desea seguir jugando? y/n\n").lower()
        if(seguir == "y"):
            iniciar()
            break
        elif (seguir == "n"):
            break

def hay_ganador(icono):
    global Movidas
    #buscamos 3 seguidos, para determinar el ganador
    #verificamos por filas completas
    for x in range(0,3):
        if (Movidas[Teclas[x*3]] == icono and Movidas[Teclas[x*3+1]] == icono and Movidas[Teclas[x*3+2]] == icono):
            return icono
    #verificamos por columnas completas
    for x in range(0,3):
        if (Movidas[Teclas[x]] == icono and Movidas[Teclas[x+3]] == icono and Movidas[Teclas[x+6]] == icono):
            return icono
    #verificamos diagonales
    print((Movidas[Teclas[0]]  + "  " +Movidas[Teclas[4]]) + "  " + Movidas[Teclas[8]])
    print((Movidas[Teclas[2]]  + "  " +Movidas[Teclas[4]]) + "  " + Movidas[Teclas[6]])
    if (Movidas[Teclas[0]] == icono and Movidas[Teclas[4]] == icono and Movidas[Teclas[8]] == icono):
        return icono
    if (Movidas[Teclas[2]] == icono and Movidas[Teclas[4]] == icono and Movidas[Teclas[6]] == icono):
        return icono
    return False

def pedir_posicion(jugador):
    global Movidas
    coordenada = input("Ingresa posicion").lower()
    #Se verifica que la cordenada sea correcta
    while not(coordenada in Movidas and Movidas[coordenada] != "X" and Movidas[coordenada] != "O"):
        coordenada = input("Ingresa posicion correcta").lower()
    Movidas.update({coordenada:jugador})
    
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














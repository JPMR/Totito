#!/usr/bin/env python3
import random
import os
import colorama as cfont
#iniciamos variables
Movidas = {}
Teclas =""
jugadores = {}
Modo_juego = ""
pc_name = ""
#creacion y almacenmiento de qwerty de cordenadas y a los jugadores
def iniciar():
    '''toma los nombres, teclas a usar y modo de juego'''
    cfont.init()
    clean_console()
    global Movidas, jugadores, Modo_juego, pc_name
    #guardamos los jugadores
    jugador1 = input("Ingresa nombre del jugador 1\n")
    clean_console()
    jugador2 = input("Ingresa nombre del jugador 2 \n*Para jugar con la pc, escribe pc\n")
    clean_console()
    if jugador2 == "pc":
        pc_name = pc_name_generator()
        print("nombre de la maquina: " + pc_name)
        print()
    jugadores = {"X":jugador1,  "O":jugador2}
    Modo_juego = input("Ingresa modo de juego (normal/miseria): ")
    while not(Modo_juego in ["normal", "miseria"]):
        Modo_juego = input("Ingresa modo de juego (normal/miseria): ")
    teclas_correctas = False
    clean_console()
    while not(teclas_correctas):
        guardar_teclas()
        print_game()
        print("Las teclas estan corrrectas? y/n: ")
        r = input("").lower()
        while not(r in ["y", "n"]):
            r = input("y/n: ").lower()
        if r == "y":
            teclas_correctas = True
    game_pvp()
#se guardan teclas como coordenadas o posiciones
def guardar_teclas():
    '''Guarda 9 teclas en una string (global Teclas) y en un diccionario (global Movidas), cada una como su propio key y value'''
    global Teclas, Movidas
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
#alternamos entre turnos de cada jugador "maneja el juego"
def game_pvp():
    '''alterna turnos y muestra el ganador'''
    global jugadores, pc_name
    Termino = False
    #Se elige al primero usando un randint
    rand = random.randint(0,1)
    if rand == 0:
        icono = "X"
        b = "O"
    elif rand == 1:
        icono = "O"
        b = "X"
    c = ""
    #mientras no ha teminado, preguntamos por movida
    while (Termino == False):
        print_game()
        #si es pc, elige random, contrario se pide respuesta
        if jugadores[icono] == "pc":
            print("turno, maquina: " + pc_name)
            movida_pc()
        else:
            print("turno, jugador: " + jugadores[icono])
            pedir_posicion(icono)
        Termino = hay_ganador(icono)
        #cambiamos de turno
        c = icono
        icono = b
        b = c
    print_game()
    #si el modo de juego es normal, el resultado es normal, contrario se cambia al ganador
    if Termino == 1:
        #empate
        print("No hay ganador, empate")
    else:
        if Modo_juego == "normal":
            print("GANADOR: " + jugadores[Termino])
        elif Modo_juego == "miseria":
            if Termino == "X":
                Termino = "O"
            else:
                Termino = "X"
            print("GANADOR: " + jugadores[Termino])
    #se pregunta si sigue jugando o no
    while True:
        seguir = input("Desea seguir jugando? y/n: \n").lower()
        if(seguir == "y"):
            iniciar()
            break
        elif (seguir == "n"):
            break
#obtiene una movida de la computadora
def movida_pc():
    '''elije una movida con random'''
    global Teclas, Movidas
    coordenada = Teclas[random.randint(0,8)]
    #Se verifica que la cordenada sea correcta
    while not(Movidas[coordenada] != "X" and Movidas[coordenada] != "O"):
        coordenada = Teclas[random.randint(0,8)]
    Movidas.update({coordenada:"O"})
#devuelve false si no hay ganador o un icono del jugador que gano
def hay_ganador(icono):
    '''verifica por 3 en linea o si no hay un ganador'''
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
    if (Movidas[Teclas[0]] == icono and Movidas[Teclas[4]] == icono and Movidas[Teclas[8]] == icono):
        return icono
    if (Movidas[Teclas[2]] == icono and Movidas[Teclas[4]] == icono and Movidas[Teclas[6]] == icono):
        return icono
    #verificamos por un empate
    empate = True
    for x in Teclas:
        if (Movidas[x] in Teclas):
            empate = False
    if empate:
        return 1
    return False
#Obtiene la movida del jugador
def pedir_posicion(jugador):
    '''toma la jugada, verifica que sea valida y la guarda'''
    global Movidas
    coordenada = input("Ingresa posicion: ").lower()
    #Se verifica que la cordenada sea correcta
    while not(coordenada in Movidas and Movidas[coordenada] != "X" and Movidas[coordenada] != "O"):
        coordenada = input("Ingresa posicion correcta: ").lower()
    Movidas.update({coordenada:jugador})
#muestra el tablero
def print_game():
    '''imprime la tabla del juego con las movidas y teclas'''
    color = []
    #Se guardan colores
    for tecla in Teclas: 
        movida = Movidas[tecla]
        if movida == "X":
            color.append(cfont.Fore.LIGHTYELLOW_EX)
        elif movida == 'O':
            color.append(cfont.Fore.BLUE)
        else: 
            color.append(cfont.Fore.GREEN)
    #creamos formato (movidas y sus colores)
    reset = cfont.Fore.WHITE
    formato = []
    for x in range(9):
        formato.append(color[x] +Movidas[Teclas[x]] + reset)
    #Se imprime tablero
    print(reset)
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
    """.format(*formato))
#limpia consola
def clean_console():
    '''os.system('cls')'''
    os.system('cls')
#genera un nombre aleatorio (not working)
def pc_name_generator():
    titles = [" elastico", """ carmesí""", " volador", " robacaramelos", " aterragnomos", ", Defensor de un mundo destrozado", """ el Maníaco Enmascarado""", " JENKINS", ", la Mente Envenenada", ", la vaca dorada", " gelatinico", " del planeta chocolate", " del equipo moradito"]
    nom = ""
    vocals = "aeiou"
    funny_consonant = ["n", "w", "rr", "k", "kr", "z", "tr", "x", "v", "gu", "fr", "h"]
    for x in range(random.randint(2,4)):
        nom = nom + vocals[random.randint(0,4)]
        nom = nom + funny_consonant[random.randint(0,11)]
    nom = nom + titles[random.randint(0,12)]
    return(nom)
iniciar()














import random
import numpy as np
import PosicionBarcos
import jugador1
import jugador2
import tablerosdejuego
import time
barcos = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
tablero1 = PosicionBarcos.posicion_barcos()
tablero2 = PosicionBarcos.posicion_barcos()

tablero_auto_disp = tablero1.copy()
tablero_jugador_disp = tablero2.copy()

tablero_vacio = np.full((10,10,), " ")
    
tablero_vacio2 = np.full((10,10,), " ")

tablerosdejuego.tableros_juego()
if __name__ == "__main__":
    
    PosicionBarcos.posicion_barcos()
    while 'O' in tablero_jugador_disp or 'O' in tablero_auto_disp:
        jugador1.disparo_player1(tablero_jugador_disp, tablero_vacio,tablero_auto_disp,tablero_vacio2)
        print(tablero_jugador_disp,tablero_vacio)
        x = int(input('J1, Introduce coordenada X'))
        if x < 0 or x > 9:
            x = int(input('Num. no valido, tira otra vez coordenada X'))
            continue
        y = int(input('J1, Introduce coordenada Y'))
        if y < 0 or y > 9:
            y = int(input('Num. no valido, tira otra vez coordenada X'))
            continue

        if tablero_jugador_disp[x, y] == 'O':  
            tablero_jugador_disp[x, y] = 'X'
            tablero_vacio[x, y] = 'X'
            print("Tablero de la maquina\n", 'Has dado en el blanco!\n', tablero_vacio)
            continue
        elif tablero_jugador_disp[x, y] == ' ':
            tablero_jugador_disp[x, y] = ' - '
            tablero_vacio[x, y] = ' - '
            print("Tablero de la maquina\n", 'Has hecho Agua!\n', tablero_vacio)
            time.sleep(3)
            jugador2.disparo_player2(tablero_auto_disp,tablero_vacio2,tablero_jugador_disp, tablero_vacio)

        else:
            continue


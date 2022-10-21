import random
import jugador1
def disparo_player2(tablero_auto_disp,tablero_vacio2,tablero_jugador_disp, tablero_vacio):
        while 'O' in tablero_auto_disp and 'O' in  tablero_jugador_disp:
            print(tablero_auto_disp)
            print('Tablero de la maquina\n',tablero_vacio2)
            x = random.randint(0,9)
            if x < 0 or x > 9:
                print('Num. no valido, tira otra vez')
                continue
            y = random.randint(0,9)
            if y < 0 or y > 9:
                print('Num. no valido, tira otra vez')
                continue

            if tablero_auto_disp[x, y] == 'O':
                tablero_auto_disp[x, y] = 'X'
                tablero_vacio2[x, y] = 'X'
                print("Tablero de la maquina\n", 'Has dado en el blanco!\n', tablero_vacio2)
                continue
            elif tablero_auto_disp[x, y] == ' ':
                tablero_auto_disp[x, y] = 'A'
                tablero_vacio2[x, y] = 'A'
                print("Tablero de la maquina\n", 'Has hecho Agua!\n', tablero_vacio2)
                jugador1.disparo_player1(tablero_jugador_disp, tablero_vacio,tablero_auto_disp,tablero_vacio2)
            else:
                print('¡HAS GANADO!')
import jugador2

def disparo_player1(tablero_jugador_disp, tablero_vacio,tablero_auto_disp,tablero_vacio2):
        while 'O' in tablero_jugador_disp and 'O' in tablero_auto_disp:
            print(tablero_auto_disp)
            print('Tablero de la maquina\n',tablero_vacio)
            x = int(input('J1, Introduce coordenada X'))
            if x < 0 or x > 9:
                print('Num. no valido, tira otra vez')
                continue
            y = int(input('J1, Introduce coordenada Y'))
            if y < 0 or y > 9:
                print('Num. no valido, tira otra vez')
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
                jugador2.disparo_player2(tablero_auto_disp,tablero_vacio2,tablero_jugador_disp, tablero_vacio)

            else:
                print('¡HAS GANADO!')
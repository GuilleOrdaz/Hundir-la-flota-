import numpy as np 
import PosicionBarcos

def tableros_juego():
    tablero1 = PosicionBarcos.posicion_barcos()
    tablero2 = PosicionBarcos.posicion_barcos()

    tablero_auto_disp = tablero1.copy()
    tablero_jugador_disp = tablero2.copy()

    tablero_vacio = np.full((10,10,), " ")
    tablero_vacio2 = np.full((10,10,), " ")
    return (tablero_auto_disp,tablero_jugador_disp,tablero_vacio,tablero_vacio2)




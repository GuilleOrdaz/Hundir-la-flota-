## JUEGO HUNDIR LA FLOTA EN PYTHON
Este es un programa básico que simula el juego 'Hundir la flota' ('Battleship'), desarrollado en lenguaje Python(3).
El juego empieza a ejecutarse con el archivo _main_.py
*HUNDIR LA FLOTA* comienza por un menú creado con dos opciones: Una primera opción para jugar y otra segunda opción para salir del juego. Habiendo selecciondo la opcion "Jugar" comenzará la generación de tableros, con un tamaño de 10 x 10, donde se crearán aleatoriamente 10 barcos mediante el tamaño de sus esloras, un total de 20:
* 4 barcos de 1 posición de eslora
* 3 barcos de 2 posiciones de eslora
* 2 barcos de 3 posiciones de eslora
* 1 barco de 4 posiciones de eslora

El lugar de los barcos, se mostrarán como 'O' en el tablero.
Se generarán cuatro tableros, dos de ellos con generación de barcos aleatorios, uno para el jugador 1, y otro para el jugador 2, que en esta versión será la máquina, más dos tableros más vacíos.
Al jugador 1 por pantalla se mostrarán dos tableros:
  *   El tablero_vacio es una copia del tablero_disparos_jugador1, donde están los barcos del jugador 2, y donde se irá registrando los movimientos de disparos que ejecute el jugador 1, registrando una 'X' donde coincida con un barco, 'O', y registrando '-' cuando el jugador 1 de en agua.
  
  * el tablero_auto_disparos, que corresponde al tablero con las posiciones de nuestros barcos, visibles para nosotros.

### Acción del juego:
La persona que comienza a tirar será el jugador 1, mediante la llamada de jugador1.py.
se le pedirá que ingrese el número del 0 al 9 de la fila, y lo mismo para la columna. 
Estas coordenadas se registran y buscarán en el tablero_disparos_jugador1 si encuentra barco('O'), o agua(' '). Si el jugador 1 acierta en barco, seguirá tirando hasta que coincida con agua y pase el turno al jugador 2.

El jugador 2, como hemos dicho anteriormente, en esta versión corresponde a la máquina, e introducirá coordenadas de forma aleatoria hacia el tablero del jugador 1, y la dinámica de turno es la misma que la mencionada con el jugador 1.

Importante destacar que la franja de valores del input del jugador 1 queda limitada a valores comprendidos entre 0 y 9 tanto para filas como para columnas, acorde a las medidas de la matriz de los tableros. De manera que, cuando se introduzca un valor negativo, un número que esté fuera de los límites del tablero o un string, se volverá a pedir que el usuario ingrese nuevamente las coordenadas con valores que si estén en la franja.

### Final
El juego acaba cuando uno de los dos jugadores acaben con todos los barcos del contrario, es decir, cuando ya no haya 'O' en el tablero de algunos de los jugadores, y mostrará por pantalla al jugador 1 si ha sido vencedor o perdedor. 
En el caso de que el jugador 2 se quede sin barcos, el jugador 1 será el ganador.

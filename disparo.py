#def disparo(x,y):  #Definimos la posición de los disparos dentro del tablero

# 3. Recibe un disparo en uno de los barcos, sustituyendo la O por una X
def disparo(board, x, y):
  board = board.copy()
  if (board[x,y]== "O"):
    board[x,y]='X'
  elif(board [x,y]== " "):
    board[x,y]='-'
  return board
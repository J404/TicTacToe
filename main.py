from board import Board

from minimax import minimax
from minimax import numGames

board = Board(None)

playerMarker = input('X or Os? ')
cpuMarker = 'X' if playerMarker == 'O' else 'O'

print('You go first')
board.printBoard()

# Game loop
while not board.checkWin():
    spot = int(input('Enter the number you would like to place your piece on: '))
    board.putOnBoard(spot, playerMarker)
    board.printBoard()

    if board.checkWin():
        break

    numGames = 0
    cpuMove = minimax(board, cpuMarker, playerMarker, 0, True)
    board.putOnBoard(cpuMove, cpuMarker)

    print(f'The computer put a {cpuMarker} on position {cpuMove}')
    board.printBoard()

winMsg = 'You have won!' if board.winner == playerMarker else 'The computer has won :('
print(winMsg)
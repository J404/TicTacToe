import math

from board import Board

numGames = 0

def minimax(board, marker, opponentMarker, depth, isMaximizing):
    global numGames

    if board.checkWin() == True:
        numGames += 1

        if board.winner == marker:
            return 10 - depth
        elif board.winner == opponentMarker:
            return -10 + depth
    elif board.movesLeft() == False:
        numGames += 1

        return 0


    if isMaximizing:
        value = -math.inf
        bestIndex = None

        for i in range(board.countEmpty()):
            copy = board.getBoardCopy()
            newBoard = Board(copy)
            indexFilled = newBoard.fillEmpty(i, marker)

            branchValue = minimax(newBoard, marker, opponentMarker, depth + 1, False)

            if branchValue > value:
                value = branchValue
                bestIndex = indexFilled
        
        # If we are at the 'start', we need to make a move
        # Otherwise, we just want the value of this branch
        if depth == 0:
            print(f'CPU searched {numGames} games')
            return bestIndex
        else:
            return value
    
    # Opponent is minimizing
    else:
        value = math.inf
        bestIndex = None

        for i in range(board.countEmpty()):
            copy = board.getBoardCopy()
            newBoard = Board(copy)
            indexFilled = newBoard.fillEmpty(i, opponentMarker)

            branchValue = minimax(newBoard, marker, opponentMarker, depth + 1, True)

            if branchValue < value:
                value = branchValue
                bestIndex = indexFilled
        
        return value

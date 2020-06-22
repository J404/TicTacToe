class Board:
    def __init__(self, board):
        if board is None:
            self.board = []
            self.initializeBoard()
        else:
            self.board = board
        self.winner = None

    def initializeBoard(self):
        k = 1
        for i in range(3):
            self.board.append([])
            for j in range(3):
                self.board[i].append(str(k))
                k += 1
    
    def getBoardCopy(self):
        copy = []

        for i in range(3):
            copy.append([])
            for j in range(3):
                copy[i].append(self.board[i][j])
        
        return copy

    # Fills in the n + 1th empty square and returns the board index of the square filled in
    def fillEmpty(self, n, marker):
        emptySeen = 0

        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 'X' and self.board[i][j] != 'O':
                    if emptySeen == n:
                        self.board[i][j] = marker
                        return ((i * 3) + j) + 1
                    else:
                        emptySeen += 1

    # Returns the number of empty squares
    def countEmpty(self):
        empty = 0

        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 'X' and self.board[i][j] != 'O':
                    empty += 1
        
        return empty

    # takes in index 1-9 and converts that to a spot on the board
    def putOnBoard(self, index, marker):
        index -= 1
        i = index // 3
        j = index % 3

        self.board[i][j] = marker

    def checkWin(self):
        # Check horizontals
        for i in range(len(self.board)):
            if self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
                self.winner = self.board[i][0]
                return True

        # Check verticals
        for i in range(len(self.board)):
            if self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
                self.winner = self.board[0][i]
                return True
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            self.winner = self.board[0][0]
            return True

        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
            self.winner = self.board[0][2]
            return True
        
        return False
    
    def movesLeft(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 'X' and self.board[i][j] != 'O':
                    return True
        
        return False
    
    def printBoard(self):
        for i in range(len(self.board)):
            print('   |   |   ')
            print(f' {self.board[i][0]} | {self.board[i][1]} | {self.board[i][2]} ')
            print('   |   |   ')

            if i != len(self.board) - 1:
                print('-----------')
    
    
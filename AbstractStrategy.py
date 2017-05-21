from Config import DIMENSION


class AbstractStrategy:
    def __init__(self, mapMatrixP):
        self.mapMatrix = mapMatrixP
        self.winningPatterns = []
        self.winningPatterns.append(0b111000000)
        self.winningPatterns.append(0b000111000)
        self.winningPatterns.append(0b000000111)
        self.winningPatterns.append(0b100100100)
        self.winningPatterns.append(0b010010010)
        self.winningPatterns.append(0b001001001)
        self.winningPatterns.append(0b100010001)
        self.winningPatterns.append(0b001010100)

    def doBestMoveNN(self, currentMapMatrix):
        pass

    def hasWon(self, turn):
        pattern = 0b000000000
        for i in range(DIMENSION):
            for j in range(DIMENSION):
                if self.mapMatrix.matrix[i][j] == turn:
                    pattern |= 1 << i * DIMENSION + j

        for winningPattern in self.winningPatterns:
            if pattern & winningPattern == winningPattern:
                return True
        return False

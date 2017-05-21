from AbstractStrategy import AbstractStrategy
from Config import DEPTH, DIMENSION, CROSS, CIRCLE, EMPTY
from Coordinates import Coordinates


class MinMaxStrategy(AbstractStrategy):
    def __init__(self, mapMatrixP):
        super().__init__(mapMatrixP)
        self.movesDone = 0
        self.nodesCheck = 0

    def countMovesDone(self):
        moves = 0
        for i in range(DIMENSION):
            for j in range(DIMENSION):
                if self.mapMatrix.matrix[i][j] is not EMPTY:
                    moves += 1
        return moves

    @staticmethod
    def validateBestMove(bestmove):
        if bestmove is None:
            print("BestMove jest None-> co oznacza że fcja minimax została włączona gdy nie było wolnego miejsca na mapie")

    def doBestMoveNN(self, currentMapMatrix, turn='ai'):
        self.mapMatrix = currentMapMatrix
        self.movesDone = self.countMovesDone()
        print("MOVESDONE: ", self.movesDone)
        with open(f'temp.txt', 'w') as file:
            bestmove, bestscore = self.minMaxPrintNodes(DEPTH - self.movesDone, "", file, -float('Inf'), float('Inf'), turn)
        print(f"MINMAX + ALFABETA MACNĄł {self.nodesCheck} WĘZłÓW")
        self.nodesCheck = 0
        self.validateBestMove(bestmove)
        return bestmove

    def doBestMove(self, currentMapMatrix, turn='ai'):
        self.mapMatrix = currentMapMatrix
        self.movesDone = self.countMovesDone()
        print("MOVESDONE: ", self.movesDone)
        with open(f'moveTree{self.movesDone}.txt', 'w') as file:
            bestmove, bestscore = self.minMaxPrintNodes(DEPTH - self.movesDone, "", file, -float('Inf'), float('Inf'), turn)
        print(f"MINMAX + ALFABETA DOTKNĄL {self.nodesCheck} WĘZłÓW")
        self.nodesCheck = 0
        temp, temp1 = self.minMax(DEPTH - self.movesDone)
        print(f" SAM MINMAX DOTNKAL {self.nodesCheck} WĘZłÓW")
        self.nodesCheck = 0
        self.validateBestMove(bestmove)
        self.mapMatrix.markCircleOn(bestmove)
        return bestmove

    def calcPossibleMoves(self):
        possibleMoves = []
        if self.hasWon(CIRCLE) or self.hasWon(CROSS):
            return possibleMoves
        for i in range(DIMENSION):
            for j in range(DIMENSION):
                if self.mapMatrix.matrix[i][j] == EMPTY:
                    temp = Coordinates(i, j)
                    possibleMoves.append(temp)
        return possibleMoves

    def minMax(self, ply, turn='ai'):
        possibleMoves = self.calcPossibleMoves()
        bestMove = None
        bestScore = None
        if turn == 'ai':
            bestScore = float('Inf')
        elif turn == 'player':
            bestScore = -float('Inf')

        if ply == 0 or not possibleMoves:
            bestScore = self.evaluate()
        else:
            for move in possibleMoves:
                self.mapMatrix.markOn(move, turn)
                self.nodesCheck += 1
                if turn == 'ai':
                    temp, score = self.minMax(ply - 1, 'player')
                    if bestScore is None or score < bestScore:
                        bestScore = score
                        bestMove = move
                elif turn == 'player':
                    temp, score = self.minMax(ply - 1, 'ai')
                    if bestScore is None or score > bestScore:
                        bestScore = score
                        bestMove = move
                self.mapMatrix.markAsEmpty(move)
        return bestMove, bestScore

    def minMaxPrintNodes(self, ply, indent, fileToWrite, alpha, beta, turn='ai'):
        indent = indent + "++"
        possibleMoves = self.calcPossibleMoves()
        bestMove = None
        bestScore = None
        if turn == 'ai':
            bestScore = float('Inf')
        elif turn == 'player':
            bestScore = -float('Inf')

        if ply == 0 or not possibleMoves:
            bestScore = self.evaluate()
        else:
            for move in possibleMoves:
                if beta <= alpha:
                    fileToWrite.write('UCINAM\n')
                    break
                self.mapMatrix.markOn(move, turn)
                self.nodesCheck += 1
                if turn == 'ai':
                    temp, score = self.minMaxPrintNodes(ply - 1, indent, fileToWrite, alpha, beta, 'player')
                    fileToWrite.write(f'{indent}{score}A\n')
                    if bestScore is None or score < bestScore:
                        bestScore = score
                        bestMove = move
                    beta = min(beta, bestScore)
                elif turn == 'player':
                    temp, score = self.minMaxPrintNodes(ply - 1, indent, fileToWrite, alpha, beta, 'ai')
                    fileToWrite.write(f'{indent}{score}P\n')
                    if bestScore is None or score > bestScore:
                        bestScore = score
                        bestMove = move
                    alpha = max(alpha, bestScore)
                self.mapMatrix.markAsEmpty(move)

        return bestMove, bestScore

    def evaluate(self):
        score = 0
        score += self.evaluateLine(0, 0, 0, 1, 0, 2)
        score += self.evaluateLine(1, 0, 1, 1, 1, 2)
        score += self.evaluateLine(2, 0, 2, 1, 2, 2)

        score += self.evaluateLine(0, 0, 1, 0, 2, 0)
        score += self.evaluateLine(0, 1, 1, 1, 2, 1)
        score += self.evaluateLine(0, 2, 1, 2, 2, 2)

        score += self.evaluateLine(0, 0, 1, 1, 2, 2)
        score += self.evaluateLine(0, 2, 1, 1, 2, 0)
        return score

    def evaluateLine(self, row1, cel1, row2, cel2, row3, cel3):
        score = 0

        if self.mapMatrix.matrix[row1][cel1] == CROSS:
            score = 1
        elif self.mapMatrix.matrix[row1][cel1] == CIRCLE:
            score = -1

        if self.mapMatrix.matrix[row2][cel2] == CROSS:
            if score > 0:
                score *= 10
            elif score == 0:
                score = 1
            else:
                return 0
        elif self.mapMatrix.matrix[row2][cel2] == CIRCLE:
            if score < 0:
                score *= 10
            elif score == 0:
                score = -1
            else:
                return 0

        if self.mapMatrix.matrix[row3][cel3] == CROSS:
            if score > 0:
                score *= 10
            elif score == 0:
                score = 1
            else:
                return 0
        elif self.mapMatrix.matrix[row3][cel3] == CIRCLE:
            if score < 0:
                score *= 10
            elif score == 0:
                score = -1
            else:
                return 0
        return score

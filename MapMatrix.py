from Config import CROSS, CIRCLE, EMPTY, DIMENSION


class MapMatrix:

    def __init__(self, size, nparray=None):

        self.matrix = [[EMPTY for _ in range(size)] for _ in range(size)]
        if nparray is not None:
            for i in range(size):
                for j in range(size):
                    if nparray[i][j] == 0:
                        self.matrix[i][j] = EMPTY
                    else:
                        self.matrix[i][j] = nparray[i][j]
        self.marks = 0

    def markOn(self, coordinates, turn):
        if turn == 'ai':
            self.matrix[coordinates.x][coordinates.y] = CIRCLE
        elif turn == 'player':
            self.matrix[coordinates.x][coordinates.y] = CROSS
        self.marks += 1

    def markCrossOn(self, coordinates):
        self.matrix[coordinates.x][coordinates.y] = CROSS
        self.marks += 1

    def markCircleOn(self, coordinates):
        self.matrix[coordinates.x][coordinates.y] = CIRCLE
        self.marks += 1

    def markAsEmpty(self, coordinates):
        if self.matrix[coordinates.x][coordinates.y] != EMPTY:
            self.marks -= 1
        self.matrix[coordinates.x][coordinates.y] = EMPTY

    def checkIfMapFull(self):
        if self.marks == DIMENSION**2:
            return True
        return False


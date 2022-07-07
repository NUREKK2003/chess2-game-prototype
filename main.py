from abc import ABC, abstractmethod


# klasa abstrakcyjna bierka
class Piece(ABC):

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def dead(self):
        pass


# self oznacza konkretną instancję
class Rook(Piece):
    canAttack = False

    def __init__(self, spawnX, spawnY):
        # inicjalizacja nowej instancji
        self.posx = int(spawnX)
        self.posy = int(spawnY)

    def move(moveX, moveY):
        pass

    def attack(attackX, attackY):
        pass

    def dead(self):
        pass


class Monkey(Piece):

    def __init__(self, spawnX, spawnY):
        # inicjalizacja nowej instancji
        self.posx = int(spawnX)
        self.posy = int(spawnY)

    def move(moveX, moveY):
        pass

    def attack(attackX, attackY):
        pass

    def dead(self):
        pass


class Elephant(Piece):

    def __init__(self, spawnX, spawnY):
        # inicjalizacja nowej instancji
        self.posx = int(spawnX)
        self.posy = int(spawnY)

    def move(moveX, moveY):
        pass

    def attack(attackX, attackY):
        pass

    def dead(self):
        pass


class Fishy(Piece):
    isFishyQuin = False

    def __init__(self, spawnX, spawnY):
        # inicjalizacja nowej instancji
        self.posx = int(spawnX)
        self.posy = int(spawnY)

    def move(moveX, moveY):
        pass

    def attack(attackX, attackY):
        pass

    def dead(self):
        pass


class King(Piece):
    hasBannana = True
    isTrapped = False

    def __init__(self, spawnX, spawnY):
        # inicjalizacja nowej instancji
        self.posx = int(spawnX)
        self.posy = int(spawnY)

    def move(moveX, moveY):
        pass

    def attack(attackX, attackY):
        pass

    def dead(self):
        pass


class Queen(Piece):
    isTrapped = False

    def __init__(self, spawnX, spawnY):
        # inicjalizacja nowej instancji
        self.posx = int(spawnX)
        self.posy = int(spawnY)

    def move(moveX, moveY):
        pass

    def attack(attackX, attackY):
        pass

    def dead(self):
        pass

class EmptyPos(Piece):

    def __init__(self, spawnX, spawnY):
        # inicjalizacja nowej instancji
        self.posx = int(spawnX)
        self.posy = int(spawnY)

    def move(self):
        pass

    def attack(self):
        pass

    def dead(self):
        pass

# szachownica (lista obiektów)
chessboard = [[EmptyPos(0,0)]*10 for i in range(9)]


#print(str(chessboard[0][0]))
#chessboard[0][0] = King(0,0)
#print(str(chessboard[0][0]))

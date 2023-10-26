import string
import random
class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = [] # TODO
        for i in range(9):
            self.grid.append(random.choice(string.ascii_letters).upper())

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        j=0
        for c in word:
            for i in range(9):
                if c==self.grid[i]:
                    j=j+1
                    break

        if j==9:
            return True
        else :
            return False

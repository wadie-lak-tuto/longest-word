import requests
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

        for c in word:
            if c in self.grid:
                    continue
            else:
                return False
        return self.__check_dictionary(word)


    @staticmethod
    def __check_dictionary(word):
        response = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        json_response = response.json()
        return json_response['found']

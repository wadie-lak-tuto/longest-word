from longest_word.game import Game
import string


class TestGame:
    def test_game_initialization(self):
            # setup
            self.new_game = Game()

            # exercise
            self.grid = self.new_game.grid

            # verify
            assert type(self.grid) == list
            assert len(self.grid) == 9
            for letter in self.grid:
                assert letter in string.ascii_uppercase


    def test_is_valid(self):

        self.test_game_initialization()
        test=Game.is_valid(self,self.grid)
        assert test , 'the word and the grid don\'t match'

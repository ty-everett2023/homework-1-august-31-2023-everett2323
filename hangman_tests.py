import unittest
from unittest.mock import patch
import random

"""
Everett, these are your unit tests. DO NOT CHANGE these tests. As you build each function, come and run the test
named after it. If it passes, the code is most likely(but not always) complete. If not, go back and try and figure 
out why the test failed. Good luck!

"""
from build_hangman_here import read_words_from_file, choose_random_word, display_word, get_player_guess, \
    is_guess_correct, update_guessed_letters, game_over, display_game_status


class TestHangman(unittest.TestCase):

    def test_read_words_from_file(self):
        # Test if the function reads words from a file and returns them as a list
        words = read_words_from_file('test_words.txt')
        self.assertEqual(words, ['apple', 'banana', 'cherry'])

    def test_choose_random_word(self):
        # Test if the function returns a random word from the given list of words
        random.seed(1)
        word = choose_random_word()
        self.assertEqual(word, 'banana')

    def test_display_word(self):
        # Test if the function returns the word with underscores for unguessed letters
        result = display_word('apple', ['a', 'p'])
        self.assertEqual(result, 'app__')

    def test_get_player_guess(self):
        # Test if the function correctly captures and returns the player's guess
        with patch('builtins.input', return_value='a'):
            guess = get_player_guess()
        self.assertEqual(guess, 'a')

    def test_is_guess_correct(self):
        # Test if the function correctly identifies if a guessed letter is in the word
        self.assertTrue(is_guess_correct('apple', 'a'))
        self.assertFalse(is_guess_correct('apple', 'z'))

    def test_update_guessed_letters(self):
        # Test if the function correctly updates the list of guessed letters
        guessed_letters = ['a', 'b']
        updated_guessed_letters = update_guessed_letters(guessed_letters, 'c')
        self.assertEqual(updated_guessed_letters, ['a', 'b', 'c'])

    def test_game_over(self):
        # Test if the function correctly identifies when the game is over
        self.assertTrue(game_over(0, 'apple'))
        self.assertFalse(game_over(1, 'apple'))
        self.assertTrue(game_over(1, '_____'))

    def test_display_game_status(self):
        # Test if the function returns the expected game status string
        status = display_game_status(3, ['a', 'b'], 'a____')
        self.assertEqual(status, 'Attempts left: 3, Guessed letters: [a, b], Word: a____')


if __name__ == '__main__':
    unittest.main()

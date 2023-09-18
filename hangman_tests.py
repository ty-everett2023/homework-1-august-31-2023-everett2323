import random
import unittest
from unittest.mock import patch

from build_hangman_here import update_guessed_letters, is_guess_correct, get_player_guess, display_word, \
    choose_random_word, read_words_from_file, game_over, display_game_status


class TestHangman(unittest.TestCase):

    def test_read_words_from_file(self):
        # Test if the function reads words from a file and returns them as a list
        words = read_words_from_file('words.txt')
        expected_words = ['FLUID', 'BROKEN', 'BEAST', 'FLEET', 'BORING', 'CUPID', 'UNANIMOUS', 'PYTHON', 'JAVA',
                          'SYNTAX', 'RUBBER', 'BUOYANT']
        self.assertEqual(words, expected_words)

    def test_choose_random_word(self):
        # Test if the function returns a random word from the given list of words
        random.seed(1)
        words = read_words_from_file('words.txt')
        word = choose_random_word()
        self.assertIn(word, words)

    def test_display_word(self):
        # Test if the function returns the word with underscores for unguessed letters
        result = display_word('FLUID', ['f', 'l'])
        self.assertEqual(result, 'FL___')

    def test_get_player_guess(self):
        # Test if the function correctly captures and returns the player's guess
        with patch('builtins.input', return_value='a'):
            guess = get_player_guess()
        self.assertEqual(guess, 'a')

    def test_is_guess_correct(self):
        # Test if the function correctly identifies if a guessed letter is in the word
        self.assertTrue(is_guess_correct('FLUID', 'f'))
        self.assertFalse(is_guess_correct('FLUID', 'z'))

    def test_update_guessed_letters(self):
        # Test if the function correctly updates the list of guessed letters
        guessed_letters = ['f', 'l']
        updated_guessed_letters = update_guessed_letters(guessed_letters, 'u')
        self.assertEqual(updated_guessed_letters, ['f', 'l', 'u'])

    def test_game_over(self):
        # Test if the function correctly identifies when the game is over
        self.assertTrue(game_over(0, 'FLUID'))
        self.assertFalse(game_over(7, 'FLUID'))
        self.assertTrue(game_over(0, '_____'))

    def test_display_game_status(self):
        # Test if the function prints the expected game status string
        with patch('builtins.print') as mocked_print:
            display_game_status(3, ['f', 'l'], 'FL___')
        mocked_print.assert_called_with('Word: FL___')


if __name__ == '__main__':
    unittest.main()
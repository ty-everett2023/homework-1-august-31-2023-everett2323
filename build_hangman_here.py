import random
# STEP 1: Import the 'random' library so we can pick random words.

# STEP 2: Set Up Variables
def read_words_from_file(filename):
    # This function is fully implemented. It reads words from a file into a list.
    with open(filename, 'r') as file:
        return [word.strip() for word in file.readlines()]

words = read_words_from_file('words.txt')  # Read words from 'words.txt'
attempts = 0  # We will set this later. It should be the length of the word being guessed plus 2.
guessed_letters = []  # An empty list to keep track of the letters you've guessed.

# STEP 3: Pick a Random Word
def choose_random_word():
    # TODO: Pick a random word from the 'words' list.
    # INSTRUCTION: Use 'random.choice(words)' to pick a random word from the list and return it.

# STEP 4: Show the Word
def display_word(word, guessed_letters):
    # TODO: Show the word but use underscores for letters not guessed yet.
    # INSTRUCTION: Use a 'for' loop to go through each letter in the word. If the letter was guessed, show it; if not, show an underscore ('_').
    # Additionally, construct a string to accumulate the result and return this string at the end of the function.

# STEP 5: Get the Player's Guess
def get_player_guess():
    # TODO: Ask the player to guess a letter.
    # INSTRUCTION: Use 'input("Guess a letter: ")' to get a letter from the player. Make sure to change it to lowercase using '.lower()'. Consider adding validation to ensure a valid letter is entered.

# STEP 6: Check the Guess
def is_guess_correct(word, guess):
    # TODO: See if the guessed letter is in the word.
    # INSTRUCTION: Use 'if guess in word.lower():' to see if the letter is in the word. Return True if it is, and False if it's not.

# STEP 7: Add Guessed Letters
def update_guessed_letters(guessed_letters, guess):
    # TODO: Add the new guessed letter to the list.
    # INSTRUCTION: Use 'guessed_letters.append(guess)' to add the new letter to the end of the list. Don't forget to return the updated list of guessed letters.

# STEP 8: Is the Game Over?
def game_over(attempts, word):
    # TODO: Find out if the game is over.
    # INSTRUCTION: The game ends if you run out of tries or if you guess the whole word. Implement a check to see if the word has been fully guessed (no underscores left) or if all attempts have been used, and return True if the game is over, and False otherwise.

# STEP 9: Show Game Info
def display_game_status(attempts, guessed_letters, word):
    # TODO: Show the current state of the game.
    # INSTRUCTION: Use 'print()' to show the number of attempts left, the letters you've guessed, and the current word with underscores for missing letters (utilize the 'display_word' function to get the current state of the word).

# STEP 10: Keep the Game Going
def main():
    # This function is fully implemented. It will use all the other functions to play the game.
    # TODO: Implement a while loop that keeps running, allowing the game to be played multiple times. At the end of each game (whether won or lost), prompt the user to play again or quit. If the user enters 'q', the game ends, otherwise a new game starts.
    # INSTRUCTION: Inside the while loop, reset the 'guessed_letters' and 'attempts' variables at the start of each new game. Also, ensure correct guesses do not decrease the 'attempts' counter. Display a message informing the user of the number of remaining attempts after an incorrect guess.

# STEP 11: Start Playing
# TODO: To start the game, you'll need to call the 'main()' function.
if __name__ == '__main__':
    main()
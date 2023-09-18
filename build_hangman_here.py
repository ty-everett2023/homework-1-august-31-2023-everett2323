import random
# STEP 1: Import the 'random' library so we can pick random words.

'''''
TEST
'''''
# STEP 2: Set Up Variables
def read_words_from_file(filename):
    # This function is fully implemented. It reads words from a file into a list.
    with open(filename, 'r') as file:
        return [word.strip() for word in file.readlines()]


words = read_words_from_file('words.txt')  # Read words from 'words.txt'
attempts = 0  # We will set this later. It should be the length of the word being guessed plus 1.
guessed_letters = []  # An empty list to keep track of the letters you've guessed.


# STEP 3: Pick a Random Word
def choose_random_word():
    # TODO: Pick a random word from the 'words' list.
    # INSTRUCTION: Use 'random.choice(words)' to pick a random word from the list and return it.
    rcw = random.choice(words)
    return rcw



# STEP 4: Show the Word
def display_word(word, guessed_letters):
    # TODO: Show the word but use underscores for letters not guessed yet.
    # INSTRUCTION: Use a 'for' loop to go through each letter in the word. If the letter was guessed, show it; if not, show an underscore ('_').
    # Additionally, construct a string to accumulate the result and return this string at the end of the function
    """
    INSTRUCTIONS
    1. CREATE A VARIABLE WITH AN EMPTY STRING IN IT. NO SPACES.
    2. CREATE A FOR EACH LOOP(FOR LETTER IN WORD)
    3. IF THE LOWERCASE LETTER IS IN GUESSED LETTERS,
    ADD THE LETTER TO DISPLAYED WORD.
    OTHERWISE, ADD A DASH TO DISPLAYED WORD
    4. RETURN THE DISPLAYED WORD


    """


# STEP 5: Get the Player's Guess
def get_player_guess():
    # TODO: Ask the player to guess a letter.
    # INSTRUCTION: Use 'input("Guess a letter: ")' to get a letter from the player. Make sure to change it to lowercase using '.lower()'.
    return input("guess a letter: ").lower()


# STEP 6: Check the Guess
def is_guess_correct(word, guess):
    # TODO: See if the guessed letter is in the word.
    # INSTRUCTION: Use 'if guess in word:' to see if the letter is in the word. Return True if it is, and False if it's not.
    # RETURN A BOOLEAN THAT SAYS IF THE GUESS IS IN THE WORD. MAKE SURE IT'S LOWERCASE
    return guess in word.lower()



# STEP 7: Add Guessed Letters
def update_guessed_letters(guessed_letters, guess):
    # TODO: Add the new guessed letter to the list.
    # INSTRUCTION: Use 'guessed_letters.append(guess)' to add the new letter to the end of the list.
    guessed_letters.append(guess)
    return guessed_letters


# STEP 8: Is the Game Over?
def game_over(attempts, word):
    # TODO: Find out if the game is over.
    # INSTRUCTION: The game ends if you run out of tries or if you guess the whole word. Return True if the game is over, and False otherwise.
    if attempts == 0:
        return True
    else:
        return False


# STEP 9: Show Game Info
def display_game_status(attempts, guessed_letters, word):
    # TODO: Show the current state of the game.
    # INSTRUCTION: Use 'print()' to show the number of attempts left, the letters you've guessed, and the current word with underscores for missing letters.
    print(f'Attempts {attempts}')
    



# STEP 10: Keep the Game Going
def main():
    while True:
        global guessed_letters, attempts
        word = choose_random_word()
        attempts = len(word) + 2
        guessed_letters = []
        while not game_over(attempts, word):
            display_game_status(attempts, guessed_letters, word)
            guess = get_player_guess()
            if is_guess_correct(word, guess):
                guessed_letters = update_guessed_letters(guessed_letters, guess)
            else:
                attempts -= 1
                print(f"Incorrect guess. You have {attempts} attempts left.")

        if '_' not in display_word(word, guessed_letters):
            print("Congratulations! You've guessed the word.")
        else:
            print(f"Game Over. The word was: {word}")

        # Asking the user if they want to play again or quit the game
        play_again = input("Press any key to play again or 'q' to quit: ").lower()
        if play_again == 'q':
            break



# STEP 11: Start Playing
# TODO: To start the game, you'll need to call the 'main()' function.
if __name__ == '__main__':
    main()

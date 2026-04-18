def verify_word(word, guessed_letters, try_letter):
    """
    Verifies if the guessed letter is in the word and updates the guessed letters list.
    Input :
    - word: str, the word to guess
    - guessed_letters: list, the list of letters that have been guessed so far
    - try_letter: str, the letter that the player is trying to guess
    Output :
    - is_correct: bool, True if the guessed letter is in the word, False otherwise
    - updated_guessed_letters: list, the updated list of guessed letters
    """
    if try_letter in word:
        guessed_letters.append(try_letter)
        return True, guessed_letters
    else:
        return False, guessed_letters
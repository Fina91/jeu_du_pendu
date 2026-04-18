import scripts.parsing_dictionnary as parsing_dictionary

def print_current_state(word, guessed_letters):
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    print(f"Mot actuel: {display_word}")

def game(word, max_attempts):
    attempts = 0
    guessed_letters = set()
    
    while attempts < max_attempts:
        guess = input("Entrer une lettre: ").lower()

        if guess == '':
            print("Veuillez entrer une lettre.")
            continue
        
        if guess in guessed_letters:
            print("Vous avez déjà deviné cette lettre. Essayez encore.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"Bravo '{guess}' se trouve dans le mot!")
            print_current_state(word, guessed_letters)
        else:
            print(f"Désolé'{guess}' n'est pas dans le mot.")
            attempts += 1
            print(f"Il vous reste {max_attempts - attempts} tentatives.")
        
        # Check if the player has guessed all letters
        if all(letter in guessed_letters for letter in word):
            print(f"Félicitations! Vous avez deviné le mot '{word}'!")
            return
    
    print(f"Perdu! Le mot était '{word}'.")

if __name__ == "__main__":
    dictionnary = parsing_dictionary.parse_dictionnary(r'data\dictionnaire.txt')
    random_word = parsing_dictionary.get_random_word(dictionnary)
    
    # Le mot n'est pas divulgué, mais sa longueur est affichée pour aider le joueur.
    # print(f"Random word: {random_word}")
    print(f"Longueur du mot: {dictionnary[random_word]}")
    print("_" * dictionnary[random_word])

    game(random_word, max_attempts = 5)



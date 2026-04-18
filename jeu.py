import scripts.parsing_dictionnary as parsing_dictionary
import yaml
import colorama
from colorama import Fore

colorama.init()

def print_current_state(word, guessed_letters):
    """
    Affiche l'état actuel du mot à deviner, en montrant les lettres devinées et les lettres manquantes.
    Input :
    - word: str, le mot à deviner
    - guessed_letters: set, l'ensemble des lettres qui ont été devinées
    Output :
    - None, affiche simplement l'état actuel du mot    
    """
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    print(f"Mot actuel: {display_word}")

def game(word, max_attempts):
    """
    Fonction principale du jeu du pendu. Gère les tentatives du joueur et vérifie les lettres devinées.
    Input :
    - word: str, le mot à deviner
    - max_attempts: int, le nombre maximum de tentatives autorisées
    Output :
    - None, gère le déroulement du jeu et affiche les résultats
    
    """
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
            print(Fore.BLUE + f"Bravo '{guess}' se trouve dans le mot!" + Fore.RESET)
            print_current_state(word, guessed_letters)
        else:
            print(Fore.YELLOW + f"Désolé '{guess}' n'est pas dans le mot." + Fore.RESET)
            attempts += 1
            print(f"Il vous reste {max_attempts - attempts} tentatives.")
        
        # Check if the player has guessed all letters
        if all(letter in guessed_letters for letter in word):
            print(Fore.GREEN + f"Félicitations! Vous avez deviné le mot '{word}'!" + Fore.RESET)
            return
    
    print(Fore.RED + f"Perdu! Le mot était '{word}'." + Fore.RESET)

if __name__ == "__main__":
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    
    dictionnary = parsing_dictionary.parse_dictionnary(config['dictionary_file'])
    random_word = parsing_dictionary.get_random_word(dictionnary)
    
    # Le mot n'est pas divulgué, mais sa longueur est affichée pour aider le joueur.
    # print(f"Random word: {random_word}")
    print(f"Longueur du mot: {dictionnary[random_word]}")
    print("_" * dictionnary[random_word])

    game(random_word, max_attempts=config['max_attempts'])


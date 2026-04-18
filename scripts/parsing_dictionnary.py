import random

def parse_dictionnary(file_path):
    """
    Parses a dictionnary file and returns a dictionary object.
    The file should have the following format:
     word;type;number
    Input :
    - file_path: str, the path to the dictionnary file
    Output :
    - dictionnary: dict, a dictionary where the keys are the words and the values are their definitions    
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()

    dictionnary = {}
    for line in lines:
        word, definition = line.strip().split(';', 1)
        dictionnary[word.strip()] = len(word.strip())

    return dictionnary

def get_random_word(dictionnary):
    return random.choice(list(dictionnary.keys()))
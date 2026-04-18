# Jeu du Pendu

Jeu de pendu pour le projet DAEU B.

## Auteur
Myriam Choukatli

## Description
Ce jeu est une implémentation du jeu du pendu en Python. Le joueur doit deviner un mot en proposant des lettres une par une. Le jeu utilise un dictionnaire de mots français.

## Dépendances
- Python 3.x
- Module `random` (inclus dans la bibliothèque standard Python)

## Installation
1. Assurez-vous que Python 3.x est installé sur votre système.
2. Clonez ou téléchargez ce dépôt.
3. Naviguez vers le répertoire du projet.

## Comment lancer le jeu
1. Ouvrez un terminal.
2. Naviguez vers le répertoire du projet : `jeu_du_pendu`
3. Exécutez la commande : `python jeu.py`

## Fonctionnement du jeu
- Au lancement, le jeu sélectionne un mot aléatoire du dictionnaire.
- La longueur du mot est affichée, ainsi qu'une série de tirets bas (_) représentant chaque lettre.
- Le joueur doit entrer une lettre à la fois.
- Si la lettre est dans le mot, elle est révélée aux bonnes positions.
- Si la lettre n'est pas dans le mot, le nombre de tentatives restantes diminue.
- Le jeu se termine lorsque le joueur devine le mot ou qu'il n'a plus de tentatives (5 maximum).

## Ce qui est affiché
- Longueur du mot et tirets initiaux.
- Invite : "Entrer une lettre: "
- Feedback pour chaque tentative :
  - "Bravo '[lettre]' se trouve dans le mot!" si correct.
  - "Désolé '[lettre]' n'est pas dans le mot." si incorrect, avec le nombre de tentatives restantes.
  - "Vous avez déjà deviné cette lettre. Essayez encore." si lettre déjà proposée.
  - "Veuillez entrer une lettre." si entrée vide.
- État actuel du mot avec lettres devinées.
- Message de victoire : "Félicitations! Vous avez deviné le mot '[mot]'!"
- Message de défaite : "Perdu! Le mot était '[mot]'."

## Structure du projet
- `jeu.py` : Fichier principal du jeu.
- `scripts/parsing_dictionnary.py` : Module pour parser le dictionnaire.
- `data/dictionnaire.txt` : Fichier contenant les mots et leurs définitions.
- `README.md` : Ce fichier.

## Format du dictionnaire
Le fichier `data/dictionnaire.txt` contient des lignes au format :
```
mot;type;nombre
```
Par exemple :
```
abandonner;verbe;1809
```

Le jeu utilise uniquement le mot et sa longueur pour le gameplay.

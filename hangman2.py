import random
from words import words
import string

def valid_w(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = valid_w(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives=7 

    while len(word_letters) > 0 and lives > 0: 
        print('You have', lives, 'remaining. Letters used:',''.join(used_letters)) 

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current Word: ',''.join(word_list))

        letter_imput = input('Input a Letter: ').upper()
        if letter_imput in alphabet - used_letters: 
            used_letters.add(letter_imput)
            if letter_imput in word_letters: 
                word_letters.remove(letter_imput)

            else: lives=lives-1 

        elif letter_imput in used_letters:
            print("ERROR: Letter has already been used. Please input a different letter.")
        else: 
            print("ERROR: Letter unrecognised. Please input a letter commonly used in the Latin Alphabet.")

    if lives == 0:
            print("You have 0 lives left and lost the game.")
            print("Word: ", word, '.')
    else: 
            print("Congratulations! You have guessed the word!")
            print('You had ', lives, ' remaining.')
            print('Your word was: ', word, '.')

hangman()
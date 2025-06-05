# SDM: make a hangman game where each part of the game is written as a function, and the main game loop is run inside of a function which calls all the other smaller function
# e.g.

import random

def print_welcome_message():
    print("Welcome to my Hangman game!")

def generate_random_word():
    words_list = ["stars", "dreams", "love", "astronomy", "mango",
               "minecraft", "jaguar", "calico"]
    return random.choice(words_list)

def generate_blanks(word_input):
    new_blanks = ""
    for char in word_input:
        new_blanks += "_"
    return new_blanks

def display_current_blanks(blanks_input):
    blanks_display = ""
    for char in blanks_input:
        blanks_display += char + " "
    print(f"Current blanks: {blanks_display}")

def get_user_answer():
    """This allows the user to guess a letter to play the game"""
    letter_guess = input("Please enter a letter guess: ")
    return letter_guess

def check_validity(secret_word, letter_guess):
    return letter_guess in secret_word


def update_blanks(secret_word, current_blanks, letter_guess):
    """This function goes through the user guess and updates the blanks depending on whether it was correct or not."""
    new_blanks = ""
    for index in range(len(secret_word)):
        if(secret_word[index] == letter_guess):
            new_blanks += letter_guess
        else:
            new_blanks += current_blanks[index]
    return new_blanks

def display_game_won_message():
    print("You have won, congratualions!")

def display_game_over_message():
    print("You lost! Try again.")

def run_game_loop():
   playing = True
   print_welcome_message()
   lives = 5
   random_word = generate_random_word()
   print(f"My secret random word is '{random_word}'.")
   blanks = generate_blanks(random_word)
   while playing:
       display_current_blanks(blanks)
       answer = get_user_answer()
       answer_valid = check_validity(random_word, answer)
       if(answer_valid):
           blanks = update_blanks(random_word, blanks, answer)
           if(blanks == random_word):
               display_game_won_message()
               playing = False
       else:
           lives = lives - 1
       if(lives == 0):
           display_game_over_message()
           playing = False

run_game_loop()

# SDM: make a hangman game where each part of the game is written as a function, and the main game loop is run inside of a function which calls all the other smaller function
# e.g.

import random

def print_welcome_message():
    print("Welcome to my Hangman game!")

def generate_random_word():
    words_list = ["elephant", "monster", "zebra", "saxophone", "clarinet",
               "sashimi", "perpendicular", "bat"]
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

def get_user_answer():
    letter_guess = input("Please enter a letter guess: ")
    return letter_guess

def check_validity():
    pass

def update_blanks():
    pass

def display_game_won_message():
    print("You have won, congratualions!")

def display_game_over_message():
    print("You lost! Try again.")

def run_game_loop():
   playing = True
   print_welcome_message()
   lives = 5
   random_word = generate_random_word()
   blanks = generate_blanks(random_word)
   while playing:
       display_current_blanks()
       answer = get_user_answer()
       answer_valid = check_validity()
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
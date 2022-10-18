from modules import print_in_color #imports the module containing the function definition for how the text is printed in color to the terminal
from get_guess_fn import get_guess #imports the module containing the function definition for obtaining the guess from the user
from is_valid_guess_fn import is_valid_guess #imports the module containing the function definition for checking whether the guess is valid (contains required letters form previous guesses)
from print_guess_fn import print_guess #imports the module containing the function definition for printing the letters of the user's guess with the appropriate color
from is_game_over_fn import is_game_over #imports the module containing the function definition for checking whether the game is over, and carrying out the corresponding actions
"""
The lines of code above import modules for previously defined functions
"""

tries_left = 6 #the tries_left variable stores the number of attempts the user has left to guess the secret word
secret_word = input("Enter the secret word: ") #Asks user for the secret word to be guessed
for iteration in range(6): #This for loop iterates through this entire block of code 6 times to allow the user have 6 attempts
    if iteration == 0: # Suggestion: Possibly change the temp variable name to current_attempt instead of iteration to make code more readable
        # For the first guess -> there is no need to check for valid guess because there is no subsequent guess to compare with, so first guess cannot use the get_guess() function.
        guess = input("Enter your guess: \n") ## making minor updat eot comment ot test this feature out
        tries_left -= 1
        if is_game_over(secret_word,guess,tries_left): # Checks to see whether the game is over. If it is over, the user's guess doesn't need to be printed to the screen again in the respective color.
            break
        else:
            required_letters = print_guess(secret_word,guess)
            print("")
    else:
        #This else statement is for the other user attempts after the first attempt, this uses the get_guess() function to also keep ensuring that the user's guess is valid.
        guess = get_guess(required_letters)
        tries_left -= 1
        if is_game_over(secret_word,guess,tries_left): # Checks to see whether the game is over. If it is over, the user's guess doesn't need to be printed to the screen again in the respective color.
            break
        else:
            required_letters = print_guess(secret_word,guess)
            print("")

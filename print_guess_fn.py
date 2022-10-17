from modules import print_in_color

def print_guess(secret_word,guess):
    """
    Description:


    Parameters:
    secret_word -> string
    guess -> string 
    """
    required_letters = []
    for index in range(5):
        shoud_print_first_letter_green = guess[index] == secret_word[index]
        shoud_print_first_letter_red = guess[index] not in secret_word
        is_similar_char = guess[index] in secret_word
        if is_similar_char == True:
            required_letters.append(guess[index])
        if shoud_print_first_letter_green:
            print_in_color(guess[index],'green')
        elif shoud_print_first_letter_red:
            print_in_color(guess[index],'red') 
        else:
            print_in_color(guess[index],'yellow')
    return required_letters
def is_game_over(secret_word,guess,tries_left):
    if guess == secret_word:
        if tries_left == 5:
            print("Correct! You got it in 1 try")
            return True
        print(f"Correct! You got it in {6-tries_left} tries!")
        return True
    elif tries_left == 0 and guess != secret_word:
        print(f"Game over! The correct word is {secret_word}")
        return True
    else:
        return False
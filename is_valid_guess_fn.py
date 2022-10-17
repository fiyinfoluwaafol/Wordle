def is_valid_guess(guess,required_letters):
    for index in range(len(required_letters)):
        if required_letters[index] not in guess:
            return False
    else:
        return True
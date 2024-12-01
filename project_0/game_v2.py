"""Guess the number game. The computer will chose and guess a number"""

import numpy as np


def random_guess(number: int = 1) -> int:
    """Randomly guess the number

    Args:
        number (int, optional): Number to guess. Defaults to 1.

    Returns:
        int: Attempts
    """

    attempts = 0
    while True:
        attempts += 1
        guess = np.random.randint(1, 101)
        if guess == number:
            break

    return attempts


def game_core_v3(number: int = 1) -> int:
    """The function guesses the number from 1 to 100.
    To begin with we start from 0 and increase our guess by 10 if it is less than the number
    and decrease by 1 if it is bigger than the number.

    Args:
        number (int, optional): The number to guess. Defaults to 1.

    Returns:
        int: Amount of attempts.
    """

    attempts = 0  # initial amount of attempts
    guess = 0  # initial guess

    while True:
        attempts += 1  # Increment amount of attmpts
        if guess == number:
            break
        elif guess > number:  # If our guess is greater than the number will decrease our guess by 1
            guess -= 1
        else:
            guess += 10  # If our guess is less than the number will increas our guess by 10

    return attempts  # Return final amount if attempts


def score_game(random_guess) -> int:
    """Mean amount of attempts to guess the number for 1000 games.

    Args:
        random_guess (_type_): The guess functions

    Returns:
        int: Mean amount of attempts
    """

    attempts_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, 1000)

    for number in random_array:
        attempts_ls.append(random_guess(number))

    score = int(np.mean(attempts_ls))
    print(f"Yor algorithm guesses the number for {score} attempts in average")
    return score


if __name__ == "__main__":
    score_game(game_core_v3)

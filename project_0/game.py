"""Game guess the number"""

import numpy as np

number = np.random.randint(1, 101)

attempts = 0
while True:
    attempts += 1
    guess = int(input("Guess the number: "))
    
    if guess < number:
        print(f"The number is greater than {guess}")
    elif guess > number:
        print(f"The number is less then {guess}")
    else:
        print(f"Your have guessed the number {number} from {attempts} attempts")
        break

def random_guess(number:int=1) -> int:
    """_summary_

    Args:
        number (int, optional): _description_. Defaults to 1.

    Returns:
        int: _description_
    """
import random
from rich import print
from rich.console import Console

console = Console()

def guessing_game():
    answer = random.randint(0, 100)

    while True:
        user_guess = int(input('What is your guess? '))

        if user_guess == answer:
            console.print(f'Right.  The answer is {user_guess}', style="bold red")
            break

        if user_guess < answer:
            console.print(f'Your answer of {user_guess} is too low')
        else:
            console.print(f'Your guess of {user_guess} is too high')


guessing_game()

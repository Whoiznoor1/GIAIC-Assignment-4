import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number :
            print('Sorry! you guessed lower one. Try again!')
        elif guess > random_number :
            print('Sorry! You guessed higher number. Try again!')

    print(f'OH YES! You guessed the correct number {random_number}. Cheers up!')

guess(10)
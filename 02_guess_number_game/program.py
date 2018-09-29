import random
print('------------------------------')
print(' GUESS THE NUMBER GAME')
print('------------------------------')
print()

the_number = random.randint(0,100)
guess = -1
print(the_number)
name = input('What is you name? ')

while guess != the_number:
    guess_text = input('Guess a number between 0 - 100: ')
    guess = int(guess_text)

    if guess < the_number:
        print('Sorry {0}. Your guess of {1} was too LOW.'.format(name, guess))
    elif guess > the_number:
        print('Sorry {0}. Your guess of {1} was too HIGH.'.format(name, guess))
    else:
        print('Good work {0}, you guessed correctly! You win!'.format(name))

print('done')

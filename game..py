import random

print("Let's play a game!!")
down_border_number = input('Type the down border of the guessing game: ')
while True:
    try:
        down_border_number = int(down_border_number)
        break
    except ValueError:
        print()
        print('You have to type an integer!')

upper_border_number = input('Type the upper border of the guessing game: ')
while True:

    try:
        upper_border_number = int(upper_border_number)
    except ValueError:
        print()
        print('You have to type an integer!')
        upper_border_number = input('Type the upper border of the guessing game: ')
        continue

    if upper_border_number == down_border_number:
        print()
        print('Way to easy...You can do better, so pick bigger upper border!')
        upper_border_number = input('Type the upper border of the guessing game: ')

    elif upper_border_number < down_border_number:
        print()
        print('Upper border must be bigger then the down border!')
        upper_border_number = input('Type the upper border of the guessing game: ')

    else:
        print()
        print("Good, let's play.")
        break

random_number = random.randint(down_border_number, upper_border_number)

player_number = input('Type your guess: ')
attempts = 0
while True:

    try:
        player_number = int(player_number)

    except ValueError:
        print()
        print('Not a valid guess!')
        player_number = input('Type your guess: ')
        continue

    if player_number == random_number:
        attempts += 1
        print()
        print('Correct!')
        print(f'Not that hard, right! You got it with {attempts} attempts.')
        break

    elif player_number > upper_border_number:
        print()
        print('You are trying to go out of range! Not in this game!')
        player_number = input('Type your guess, AGAIN: ')

    elif player_number < down_border_number:
        print()
        print('You are trying to go out of range! Not in this game!')
        player_number = input('Type your guess, AGAIN: ')

    else:
        attempts += 1

        if attempts > 2:
            print()
            print('Incorrect! Do you give up?')
            answer = input('Yes or No: ')

            if answer.lower() == 'yes':
                print()
                print(f'The answer was: {random_number}')
                break
            elif answer.lower() == 'no':
                print()
                print('I guess not. Good!')
                player_number = input('Type your guess: ')

            else:
                print()
                print('You trying some stuff clearly.')
                player_number = input('Type your guess: ')
        else:
            print()
            print('Incorrect!')
            player_number = input('Type your guess: ')

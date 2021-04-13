import random
from time import sleep

def make_decision_computer():
    available_options = ('PAPER', 'SCISSORS', 'ROCK')
    choice = random.choice(available_options)
    return choice

def make_decision_player():
    player_options = {'R':'ROCK', 'S': 'SCISSORS', 'P': 'PAPER'}
    choice = input('>').upper()
    return player_options[choice]

def main_game():
    computer_score = []
    player_score = []

    computer_live = 3
    player_live = 3
    round = 1

    print('='* 50)
    print('ROCK, SCISSORS, PAPER GAME'.center(50))
    print('='* 50)
    print('INSTRUCTIONS: ')
    print(f'''->ROCK BEATS SCISSORS
->SCISSORS BEATS PAPER
->PAPER BEATS ROCK
{('-' * 50)}
PRESS:
->[R] FOR ROCK
->[S] FOR SCISSORS
->[P] FOR PAPER
{('-' * 50)}
->PRESS 'Q' FOR EXIT
{('=' * 50)}
GAME STARTED!
''')
    print('MAKE YOUR DECISION!')
    computer_decision = make_decision_computer()
    player_decision = make_decision_player()
    i = 3
    for i in range(4):
        print(f'{i}..')
        sleep(1)
    print(f'PLAYER = {player_decision}')
    print(f'COMPUTER {computer_decision}')



main_game()



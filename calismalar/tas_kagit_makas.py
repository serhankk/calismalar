import random
from time import sleep

def make_decision_computer():
    available_options = ('PAPER', 'SCISSORS', 'ROCK')
    choice = random.choice(available_options)
    return choice

def make_decision_player():
    player_options = {'R':'ROCK', 'S': 'SCISSORS', 'P': 'PAPER', 'Q': 'EXIT'}
    err_flag = 1
    while err_flag == 1:
        choice = input('>>>').upper()
        if choice == 'Q':
            exit('Exiting.')
        elif choice not in player_options.keys():
            print('PLEASE ENTER A VALID CHOICE!')
            continue
        else:
            return player_options[choice]


def main_game():

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
    while True:
        print(f'ROUND: {round}')
        print(f'Player Live= {player_live} | Computer Live= {computer_live}')
        print('MAKE YOUR DECISION!')
        computer_decision = make_decision_computer()
        player_decision = make_decision_player()
        for i in range(1,4):
            print(f'{i}..')
            sleep(0.7)
        print('-' * 50)
        print(f'PLAYER = {player_decision}')
        print(f'COMPUTER = {computer_decision}')

        print('-' * 50)
        if player_decision == computer_decision:
            print('*** DRAW *** '.center(50, '-'))
            round += 1
        elif (player_decision == 'R') and (computer_decision == 'SCISSORS'):
            print('*** PLAYER WINS ***'.center(50, '-'))
            round += 1
            computer_live -= 1
        elif (player_decision == 'P') and (computer_decision == 'ROCK'):
            print('*** PLAYER WINS ***'.center(50, '-'))
            round += 1
            computer_live -= 1
        elif (player_decision == 'S') and (computer_decision == 'PAPER'):
            print('*** PLAYER WINS ***'.center(50, '-'))
            round += 1
            computer_live -= 1
        else:
            print('*** COMPUTER WINS ***'.center(50, '-'))
            round += 1
            player_live -= 1
        print('=' * 50)

        if player_live == 0 or computer_live == 0:
            if player_live == 0:
                print('GAME OVER! YOU LOST!')
            elif computer_live == 0:
                print('GAME OVER! YOU WIN!')
            print('=' * 50)
            print('DO YOU WANT TO PLAY AGAIN? ([Y]ES / [N]O)')
            play_again = input('>>>').upper()
            if play_again == 'Y':
                computer_live = 3
                player_live = 3
                round = 1
                continue
            elif play_again == 'N':
                print('End of game.')
                exit('Exiting.')
            else:
                exit('Unkown')


main_game()
print('End of game by flow end.')
exit('Exiting.')


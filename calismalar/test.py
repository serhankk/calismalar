def make_decision_player():
    player_shortcut = {'R':'ROCK', 'S': 'SCISSORS', 'P': 'PAPER'}
    choice = input().upper()

    return player_shortcut[choice]

print('abc')
x = make_decision_player()
print('123')
print(x)
print('qwe')
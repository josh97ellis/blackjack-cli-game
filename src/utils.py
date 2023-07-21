from config import Configuration
from playsound import playsound
import sys

_config = Configuration('game_config.yaml')

def play_again() -> bool:
    action = input('Play Again? (y/n): ')
    if action == 'y':
        return True
    elif action == 'n':
        return False
    else:
        print('Invalid input!')
        play_again()


def confirm_play():
    # Confirm play
    play = input('Would you like to play the game? (y/n):')
    if play == 'y':
        playsound(_config.get_value('sounds')[0]['casino_bling'])
        pass
    elif play == 'n':
        print('Goodbye!')
        sys.exit()
    else:
        print(f'{play} is not an allowed action!')
        confirm_play()
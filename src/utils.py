from config import Configuration
from playsound import playsound
import sys


def play_again() -> bool:
    action = input('Play Again? (y/n): ')
    if action == 'y':
        return True
    elif action == 'n':
        print('Goodbye!')
        sys.exit()
    else:
        print(f'{action} is not an allowed action!')
        play_again()


def confirm_play():
    # Confirm play
    play = input('Would you like to play the game? (y/n):')
    if play == 'y':
        print('Welcome!')
        print('')
    elif play == 'n':
        print('Goodbye!')
        sys.exit()
    else:
        print(f'{play} is not an allowed action!')
        confirm_play()
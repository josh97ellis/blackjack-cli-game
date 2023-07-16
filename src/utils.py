def play_again() -> bool:
    action = input('Play Again? (y/n): ')
    if action == 'y':
        return True
    elif action == 'n':
        return False
    else:
        print('Invalid input!')
        play_again()
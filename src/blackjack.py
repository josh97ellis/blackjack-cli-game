import sys
import time

import scenarios
from utils import play_again
from cards2 import Shoe, Hand, Chips

print('Welcome to my Blackjack Game, Good Luck! \n')

# Ask player to purchase chips
player_chips = Chips()

# Create a shoe of decks for the game
shoe = Shoe(num_decks=8)
shoe.shuffle()

while True:
    print('Starting a New Game, Good Luck! \n')
    
    # Player make bet
    print(f'Current chip total: ${player_chips.total} \n')
    player_chips.bet = int(input("How much would you like to bet? Minimum is $5: "))
    if player_chips.bet > player_chips.total:
        print(f"${player_chips.bet} is more than what you have. Bet must not exceed ${player_chips.total}! \n")
        continue
    
    # Initial deal: 1 to player, 1 to dealer (down), 1 to player, 1 to dealer (up)
    player_hand = Hand()
    dealer_hand = Hand()
    player_hand.add_card(shoe.deal_card())
    dealer_hand.add_card(shoe.deal_card())
    player_hand.add_card(shoe.deal_card())
    dealer_hand.add_card(shoe.deal_card())
    
    # Show hand to player
    print('')
    print('Your Hand:')
    player_hand.display_cards(show_all=True)
    time.sleep(1)
    print('')
    print('Dealer Showing:')
    dealer_hand.display_cards(show_all=False)
    print('')
    
    # Insurance if dealers face up card is an Ace
    if 'Ace' in dealer_hand.cards[1].rank:
        player_insurance = input('Insurance? y/n: ')
        
    # Handle scenarios where the deal has a blackjack
    if dealer_hand.value == 21:
        dealer_hand.display_cards(show_all=True)
        if player_hand.value == 21:
            scenarios.push()
        else:
            scenarios.dealer_wins(player_chips)
        
        if play_again():
            continue
        else:
            sys.exit()
    
    # Handle scenario where the player gets a blackjack and dealer does not
    if player_hand.value == 21:
        scenarios.player_wins(player_chips, blackjack=True)
        if play_again():
            continue
        else:
            sys.exit()

    # Continue play with player until hand is complete
    while player_hand.value < 21:
        action = input('Hit or Stand?: ').lower()
        if action == 'hit':
            player_hand.add_card(shoe.deal_card())
            print('')
            print('Player Hand:')
            player_hand.display_cards()
            if player_hand.value > 21:
                scenarios.player_busts(player_chips)
                player_hand.is_bust = True
                break
            else:
                continue
        else:
            break
    
    # Ask to play another game if player hand has busted
    if player_hand.is_bust:
        if play_again():
            continue
        else:
            sys.exit()
    
    # Continue play with dealer until hand is complete
    print('')
    print('Dealer Hand:')
    dealer_hand.display_cards(show_all=True)
    time.sleep(3)
    while dealer_hand.value < 17:
        dealer_hand.add_card(shoe.deal_card())
        dealer_hand.display_cards(show_all=True)
        if dealer_hand.value > 21:
            scenarios.dealer_busts(player_chips)
            dealer_hand.is_bust = True
            break
        if dealer_hand.value > 17:
            break
        else:
            time.sleep(3)
    
    # Ask to play another game if dealer hand has busted
    if dealer_hand.is_bust:
        if play_again():
            continue
        else:
            sys.exit()
    
    # If neither the dealer or player have busted, compare the hand values to determine winner
    if player_hand.value > dealer_hand.value:
        scenarios.player_wins(player_chips, blackjack=False)
    elif player_hand.value == dealer_hand.value:
        scenarios.push()
    else:
        scenarios.dealer_wins(player_chips)
    
    # Ask to play another game
    if play_again():
            continue
    else:
        sys.exit()

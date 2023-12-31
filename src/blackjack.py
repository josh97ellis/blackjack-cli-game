import sys
import time
from playsound import playsound

import scenarios
from config import Configuration
from utils import play_again, confirm_play
from cards import Shoe
from player import Chips, Hand

_config = Configuration('game_config.yaml')

print('Welcome to my Blackjack Game, Good Luck!\n')
playsound(_config.get_value('sounds')[0]['casino_bling'])

# Congiure table rules
game_config = Configuration('game_config.yaml')
MIN_BET = game_config.get_value('game_rules')[0]['minimum_bet']
MAX_BET = game_config.get_value('game_rules')[0]['maximum_bet']
NUM_DECKS = game_config.get_value('game_rules')[0]['decks_in_shoe']
SOFT_17 = game_config.get_value('game_rules')[0]['soft_17']
BLACKJACK_PAYOUT = game_config.get_value('game_rules')[0]['blackjack_payout']

# Print game rules
print('Table Rules:')
print(f'-> Minimum Bet: {MIN_BET}')
print(f'-> Maximum Bet: {MAX_BET}')
print(f'-> Number of Decks: {NUM_DECKS}')
print(f'-> Soft 17: {SOFT_17}')
print(f'-> Blackjack Payout: {BLACKJACK_PAYOUT}')
print('')

# Confirm play
confirm_play()

# Create a shoe of decks for the game
shoe = Shoe(num_decks=NUM_DECKS)
shoe.shuffle()
burner_card = shoe.deal_card(show=False, sound=False)

# Ask player to purchase chips
player_chips = Chips()
player_chips.purchase_chips()

while True:
    print('')
    print('-------------------------------')
    print('Starting a New Game, Good Luck!')
    print('-------------------------------')
    
    print(f'Current chip total: ${player_chips.total} \n')
    player_chips.bet = 0
    
    # Check if the player has enough chips to play the game
    if player_chips.total < MIN_BET:
        while player_chips.total < MIN_BET:
            purchase_more = input(f"You do not have enough chips to play, minimum is ${MIN_BET}. Would you like to purchase more chips? (y/n):")
            print('')
            if purchase_more == 'y':
                player_chips.purchase_chips()
                print(f'Current chip total: ${player_chips.total} \n')
            else:
                print("Goodbye!")
                sys.exit()
    
    # Have player make their bet
    player_chips.make_bet()
    
    # Check that the bet is not more than the total chips the player has
    if player_chips.bet > player_chips.total:
        while player_chips.bet > player_chips.total:
            print(f"${player_chips.bet} is more than what you have. Bet must not exceed ${player_chips.total}! \n")
            player_chips.make_bet()
    
    # Check that the bet is not less than the table minimum
    if player_chips.bet < MIN_BET:
        while player_chips.bet < MIN_BET:
            print(f"${player_chips.bet} is less than the table minimum. Bet must be at least ${MIN_BET}! \n")
            player_chips.make_bet()
    
    # Check that the bet is not less than the table minimum
    if player_chips.bet > MAX_BET:
        while player_chips.bet > MAX_BET:
            print(f"${player_chips.bet} is more than the table maximum. Bet must not exceed ${MAX_BET}! \n")
            player_chips.make_bet()
    
    # Initial deal: 1 to player, 1 to dealer (down), 1 to player, 1 to dealer (up)
    player_hand = Hand()
    dealer_hand = Hand()
    
    print('player card:')
    card = shoe.deal_card(side='front')
    player_hand.add_card(card)
    time.sleep(.25)
    
    print('dealer card:')
    card = shoe.deal_card(side='back')
    dealer_hand.add_card(card)
    time.sleep(.25)
    
    print('player card:')
    card = shoe.deal_card(side='front')
    player_hand.add_card(card)
    time.sleep(.25)
    
    print('dealer card:')
    card = shoe.deal_card(side='back')
    dealer_hand.add_card(card)
    time.sleep(.25)
    
    # Show hand to player
    print('Your Hand:')
    player_hand.display_cards(show_all=True)
    print('')
    time.sleep(.5)
    
    # Show dealers face up card to player
    print('Dealer Showing:')
    dealer_hand.display_cards(show_all=False)
    print('')
    time.sleep(.5)
    
    # Insurance if dealers face up card is an Ace
    if 'Ace' in dealer_hand.cards[0].rank:
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
    
    # Handle scenario where the player gets a blackjack and dealer does not
    if player_hand.value == 21:
        scenarios.player_wins(player_chips, blackjack=True)
        if play_again():
            continue

    # Continue play with player until hand is complete
    while player_hand.value < 21:
        action = input('Hit or Stand?: ').lower()
        if action == 'hit':
            player_hand.add_card(shoe.deal_card())
            print('Player Hand:')
            player_hand.display_cards()
            if player_hand.value > 21:
                scenarios.player_busts(player_chips)
                player_hand.is_bust = True
                break  # Stops dealing
            else:
                continue  # continues dealing
        else:
            break  # Stops dealing
    
    # Ask to play another game if player hand has busted
    if player_hand.is_bust:
        if play_again():
            continue
    
    # Continue play with dealer until hand is complete
    print('')
    print('Dealer Hand:')
    dealer_hand.display_cards(show_all=True)
    time.sleep(3)
    
    if SOFT_17 == 'stand':
        dealer_plays_until = 17
    else:
        dealer_plays_until = 18
    
    while dealer_hand.value < dealer_plays_until:
        dealer_hand.add_card(shoe.deal_card())
        time.sleep(.25)
        dealer_hand.display_cards(show_all=True)
        if dealer_hand.value > 21:
            scenarios.dealer_busts(player_chips)
            dealer_hand.is_bust = True
            break
        if dealer_hand.value > 17:
            break
        else:
            time.sleep(2.5)
    
    # Ask to play another game if dealer hand has busted
    if dealer_hand.is_bust:
        if play_again():
            continue
    
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

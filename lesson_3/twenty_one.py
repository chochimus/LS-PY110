import random
import os
import time

def display_hand(h1, h2, first_turn=False):
    os.system('clear')
    if first_turn:
        dealerline1 = f'|          {SUITE_MAP[h2[0][0]]}|  |'
        dealerline2 = f'|_________{str(h2[0][1]).rjust(2,'_')}|__|'

    else:
        dealerline1 = '|        '
        dealerline2 = '|________'

        for card in h2:
            dealerline1 += ' ' + SUITE_MAP[card[0]] + '|'
            dealerline2 += str(card[1]).rjust(2,'_') + '|'

    line1 = ''
    line2 = '|'
    line3 = '|'
    for i, card in enumerate(h1):
        value = str(card[1]).ljust(2)
        suit = SUITE_MAP[card[0]]

        if i == len(h1) - 1:
            line1 += '_' * 11
            line2 += value + ' ' * 8 + '|'
            line3 += suit + ' ' * 8 + ' |'
        else:
            line1 += '_' * 3
            line2 += value + '|'
            line3 += suit + ' |'

    print(dealerline1)
    print(dealerline2)
    print()
    print(line1)
    print(line2)
    print(line3)

def initialize_deck():
    deck = [[suite, value ] for suite in SUITES for value in VALUES]
    random.shuffle(deck)
    return deck

def deal_cards(deck):
    player_hand = []
    dealer_hand = []
    for i in range(4):
        if i % 2 == 0:
            player_hand.append(deck.pop())
        else:
            dealer_hand.append(deck.pop())
    return player_hand, dealer_hand

def total_hand(cards):
    values = [card[1] for card in cards]
    sum_val = 0
    for value in values:
        if value == 'A':
            sum_val += 11
        elif value in 'JQK':
            sum_val += 10
        else:
            sum_val += int(value)

    aces = values.count("A")
    while sum_val > 21 and aces:
        sum_val -= 10
        aces -= 1

    return sum_val

def busted(total):
    return total > 21

def play_again():
    print("----")
    answer = input("Do you want to play again? (y or n)")
    return answer == 'y'

def check_win(player_total, dealer_total):
    if player_total > 21:
        return "P_BUST"
    elif dealer_total > 21:
        return "D_BUST"
    elif player_total < dealer_total:
        return "D"
    elif player_total > dealer_total:
        return "P"
    else:
        return "T"
        
def display_win(player_total, dealer_total):
    results = check_win(player_total, dealer_total)
    
    match results:
        case "P_BUST":
            print("You busted, dealer wins!")
        case "D_BUST":
            print("Dealer busted, you win!")
        case "P":
            print("You win!")
        case "D":
            print("Dealer wins!")
        case "T":
            print("You tied!")

SUITES = ['H', 'S', 'D', 'C']
VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
SUITE_MAP = {
    'C':'♣',
    'H':'♥',
    'S':'♠',
    'D':'♦'
}
WIN_CON = 21
DEALER_LIMIT = 17

while True:
    player_busted = False
    dealer_busted = False
    deck = initialize_deck()
    player_hand, dealer_hand = deal_cards(deck)
    player_total = total_hand(player_hand)
    dealer_total = total_hand(dealer_hand)
    display_hand(player_hand, dealer_hand, True)

    if player_total == WIN_CON or dealer_total == WIN_CON:
        if dealer_total == WIN_CON:
            display_hand(player_hand, dealer_hand)
        display_win(player_total, dealer_total)
        break
    

    while True:
        if player_total == WIN_CON:
            print("You hit 21! Dealers turn...")
            time.sleep(1)
            break
        choice = input("hit or stay? (h or s)")
        if choice not in ['h', 's']:
            print("Sorry, must enter 'h' or 's'.")
            continue
        if choice == 's':
            break
        player_hand.append(deck.pop())
        player_total = total_hand(player_hand)
        if busted(player_total):
            player_busted = True
            break
        display_hand(player_hand, dealer_hand, True)
    if player_busted:
        display_hand(player_hand, dealer_hand)
        display_win(player_total, dealer_total)
        break
    else:
        print(f"You chose to stay at {player_total}.")
        time.sleep(1)

    display_hand(player_hand, dealer_hand)
    time.sleep(1)
    while dealer_total < 17:
        dealer_hand.append(deck.pop())
        dealer_total = total_hand(dealer_hand)
        display_hand(player_hand, dealer_hand)
        time.sleep(1)
    if busted(dealer_total):
        display_hand(player_hand, dealer_hand)
        display_win(player_total, dealer_total)
        break

    print(f"Dealer stays at {dealer_total}")
    display_win(player_total, dealer_total)
    break
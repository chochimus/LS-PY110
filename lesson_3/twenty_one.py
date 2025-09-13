import random
import os
import time

SUITE_MAP = {
    'C':'♣',
    'H':'♥',
    'S':'♠',
    'D':'♦'
}
def display_hand(h1, h2, first_turn=False):
    os.system('clear')
    if first_turn:
        dealerline1 = f'|          {SUITE_MAP[h2[0][0]]}|  |'
        dealerline2 = f'|_________{str(h2[0][1]).rjust(2,'_')}|__|'

    else:
        dealerline1 = '|        '
        dealerline2 = '|________'

        for i in range(len(h2)):
            dealerline1 += ' ' + SUITE_MAP[h2[i][0]] + '|'
            dealerline2 += str(h2[i][1]).rjust(2,'_') + '|'

    line1 = ''
    line2 = '|'
    line3 = '|'
    for i in range(len(h1)):
        value = str(h1[i][1]).ljust(2)
        suit = SUITE_MAP[h1[i][0]]

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

def shuffle_deck(deck):
    random.shuffle(deck)

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

def busted(cards):
    return total_hand(cards) > 21

def hit(cards):
    return deck.pop()

SUITES = ['H', 'S', 'D', 'C']
VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


deck = [[suite, value ] for suite in SUITES for value in VALUES]

shuffle_deck(deck)
player_hand, dealer_hand = deal_cards(deck)

while True:
    player_busted = False
    dealer_busted = False
    display_hand(player_hand, dealer_hand, True)
    if total_hand(player_hand) == 21 and total_hand(dealer_hand) == 21:
        display_hand(player_hand, dealer_hand)
        print("You tied!")
        break
    elif total_hand(player_hand) == 21:
        print("You won!")
        break
    elif total_hand(dealer_hand) == 21:
        display_hand(player_hand, dealer_hand)
        print("Dealer won!")
        break

    while True:
        if total_hand(player_hand) == 21:
            print("You hit 21! Dealers turn...")
            time.sleep(1)
            break
        choice = input("hit or stay? (h or s)")
        if choice == 's':
            break
        player_hand.append(hit(player_hand))
        if busted(player_hand):
            player_busted = True
            break
        display_hand(player_hand, dealer_hand, True)
    if player_busted:
        display_hand(player_hand, dealer_hand, True)
        print("You busted, dealer wins!")
        break
    else:
        print("You chose to stay.")
        time.sleep(1)

    display_hand(player_hand, dealer_hand)
    time.sleep(1)
    while total_hand(dealer_hand) < 17:
        dealer_hand.append(hit(dealer_hand))
        if busted(dealer_hand):
            dealer_busted = True
            break
        display_hand(player_hand, dealer_hand)
        time.sleep(2)
    if dealer_busted:
        display_hand(player_hand, dealer_hand)
        print("You win!")
        break
    else:
        if total_hand(player_hand) > total_hand(dealer_hand):
            print("You win!")
            break
        elif total_hand(player_hand) == total_hand(dealer_hand):
            print("You tied!")
            break
        else:
            print("Dealer wins!")
            break
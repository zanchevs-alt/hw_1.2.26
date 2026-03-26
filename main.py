"""
♦️❤️♠️♣️ Homework – Loops & Random Games ♦️❤️♠️♣️
Card Game: WAR
Objective
Build a simple card game between a player and the computer
The goal is to be the first to reach 10 points

Game Rules
The player gets one random card

The computer gets one random card

Card values:

A (Ace) → highest
K (King)
Q (Queen)
J (Jack)
10, 9, 8, .... 2
Use this code to generate random cards: click here

Scoring Rules
Player card > Computer card → Player gets +1 point
Computer card > Player card → Computer gets +1 point
Draw (same value) → 0 points to both
Game Flow
Start both scores at 0

Repeat rounds:

Deal one card to the player
Deal one card to the computer
Show both cards and their values
Update scores according to the rules
The game ends when:

Player score reaches 10 → Player wins
Computer score reaches 10 → Computer wins
Example Round
Player card: K ♠️
Computer card: 7 ♦️

Player wins the round (+1 point)
Score:
Player: 4
Computer: 3
Example Draw
Player card: 9 ❤️
Computer card: 9 ♣️

Draw – no points awarded
"""

import random

card_number = random.choice(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'])
card_suit = random.choice(['♠️', '♦️', '❤️', '♣️'])

print(card_number, card_suit)

computer_score = 0
player_score = 0

while True:
    computer_card_number = random.randint(2,14)
    computer_card_suit = random.choice(['♠️', '♦️', '❤️', '♣️'])

    print('computer:', end="")

    if computer_card_number <= 10:
        display_number = computer_card_number
    elif computer_card_number == 11:
        display_number = 'J'
    elif computer_card_number == 12:
        display_number = 'Q'
    elif computer_card_number == 13:
        display_number = 'K'
    elif computer_card_number == 14:
        display_number = 'A'

    print(display_number, computer_card_suit)

    player_card_number = random.randint(2,14)
    player_card_suit = random.choice(['♠️', '♦️', '❤️', '♣️'])

    print('player:', end="")

    if player_card_number <= 10:
        display_number = player_card_number
    elif player_card_number == 11:
        display_number = 'J'
    elif player_card_number == 12:
        display_number = 'Q'
    elif player_card_number == 13:
        display_number = 'K'
    elif player_card_number == 14:
        display_number = 'A'

    print(display_number, player_card_suit)

    if player_card_number > computer_card_number:
        player_score += 1
        print('player won!')
    elif player_card_number < computer_card_number:
        computer_score += 1
        print('computer won!')
    else:
        print('draw')

    print('player_score:', player_score, 'computer_score:', computer_score)

    if computer_score >= 10 or player_score >= 10:
        break

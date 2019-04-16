# 19.blackjack_advice.py
import random
cards = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}

# SOOO I THOUGHT WE WERE GENERATING RANDOM CARDS FOR THE USER... LOL.
# card = random.choice(list(cards))
# #card is key, cards[card] is value
# print(card, cards[card])
# print(f'Whatsyour first card? {card}')
###########

def main():
    again = True

    while again:
        card_1 = input('What\'s your first card? ')
        card_2 = input('What\'s your second card? ')
        card_3 = input('What\'s your third card? ')

        sum = cards[card_1] + cards[card_2] + cards[card_3]

        if sum < 17:
            print(f'{sum} Hit')
        elif 17 < sum < 21:
            print(f'{sum} Stay')
        elif sum == 21:
            print(f'{sum} Blackjack!')
        else:
            print(f'{sum} Already Busted')

        while True:
            replay = input('Do you want to play again? ').strip().lower()
            if replay in ['yes', 'y', 'no', 'n']:
                break
        if replay.startswith('n'):
            again = False
            print('Goodbye!')

if __name__ == '__main__':
    main()

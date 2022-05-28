#BLACKJACK 2.0 editar

import random

card = 2, 3, 4, 5, 6, 7, 8, 9, 10, 'AS', 'J', 'Q', 'K'
pale = '♠', '♥', '♦', '♣'
def game():
    print('empiece a jugar')

def card_generator(card, pale):

    random_num_fig_player = random.choice(card)
    random_pale_player = random.choice(pale)
    random_num_fig_crupier = random.choice(card)
    random_pale_crupier = random.choice(pale)
    print(random_num_fig_player, random_pale_player)

#BLACKJACK 2.0

import random


#funcion de generacion de carta random
cards = 2, 3, 4, 5, 6, 7, 8, 9, 10, 'AS', 'J', 'Q', 'K'
pale = 'de Picas ♠', 'de Corazones ♥', 'de Rombos ♦', 'de Tréboles ♣'



def card_value_generator(cards):

    random_num_fig_player = random.choice(cards)
    if random_num_fig_player == 'J' or random_num_fig_player == 'Q' or random_num_fig_player == 'K':
      random_num_fig_player_value = 10
    elif random_num_fig_player == 'AS':
      random_num_fig_player_value = 11
    else:
        random_num_fig_player_value = random_num_fig_player
    print(random_num_fig_player)
    return random_num_fig_player

def card_pale_generator(pale):
    random_pale_player = random.choice(pale)
def main_game():
    option = None
    card_player_count = 0
    card_player_value = 0
    player_name = str(input('Ingrese su nombre --> '))
    print('Bienvenido', player_name, '!, ahora ingrese su monto')
    amount_money_box = int(input("ingrese la cantidad de dinero que desea tener en su pozo \nel monto no debe ser menor a 0 ni mayor a 100000$ -->"))
    while amount_money_box > 100000 or amount_money_box <= 0:
        print("no se puede ingresar una cantidad superior a 100000$ ni menor o igual a 0")
        amount_money_box = int(input("ingrese la cantidad de dinero deseada --> "))
    while option != 3:
        print("MENU")
        print(18*"-")
        print("1 - Apostar\n2 - Jugar una mano\n3 - Salir")
        option = int(input("elija la opcion deseada --> "))
        # hacer la despedida
        print('\n\n')
        if option == 1:
            while amount_money_box_plus <= 0:
                print("no se puede ingresar una cantidad superior a 100000$ ni menor o igual a 0")
                amount_money_box_plus = int(input("ingrese la cantidad de dinero deseada --> "))
                if (amount_money_box_plus % 5) == 0 and (amount_money_box_plus + amount_money_box) <= 100000:
                    amount_money_box += amount_money_box_plus
                else:
                    print('El monto ingresado no es multiplo de 5 o el total entre este monto y el primero supera la cantidad de cien mil pesos')
        elif option == 2:
            card_player_value += card_generator(cards, pale)
            card_player_count += 1
main_game()

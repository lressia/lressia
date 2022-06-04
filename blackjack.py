#BLACKJACK 2.0
import random


def as_control(score,card_value):
    value = card_value
    if score >= 11 and card_value == 11:
        value = 1
        
    return value


def card_generator():
    value = (11,2,3,4,5,6,7,8,9,10,10,10,10)
    names = (" -AS"," -2"," -3"," -4"," -5"," -6"," -7"," -8"," -9"," -10"," -J"," -Q"," -K")
    pales = (" de picas"," de corazones"," de diamantes"," de treboles")
    index = random.randint(0,12)
    pale = str(random.choice(pales))

    return names[index],pale,value[index]


def natural_control(player_score, crupier_score):
    winner = 0
    winner_state = False
    if player_score == 21:
        winner = player_score
        winner_state = True
    if crupier_score == 21:
        winner = crupier_score
        winner_state = True
    if player_score == 21 and crupier_score == 21:
        winner = 0
        winner_state = False
    return winner_state, winner


def check_result(player_name,player_score,bet,crupier_score,winner):
    amount_money_box = 0
    winer = None
    winner = winner
    message = None
    if winner == True:
        message = (player_name," gano por black jack natural")
        amount_money_box += bet
        winer = 1
    elif player_score <= 21:
        if crupier_score > 21:
            message =("El crupier se paso de 21 y ", player_name, "gana con ",player_score, "puntos")
            amount_money_box += bet
            winer = 1
        elif player_score > crupier_score:
            message = (player_name, "gana con ", player_score, "puntos")
            amount_money_box += bet
            winer = 1
        elif player_score == crupier_score:
            message = (player_name, "y el crupier empatan con ", crupier_score, "puntos")
            amount_money_box = 0
            winer = 0
        else:
            message = ("El crupier gano con ", crupier_score, "puntos")
            amount_money_box -= bet
            winer = 2
    elif crupier_score > 21:
        message = (player_name, "y el crupier se pasaron de 21, así que el crupier gana")
        amount_money_box -= bet
        winer = 0

    else:
        message = (player_name, "se paso de 21 y el crupier gano con ", crupier_score, "puntos")
        amount_money_box -= bet
        winer = 2

    return message, amount_money_box, winer


def main_game():
    option = None
    amount_money_box = 0
    acu_amount_money_box = 0
    act_amount_money_box = 1
    amount_money_box_plus = 0
    winner = False
    bet = None
    card_player_count = 0
    card_player_value = 0
    victory_player = 0
    victory_crupier = 0
    victory_crupier_flag = False
    racha_crupier = 0
    cont_games = 0
    cant_blackjack_nat = 0
    player_name = False
    total_cards_player = None
    total_cards_crupier = None
    amount_money_box_max = None
    max_bet_lost = None
    flag_finish_game = False
    finish_racha_crupier = None

    # PEDIDO DE NOMBRE Y CANTIDAD DE DINERO
    player_name = str(input('Ingrese su nombre --> '))
    print('\nBienvenido', player_name, '!')
    amount_money_box = int(input("\nIngrese la cantidad de dinero que desea tener en su pozo para comenzar\nEl monto no debe ser menor a 0 ni mayor a 100000$ --> "))
    while amount_money_box > 100000 or amount_money_box <= 0:
        print("no se puede ingresar una cantidad superior a 100000$ ni menor o igual a 0")
        amount_money_box = int(input("ingrese la cantidad de dinero deseada --> "))
    acu_amount_money_box = amount_money_box
    if amount_money_box_max == None:
        amount_money_box_max = amount_money_box

    while option != 3:
        print("\nMENU")
        print(18*"-")
        print("1 - Apostar\n2 - Jugar una mano\n3 - Salir")
        print(18*"-")
        option = int(input("Elija la opcion deseada --> "))

        #OPCION DE APUESTA
        if option == 1:
            amount_money_box_plus = 0
            while amount_money_box_plus <= 0 or amount_money_box_plus > 100000:
                print("\nNo se puede ingresar una cantidad superior a 100000$ ni menor o igual a 0")
                amount_money_box_plus = int(input("\nIngrese la cantidad de dinero deseada --> "))
                if (amount_money_box_plus + amount_money_box) <= 100000:
                    amount_money_box += amount_money_box_plus
                    act_amount_money_box += 1
                    acu_amount_money_box += amount_money_box
                else:
                    print('\nEl monto ingresado es menor o igual a 0 o... \nEl total entre este monto y el primero supera la cantidad de 100000')
                    amount_money_box_plus = 0
        #OPCION DE JUGAR UNA MANO
        elif option == 2:
            if amount_money_box == 0 or amount_money_box < 5:
                print("\nNo tiene sificiente dinero. Volviendo al menu principal")
                continue
            print("\nSu saldo disponible es :", amount_money_box)
            bet = int(input("\nIngresar un apuesta inferior o igual al saldo disponible --> "))
            while bet > amount_money_box or bet <= 0 or (bet % 5) != 0:
                if bet % 5 != 0:
                    print("\nLa apuesta debe ser múltiplo de 5. Ingrese otra vez: ")
                elif bet > amount_money_box:
                    print("\nNo cuentas con suficiente dinero para realizar esta apuesta")
                elif bet <= 0:
                    print("\nLa apuesta debe ser mayor que 0. Ingrese otra vez: ")
                bet = int(input("\ningresar un apuesta inferior o igual al saldo disponible --> "))
            if bet == None:
                print("\nDebes apostar antes de jugar")
            else:
                #return name,pale,value
                #GENERACION DE CARTAS DEL CRUPIER
                card1_crupier = card_generator()
                crupier_score = card1_crupier[2]
                name_crupier_card1 = card1_crupier[0] + card1_crupier[1]
                total_cards_crupier = name_crupier_card1

                #GENERACION DE CARTAS DEL JUGADOR
                card_player_1 = card_generator()
                player_score = card_player_1[2]
                card_player_2 = card_generator()

                #CONTROL DE AS
                value_card = as_control(player_score,card_player_2[2])
                player_score += value_card

                #ACUMULADOR DE CARTAS
                name_player_card1 = card_player_1[0] + card_player_1[1]
                name_player_card2 = card_player_2[0] + card_player_2[1]
                total_cards_player = name_player_card1 + name_player_card2

                print("\nLas primeras dos cartas de ", player_name, " son: \n--> ", total_cards_player, "\nla carta del crupier es: \n--> ",total_cards_crupier)

                #CONTROL BLACK JACK NATURAL
                control = natural_control(player_score, crupier_score)
                winner = control[0]

                if winner == True:
                    cant_blackjack_nat += 1
                else:
                    #GENERACION DE CARTAS DEL JUGADOR
                    print()
                    print("\nSEGUIR JUEGO\n")
                    print("\n1 - Si desea sacar otra carta\n0 - Si desea plantarse")
                    print()
                    decision = int(input("\nIngrese la opcion deseada --> "))

                    while decision != 1 and decision != 0:
                        print("\nDebe ingresar una opcion valida")
                        print()
                        print("\n1 - Si desea sacar otra carta\n0 - Si desea plantarse")
                        print()
                        decision = int(input("\nIngrese la opcion deseada --> "))
                        print()

                    while player_score < 21 and decision == 1:
                        #CARTAS SIGUIENTES DEL JUGADOR
                        player_card = card_generator()
                        #VARIABLES ACUMULADORAS
                        card = player_card[0] + player_card[1]
                        value_card = as_control(player_score,player_card[2])
                        player_score += value_card
                        print(player_name, " saco la carta--> ", player_card[0] + player_card[1], "\nel puntaje actual de ", player_name, " es--> ", player_score)
                        total_cards_player += card
                        if player_score < 21:
                            #MENU PARA EL JUGADOR
                            print()
                            print("\nSEGUIR JUEGO\n")
                            print("\n 1 - Si desea sacar otra carta\n0 - Si desea plantarse")
                            print()
                            decision = int(input("ingrese la opcion deseada --> "))
                            while decision != 1 or 0:
                                print("\nDebe ingresar una opcion valida")
                                print()
                                print("1 - Si desea sacar otra carta\n0 - Si desea plantarse")
                                print()
                                decision = int(input("\nIngrese la opcion deseada --> "))
                    if decision == 0:
                        print(player_name, " se plantó")
                    if player_score > 21:
                        print(player_name," se pasó")

                    #GENERACION DE CARTAS DEL CRUPIER
                while crupier_score < 21 and crupier_score < 17:
                    if crupier_score < 17:
                        #GENERACION DE CARTA DEL CRUPIER
                        crupier_card = card_generator()
                        #VARIABLE PARA ACUMULAR
                        card = crupier_card[0] + crupier_card[1]
                        value_card = as_control(crupier_score,crupier_card[2])
                        crupier_score += value_card
                        total_cards_crupier += card
                if winner == False:
                    if crupier_score >= 17 and crupier_score <= 21:
                        print("El crupier se plantó")
                    elif crupier_score > 21:
                        print("El crupier se pasó")
                print("\n")
                result = check_result(player_name, player_score, bet, crupier_score,winner)
                print(result[0])
                print("\nEl saldo de ", player_name, " antes de esta mano era de:", amount_money_box)
                print("La apuesta de ", player_name, " fue de:", bet)
                print("El saldo actual de ", player_name, " es de:", (amount_money_box + result[1]))
                print("Las cartas de ", player_name, " fueron:", total_cards_player)
                print("Las cartas del crupier fueron:",total_cards_crupier)

                            #PROCESOS
                flag_finish_game = True
                if result[2] == 2 or result[2] == 0:
                    victory_crupier_flag = True
                    victory_crupier += 1
                    if max_bet_lost == None:
                        max_bet_lost = bet
                    elif bet > max_bet_lost:
                        max_bet_lost = bet
                else:
                    victory_crupier_flag = False
                    victory_crupier = 0
                    racha_crupier = 0
                if victory_crupier_flag == True:
                    racha_crupier = victory_crupier
                if finish_racha_crupier == None:
                    finish_racha_crupier = racha_crupier
                elif racha_crupier > finish_racha_crupier:
                    finish_racha_crupier = racha_crupier
                if result[2] == 1:
                    victory_player += 1
                cont_games += 1
                amount_money_box += result[1]
                #POZO
                if amount_money_box > amount_money_box_max:
                    amount_money_box_max = amount_money_box
                act_amount_money_box += 1
                acu_amount_money_box += amount_money_box
        elif option != 1 and option != 2:
            print("\nElija una opción válida\n")
    if option == 3:
        if flag_finish_game == False:
            print("\nNo se concreto ninguna partida")
        else:
            print("\n\n")
            print("ESTADISTICAS DEL JUEGO")
            print("\nEl porcentaje de victorias del jugador es: ",(victory_player*100)/cont_games)
            print("Cantidad de manos donde hubo un black jack natural: ",cant_blackjack_nat)
            print("Monto maximo de",player_name,"en el pozo: ",amount_money_box_max)
            print("La cantidad promedio de dinero que tuvo ",player_name," en su pozo fue: ",acu_amount_money_box / act_amount_money_box)
            print("La racha de victorias mas larga del crupier fue de ", racha_crupier," victorias")
            print("La apuesta mas grande que perdio ",player_name," fue de ",max_bet_lost,"$")

main_game()

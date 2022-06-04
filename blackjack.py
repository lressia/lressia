#BLACKJACK 2.0

import random


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

def check_result(player_name, player_score, bet, crupier_score):
    amount_money_box = 0
    winner_player = 0
    losser_player = 0
    message = None
    if player_score <= 21:
        if crupier_score > 21:
            message =("El crupier se paso de 21 y ", player_name, "gana con ",player_score, "puntos")
            amount_money_box = bet * 2
            winner_player += 1
        elif player_score > crupier_score:
            message = (player_name, "gana con ", player_score, "puntos")
            amount_money_box = bet * 2
            winner_player += 1
        elif player_score == crupier_score:
            message = (player_name, "y el crupier empatan con ", crupier_score, "puntos")
            amount_money_box = bet
        else:
            message = ("El crupier gano con ", crupier_score, "puntos")
            amount_money_box -= bet
            losser_player += 1
    elif crupier_score > 21:
        message = (player_name, "y el crupier se pasaron de 21, así que el crupier gana")
        amount_money_box -= bet
        losser_player += 1
    else:
        message = (player_name, "se paso de 21 y el crupier gano con ", crupier_score, "puntos")
        amount_money_box -= bet
        losser_player += 1
    return message, amount_money_box, winner_player, losser_player

def winner_times(winner_player, rounds):

    result = (winner_player * 100) // rounds
    return result

def main_game():
    option = None
    amount_money_box_plus = 0
    winner = False
    bet = None
    card_player_count = 0
    card_player_value = 0
    victory_player = 0
    victory_crupier = 0
    cant_blackjack_nat = 0
    player_name = False
    round = 0
    winner_times = 0

    # PEDIDO DE NOMBRE Y CANTIDAD DE DINERO
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

        #OPCION DE APUESTA
        if option == 1:
            amount_money_box_plus = int(input("Ingrese la cantidad de dinero deseada: "))
            while amount_money_box_plus <= 0 or amount_money_box_plus > 100000:
                print("no se puede ingresar una cantidad superior a 100000$ ni menor o igual a 0")
                amount_money_box_plus = int(input("ingrese la cantidad de dinero deseada --> "))
                if (amount_money_box_plus + amount_money_box) <= 100000:
                    amount_money_box += amount_money_box_plus
                else:
                    print('El total entre este monto y el primero supera la cantidad de cien mil pesos')
            else:
                if (amount_money_box_plus + amount_money_box) <= 100000:
                    amount_money_box += amount_money_box_plus
            amount_money_box_plus = 0

        #OPCION DE JUGAR UNA MANO
        elif option == 2:

            round = 1
            print("Su saldo disponible es:", amount_money_box)
            bet = int(input("ingresar un apuesta inferior o igual al saldo disponible --> "))
            while bet > amount_money_box or bet <= 0 or (bet % 5) != 0:

                if bet % 5 != 0:
                    print("La apuesta debe ser múltiplo de 5. Ingrese otra vez: ")
                elif bet > amount_money_box:
                    print("no cuentas con suficiente dinero para realizar esta apuesta")
                elif bet <= 0:
                    print("La apuesta debe ser mayor que 0. Ingrese otra vez: ")
                bet = int(input("ingresar un apuesta inferior o igual al saldo disponible --> "))
            if bet == None:
                print("debes apostar antes de jugar")
            else:
                #return name,pale,value
                #GENERACION DE CARTAS DEL CRUPIER
                card1_crupier = card_generator()
                crupier_score = card1_crupier[2]
                name_crupier_card1 = card1_crupier[0] + card1_crupier[1]
                total_cards_crupier = name_crupier_card1

                #GENERACION DE CARTAS DEL JUGADOR
                card_player_1 = card_generator()
                card_player_2 = card_generator()
                player_score = card_player_1[2] + card_player_2[2]
                name_player_card1 = card_player_1[0] + card_player_1[1]
                name_player_card2 = card_player_2[0] + card_player_2[1]
                total_cards_player = name_player_card1 + name_player_card2


                print("las primeras dos cartas de ", player_name,
                      " son: \n--> ", total_cards_player, "\nla carta del crupier es: \n--> ",total_cards_crupier)

                #CONTROL BLACK JACK NATURAL
                control = natural_control(player_score, crupier_score)
                winner = control[0]
                if winner == True:
                    result = check_result(player_name, player_score, bet, crupier_score)
                    print("el saldo de ", player_name, " antes de esta mano era de:", amount_money_box)
                    print("la apuesta de ", player_name, " fue de:", bet)
                    print("el saldo actual de ", player_name, " es de:", (amount_money_box + result[1]))
                    print("las cartas de ", player_name, " fueron:", total_cards_player, "y su puntaje es: ", player_score)
                    print("las cartas del crupier fueron:", total_cards_crupier, "y su puntaje es: ", crupier_score)
                while player_score < 21:
                    print("1 - Jugar otra mano\n2 - Salir")
                    option = int(input("elija la opcion deseada --> "))
                    while option != 2:
                        while option != 1:
                            print('Introduzca un caracter valido')
                            print("1 - Jugar otra mano\n2 - Salir")
                            option = int(input("elija la opcion deseada --> "))
                        else:
                            round += 1
                            #GENERACION DE CARTA DEL JUGADOR
                            card_player_1 = card_generator()
                            player_score += card_player_1[2]
                            name_player_card1 = card_player_1[0] + card_player_1[1]
                            total_cards_player += name_player_card1
                    else:
                        result = check_result(player_name, player_score, bet, crupier_score)
                        winner_message = result[0]
                        winner_score = result[2]
                        winner_times = winner_times(winner_score, round)
                        print(winner_message)
                        print("el saldo de ", player_name, " antes de esta mano era de:", amount_money_box)
                        print("la apuesta de ", player_name, " fue de:", bet)
                        print("el saldo actual de ", player_name, " es de:", (amount_money_box + result[1]))
                        print("las cartas de ", player_name, " fueron:", total_cards_player, "y su puntaje es: ", player_score)
                        print("las cartas del crupier fueron:", total_cards_crupier, "y su puntaje es: ", crupier_score)
                while crupier_score < 21:
                    print("1 - Jugar otra mano\n2 - Salir")
                    option = int(input("elija la opcion deseada --> "))
                    while option != 2:
                        while option != 1:
                            print('Introduzca un caracter valido')
                            print("1 - Jugar otra mano\n2 - Salir")
                            option = int(input("elija la opcion deseada --> "))
                        else:

                            round += 1
                            #GENERACION DE CARTA DEL CRUPIER
                            card1_crupier = card_generator()
                            crupier_score += card1_crupier[2]
                            name_crupier_card1 = card1_crupier[0] + card1_crupier[1]
                            total_cards_crupier += name_crupier_card1
                            if crupier_score >= 17 and crupier_score <= 21:
                                print("el crupier se planto")
                            elif crupier_score > 21:
                                print("el crupier se paso")
                    else:
                        result = check_result(player_name, player_score, bet, crupier_score)
                        winner_message = result[0]
                        winner_score = result[2]
                        winner_times = winner_times(winner_score, round)
                        print(winner_message)
                        print("el saldo de ", player_name, " antes de esta mano era de:", amount_money_box)
                        print("la apuesta de ", player_name, " fue de:", bet)
                        print("el saldo actual de ", player_name, " es de:", (amount_money_box + result[1]))
                        print("las cartas de ", player_name, " fueron:", total_cards_player, "y su puntaje es: ", player_score)
                        print("las cartas del crupier fueron:", total_cards_crupier, "y su puntaje es: ", crupier_score)
                        print("El procentaje de victorias del jugador fue de:", winner_times[0], "%")

main_game()

# 21 BLACKJACK

# # Titulo general y carga de datos ... BLACKJACK
# name_player = input('Ingrese su nombre para continuar: ')
#
# #Definicion de variables...
# simb_poker = '♣♦♥♠-'
# simb_replicado = simb_poker * 20
#
# import random
#
# cartas = 2, 3, 4, 5, 6, 7, 8, 9, 10, 'AS', 'J', 'Q', 'K'
# palos = 'de Picas ♠', 'de Corazones ♥', 'de Rombos ♦', 'de Tréboles ♣'
#
# #INTERFAZ...
# print()
# print("¡WELCOME TO BLACKJACK!:", name_player, '\n')
# print('Reglas del juego: Jugaras una única mano de 2 o 3 rondas contra el crupier para determinar el ganador\nEl ganador será quien haya alcanzado un puntaje más cercano a 21 sin pasarse.\n')
# print(simb_replicado, '\n')
#
# # GENERADOR DE CARTAS ALEATORIAS
#
#
# # GENERACION DE LA PRIMERA CARTA
#
# random_num_fig_player = random.choice(cartas)
# random_pale_player = random.choice(palos)
# random_num_fig_crupier = random.choice(cartas)
# random_pale_crupier = random.choice(palos)
#
# card_player_r1 = random_num_fig_player , random_pale_player
# card_crupier_r1 = random_num_fig_crupier ,  random_pale_crupier
#
#
#
# #PUNTUACION PARCIAL RONDA 1
# player_sum_r1 = 0
# crupier_sum_r1 = 0
# player_sum_as_r1 = 0
# crupier_sum_as_r1 = 0
# con_fig_r1 = 0
# con_as_r1 = 0
#
# #JUGADOR_RONDA_1
#
# if random_num_fig_player == 'J' or random_num_fig_player == 'Q' or random_num_fig_player == 'K':
#   player_sum_r1 += 10
#   con_fig_r1 += 1
# elif random_num_fig_player == 'AS':
#   con_as_r1 += 1
#   player_sum_r1 += 11
#   player_sum_as_r1 = 1
# else:
#   player_sum_r1 += random_num_fig_player
#
# #CRUPIER_RONDA_1
#
# if random_num_fig_crupier == 'J' or random_num_fig_crupier == 'Q' or random_num_fig_crupier == 'K':
#   con_fig_r1 += 1
#   crupier_sum_r1 += 10
# elif random_num_fig_crupier == 'AS':
#   con_as_r1 += 1
#   crupier_sum_r1 += 11
#   crupier_sum_as_r1_r1 = 1
# else:
#   crupier_sum_r1 += random_num_fig_crupier
#
#
#
# #RESULTADOS DE LA RONDA 1
# input('Presionar ENTER para que comience el juego!')
# print('RONDA 1\n')
# print(name_player, 'tu carta fue:', random_num_fig_player, random_pale_player, ' obtienes +', player_sum_r1, 'puntos')
# print('La carta del Crupier fue:', random_num_fig_crupier, random_pale_crupier, ' obtiene +', crupier_sum_r1, 'puntos\n')
#
# #COMPARAR EL PALO, NUM Y FIG DE LAS CARTAS EN LA PRIMERA RONDA
#
# if con_fig_r1 == 2:
#   if random_num_fig_player == random_num_fig_crupier:
#       if random_pale_player == random_pale_crupier:
#           print('ALUCINANTE! Has obtenido la misma figura con el mismo palo que el Crupier')
#       else:
#           print('Has obtenido la misma figura que el Crupier pero con distinto palo')
#   else:
#       print('Ambos han obtenido una figura, pero no hay coincidencias')
# else:
#   if con_as_r1 == 2:
#       if random_pale_player == random_pale_crupier:
#           print('INSANO! Obtuviste un AS con el mismo palo que el crupier. De locos!')
#       else:
#           print('Ambos han obtenido un AS pero con distinto palo')
#   else:
#       if random_num_fig_player == random_num_fig_crupier:
#
#           if random_pale_player == random_pale_crupier:
#               print('INCREIBLE! Has obtenido el mismo número con el mismo palo que el Crupier')
#           else:
#               print('Has obtenido el mismo número que el Crupier pero con distino palo')
#       else:
#           if random_pale_player == random_pale_crupier:
#               print('Hubo coincidencia de palos')
#           else:
#               print('No hubo coincidencias de palos')
#
# #GENERACION DE LA SEGUNDA CARTA
# random_num_fig_player = random.choice(cartas)
# random_pale_player = random.choice(palos)
# random_num_fig_crupier = random.choice(cartas)
# random_pale_crupier = random.choice(palos)
#
# card_player_r2 = random_num_fig_player , random_pale_player
# card_crupier_r2 = random_num_fig_crupier , random_pale_crupier
#
#
# #PUNTUACION_PARCIAL_RONDA 2
# player_sum_r2 = 0
# crupier_sum_r2 = 0
# player_sum_as_r2 = 0
# crupier_sum_as_r2 = 0
# con_fig_r2 = 0
# con_as_r2 = 0
#
# #JUGADOR_RONDA_2
#
# if random_num_fig_player == 'J' or random_num_fig_player == 'Q' or random_num_fig_player == 'K':
#   player_sum_r2 += 10
#   con_fig_r2 += 1
# elif random_num_fig_player == 'AS':
#   con_as_r2 += 1
#   if (player_sum_r1 + 11) < 21:
#       player_sum_r2 = 11
#       player_sum_as_r2 = 1
#   else:
#       player_sum_r2 += 1
#       player_sum_as_r2 = 1
# else:
#   player_sum_r2 += random_num_fig_player
#
# #CRUPIER_RONDA_2
#
# if random_num_fig_crupier == 'J' or random_num_fig_crupier == 'Q' or random_num_fig_crupier == 'K':
#   crupier_sum_r2 += 10
#   con_fig_r2 += 1
# elif random_num_fig_crupier == 'AS':
#   if (crupier_sum_r1 + 11) < 21:
#       crupier_sum_r2 += 11
#       crupier_sum_as_r2 = 1
#   else:
#       crupier_sum_r2 += 1
#       crupier_sum_as_r2 = 1
# else:
#   crupier_sum_r2 += random_num_fig_crupier
#
# #RESULTADOS DE LA RONDA 2
#
# print('\n',simb_replicado,'\n')
#
# input('Presione Enter para jugar la Ronda 2')
# print('RONDA 2\n')
# print(name_player, 'tu carta fue:', random_num_fig_player, random_pale_player, ' Obtienes +', player_sum_r2, 'puntos' )
# print('La carta del crupier fue:', random_num_fig_crupier, random_pale_crupier, ' Obtiene +', crupier_sum_r2, 'puntos\n')
#
# #COMPARAR EL PALO DE LAS CARTAS EN LA SEGUNDA RONDA
#
# if con_fig_r2 == 2:
#   if random_num_fig_player == random_num_fig_crupier:
#       if random_pale_player == random_pale_crupier:
#           print('ALUCINANTE! Has obtenido la misma figura con el mismo palo que el Crupier')
#       else:
#           print('Has obtenido la misma figura que el Crupier pero con distinto palo')
#   else:
#       print('Ambos han obtenido una figura, pero no hay coincidencias de palos')
# else:
#   if con_as_r2 == 2:
#       if random_pale_player == random_pale_crupier:
#           print('INSANO! Obtuviste un AS con el mismo palo que el crupier. De locos')
#       else:
#           print('Ambos han obtenido un AS pero con distinto palo')
#   else:
#       if random_num_fig_player == random_num_fig_crupier:
#           if random_pale_player == random_pale_crupier:
#               print('INCREIBLE! Has obtenido el mismo número con el mismo palo que el Crupier')
#           else:
#               print('Has obtenido el mismo número que el Crupier pero con distino palo')
#       else:
#           if random_pale_player == random_pale_crupier:
#               print('Hubo coincidencia de palos')
#           else:
#               print('No hubo coincidencias de palos')
#
# #PUNTOS DE R1 Y R2 SUMADOS
#
# ptos_player_r1_r2 = player_sum_r1 + player_sum_r2
# ptos_crupier_r1_r2 = crupier_sum_r1 + crupier_sum_r2
#
# #RESULTADO DE LOS PUNTOS DE LA RONDA 1 Y 2 DEL JUGADOR
#
# print('\n',simb_replicado,'\n')
# print(name_player, 'Tu puntuación hasta el momento es de: ', ptos_player_r1_r2, 'puntos\n')
# print('La puntuación del crupier hasta el momomento es de: ', ptos_crupier_r1_r2, 'puntos\n')
#
# #TERCERA Y ULTIMA RONDA
#
# #RESULTADOS DE LA RONDA 3
# print(simb_replicado,'\n')
# input('Presione Enter para continuar con la 3ra Ronda')
# print('RONDA 3\n')
#
# #GENERACION DE LA TERCERA CARTA DEL JUGADOR Y PUNTUACION OBTENIDA
#
# #JUGADOR_RONDA_3
#
# player_sum_r3 = 0
# crupier_sum_r3 = 0
# ptos_player_r1_r2_r3 = ptos_player_r1_r2
# ptos_crupier_r1_r2_r3 = ptos_crupier_r1_r2
# con_fig_r3 = 0
# con_as_r3 = 0
# con_card_r3 = 0
#
# #3RA RONDA PLAYER
#
# if ptos_player_r1_r2_r3 < 17:
#   random_num_fig_player = random.choice(cartas)
#   random_pale_player = random.choice(palos)
#   con_card_r3 += 1
#
#   if random_num_fig_player == 'J' or random_num_fig_player == 'Q' or random_num_fig_player == 'K':
#       player_sum_r3 += 10
#       ptos_player_total = ptos_player_r1_r2 + player_sum_r3
#       con_fig_r3 +=1
#       print(name_player, 'tu carta fue: ', random_num_fig_player, random_pale_player, ' Obtienes +', player_sum_r3, 'puntos')
#
#   elif random_num_fig_player == 'AS':
#       con_as_r3 += 1
#       if (ptos_player_r1_r2 + 11) < 21:
#           player_sum_r3 += 11
#           ptos_player_total = ptos_player_r1_r2 + player_sum_r3
#           print(name_player, 'tu carta fue: ', random_num_fig_player, random_pale_player, ' Obtienes +', player_sum_r3, 'puntos')
#       else:
#           player_sum_r3 += 1
#           ptos_player_total = ptos_player_r1_r2 + player_sum_r3
#           print(name_player, 'tu carta fue: ', random_num_fig_player, random_pale_player, ' Obtienes +', player_sum_r3, 'puntos')
#   else:
#       player_sum_r3 += random_num_fig_player
#       ptos_player_total = ptos_player_r1_r2 + player_sum_r3
#       print(name_player, 'tu carta fue: ', random_num_fig_player, random_pale_player, ' Obtienes +', player_sum_r3, 'puntos')
# else:
#   ptos_player_total = ptos_player_r1_r2_r3
#   player_sum_r3 = print('Ya no puedes pedir más cartas, tu puntaje se quedará en: ', ptos_player_total)
#
# #GENERACION DE LA TERCERA CARTA DEL CRUPIER y PUNTUACION OBTENIDA
#
# card_crupier_r3 = 0
# crupier_sum_r3 = 0
# ptos_crupier_total = 0
#
# if ptos_crupier_r1_r2 < 17:
#   random_num_fig_crupier = random.choice(cartas)
#   random_pale_crupier = random.choice(palos)
#   con_card_r3 += 1
#
#   if random_num_fig_crupier == 'J' or random_num_fig_crupier == 'Q' or random_num_fig_crupier == 'K':
#       crupier_sum_r3 += 10
#       ptos_crupier_total = ptos_crupier_r1_r2 + crupier_sum_r3
#       con_fig_r3 += 1
#       print('La carta del Crupier fue: ', random_num_fig_crupier, random_pale_crupier, 'Obtiene +', crupier_sum_r3, 'puntos')
#
#   elif random_num_fig_crupier == 'AS':
#       con_as_r3 += 1
#
#       if (ptos_crupier_r1_r2 + 11) < 21:
#           crupier_sum_r3 += 11
#           ptos_crupier_total = ptos_crupier_r1_r2 + crupier_sum_r3
#           print('La carta del Crupier fue: ', random_num_fig_crupier, random_pale_crupier, 'Obtiene +', crupier_sum_r3, 'puntos')
#       else:
#           crupier_sum_r3 += 1
#           ptos_crupier_total = ptos_crupier_r1_r2 + crupier_sum_r3
#           print('La carta del Crupier fue: ', random_num_fig_crupier, random_pale_crupier, 'Obtiene +', crupier_sum_r3, 'puntos')
#
#   else:
#       crupier_sum_r3 += random_num_fig_crupier
#       ptos_crupier_total = ptos_crupier_r1_r2 + crupier_sum_r3
#       print('La carta del Crupier fue: ', random_num_fig_crupier, random_pale_crupier, 'Obtiene +', crupier_sum_r3, 'puntos')
#
# else:
#   ptos_crupier_total = ptos_crupier_r1_r2
#   crupier_sum_r3 = print('El Crupier ya no puede pedir más cartas.')
#
#
# #COMPARAR EL PALO DE LAS CARTAS EN LA TERCERA RONDA
#
# if con_fig_r3 == 2:
#   if random_num_fig_player == random_num_fig_crupier:
#       if random_pale_player == random_pale_crupier:
#           print('ALUCINANTE! Has obtenido la misma figura con el mismo palo que el Crupier')
#       else:
#           print('Has obtenido la misma figura que el Crupier pero con distinto palo')
#   else:
#       print('Ambos han obtenido una figura, pero no hay coincidencias de palos')
# else:
#   if con_as_r3 == 2:
#       if random_pale_player == random_pale_crupier:
#           print('INSANO! Obtuviste un AS con el mismo palo que el crupier. De locos')
#       else:
#           print('Ambos han obtenido un AS pero con distinto palo')
#   else:
#       if con_card_r3 == 2:
#           if random_num_fig_player == random_num_fig_crupier:
#               if random_pale_player == random_pale_crupier:
#                   print('INCREIBLE! Has obtenido el mismo número con el mismo palo que el Crupier')
#               else:
#                   print('Has obtenido el mismo número que el Crupier pero con distino palo')
#           else:
#               if random_pale_player == random_pale_crupier:
#                   print('Hubo coincidencias de palo')
#               else:
#                   print('No hubo coincidencia de palo')
#
#
# # RESULTADOS DE PUNTUACION TOTAL
#
# # DETERMINACION DEL GANADOR - PERDEDOR - EMPATE
#
# print('\n', simb_replicado, '\n')
# input('Presione Enter para ver el resultado final\n')
# print(name_player, 'tu puntaje final fue de: ',ptos_player_total)
# print('El puntaje final del Crupier fue de: ', ptos_crupier_total, '\n')
#
# if ptos_crupier_total <= 21 and ptos_player_total <= 21:
#
#   if  ptos_player_total == ptos_crupier_total:
#       print('¡Enhorabuena! Haz empatado contra el crupier')
#
#   else:
#       if ptos_player_total > ptos_crupier_total:
#           print('Felicidades! Haz sido el ganador!')
#       else:
#           print('Lo siento, quizás la próxima tengas más suerte. El Crupier gana!')
#
# else:
#   if ptos_player_total > 21 and ptos_crupier_total > 21:
#       print('Ambos han sacado más de 21 puntos. Todos pierden!')
#
#   else:
#       if ptos_player_total > 21:
#           print('Has perdido! Tu puntuación final superó los 21 puntos. El ganador es el Crupier con', ptos_crupier_total, 'puntos.')
#       else:
#           print('Felicidades! Haz sido el ganador de esta mano.')
#
# # ESTADÍSTICAS
#
# fig_total = con_fig_r1 + con_fig_r2 + con_fig_r3
# print('\nCartas con figuras totales durante la partida: ', fig_total)
#
# FIN DEL PROGRAMA

#PROGRAMA TP2 QUE ANDA MASO
# import random


# #funcion de generacion de carta random
# def carta_random():
#     valores = (11,2,3,4,5,6,7,8,9,10,10,10,10)
#     nombres = (" -AS"," -2"," -3"," -4"," -5"," -6"," -7"," -8"," -9"," -10"," -J"," -Q"," -K")
#     palos = (" de picas"," de corazones"," de diamantes"," de treboles")
#     indice = random.randint(0,12)
#     palo = str(random.choice(palos))
#     return nombres[indice],palo,valores[indice]


# def control_as(puntaje,carta):
#     valor = carta
#     if puntaje >= 11 and carta == 11:
#         valor = 1
#     return valor


# def control_resultado(nombre,punt_jugador,apuesta,punt_crupier):
#     dinero = 0
#     ganador = None
#     if punt_jugador <= 21:
#         if punt_crupier > 21:
#             mensaje =("El crupier se paso de 21 y ", nombre, "gana con ", punt_jugador, "puntos")
#             dinero = apuesta + apuesta
#             ganador = 1
#         elif punt_jugador > punt_crupier:
#             mensaje = (nombre, "gana con ", punt_jugador, "puntos")
#             dinero = apuesta + apuesta
#             ganador = 1
#         elif punt_jugador == punt_crupier:
#             mensaje = (nombre, "y el crupier empatan con ", punt_crupier, "puntos")
#             dinero = apuesta
#             ganador = 0
#         else:
#             mensaje = ("El crupier gano con ", punt_crupier, "puntos")
#             dinero -= apuesta
#             ganador = 2
#     elif punt_crupier > 21:
#         mensaje = (nombre,"y el crupier se pasaron de 21, así que el crupier gana")
#         dinero -= apuesta
#         ganador = 0
#     else:
#         mensaje = (nombre,"se paso de 21 y el crupier gano con ", punt_crupier, "puntos")
#         dinero -= apuesta
#         ganador = 2
#     return mensaje,dinero,ganador


# def control_natural(nombre,jugador,crupier):
#     ganador = 0
#     winer = False
#     mensaje = "todavia no hay ganador"
#     if jugador == 21:
#         ganador = jugador
#         mensaje = nombre," gano la partida por black ajck natural"
#         winer = True
#     if crupier == 21:
#         ganador = crupier
#         mensaje = "el crupier gano la partida por black jack natural"
#         winer = True
#     if jugador == 21 and crupier == 21:
#         ganador = 0
#         mensaje = "todavia no hay ganador"
#         winer = False
#     return winer,mensaje,ganador


# # MENU DE OPCIONES
# #inicializaciones del menu
# saldo = None
# bet = None
# winner = False
# opcion = None
# name = str(input("ingresar el nombre del jugador --> "))
# victory_player = 0
# victory_crupier = 0
# racha_jugador = 0
# racha_crupier = 0
# apuesta_max = 0
# cant_blackjack_nat = 0
# suma_saldo = 0
# act_saldo = 0
# perdida_max = 0
# #inicializaciones
# cartas_jugador = None
# cartas_crupier = None
# puntaje_jugador = 0
# puntaje_crupier = 0

# #ingreso de saldo
# print("INGRESO DEL SALDO")
# ingreso_saldo = int(input("ingrese la cantidad de dinero que desea tener en su pozo \nel monto no debe ser menor a 0 ni mayor a 100000$ -->"))
# while ingreso_saldo > 100000 or ingreso_saldo <= 0:
#     print("no se puede ingresar una cantidad superior a 100000$ ni menor o igual a 0")
#     ingreso_saldo = int(input("ingrese la cantidad de dinero deseada -->"))
# saldo = ingreso_saldo


# #ciclo que controla el menu
# while opcion != 3:
#     print("MENU")
#     print(18*"-")
#     print("1 - Apostar")
#     print("2 - Jugar una mano")
#     print("3 - Salir")
#     opcion = int(input("elija la opcion deseada --> "))
#     print()
#     print()

#     #OPCION DE APUESTA
#     if opcion == 1:
#         print("ingreso de un monto para su pozo")
#         ingreso_saldo = int(input("ingrese la cantidad de dinero que desea tener en su pozo \n el monto no debe ser menor a 0 ni mayor a 100000$"))
#         while ingreso_saldo > 100000 or ingreso_saldo <= 0 or ingreso_saldo%5 != 0:
#             print("no se puede ingresar una cantidad superior a 100000$")
#             ingreso_saldo = int(input("ingrese la cantidad de dinero deseada -->"))
#         saldo += ingreso_saldo

#     #OPCION DE JUEGO

#     elif opcion == 2:
#         bet = int(input("ingresar un apuesta inferior o igual al saldo disponible --> "))
#         while bet > saldo or bet < 0 or bet%5 != 0:

#             if bet % 5 != 0:
#                 print("La apuesta debe ser múltiplo de 5. Ingrese otra vez: ")
#             elif bet > saldo:
#                 print("no cuentas con suficiente dinero para realizar esta apuesta")
#             elif bet < 0:
#                 print("La apuesta debe ser mayor que 0. Ingrese otra vez: ")
#             bet = int(input("ingresar un apuesta inferior o igual al saldo disponible --> "))
#         if bet == None:
#             print("debes apostar antes de jugar")
#         else:
#             #primera ronda
#             carta1_jugador = carta_random()
#             carta2_jugador = carta_random()

#             #VARIABLES PARA EL ACUMULADOR DE CARTAS
#             carta1_J = carta1_jugador[0] + carta1_jugador[1]
#             carta2_J = carta2_jugador[0] + carta2_jugador[1]

#             #validacion si la carta es un as
#             valor_jugador = control_as(carta1_jugador[2],carta2_jugador[2])

#             carta1_crupier = carta_random()
#             carta2_crupier = carta_random()

#             #VARIABLES PARA EL ACUMULADOR DE CARTAS
#             carta1_C = carta1_crupier[0] + carta1_crupier[1]
#             carta2_C = carta2_crupier[0] + carta2_crupier[1]

#             valor_crupier = control_as(carta1_crupier[2],carta2_crupier[2])

#             print("las primeras dos cartas de ", name, " son: \n--> ", carta1_jugador[0] + carta1_jugador[1], "\n--> ", carta2_jugador[0] + carta2_jugador[1])
#             print("\nla carta del crupier es: \n--> ",carta1_crupier[0]+carta1_crupier[1])

#             cartas_jugador = carta1_J + carta2_J

#             cartas_crupier = carta1_C + carta2_C

#             puntaje_jugador = carta1_jugador[2] + valor_jugador
#             puntaje_crupier = carta1_crupier[2] + valor_crupier

#             print("el puntaje actual de ", name, " es --> ", puntaje_jugador)
#             print("el puntaje actual del crupier es--> ",puntaje_crupier)

#             #control black jack natural
#             control = control_natural(name, puntaje_jugador, puntaje_crupier)
#             winner = control[0]
#             if winner == True:
#                 resultado = control_resultado(name, puntaje_jugador, bet, puntaje_crupier)
#                 print(control[1])
#                 print("el saldo de ", name, " antes de esta mano era de:", saldo)
#                 print("la apuesta de ", name, " fue de:", bet)
#                 print("el saldo actual de ", name, " es de:", (saldo + resultado[1]))
#                 print("las cartas de ", name, " fueron:", cartas_jugador)
#                 print("las cartas del crupier fueron:",cartas_crupier)

#                 #PROCESOS
#                 if control[2] == puntaje_jugador:
#                     victory_player += 1
#                 else:
#                     victory_crupier += 1
#                 cant_blackjack_nat += 1
#                 suma_saldo += resultado[1]
#                 act_saldo += 1
#                 if bet > apuesta_max:
#                     apuesta_max = bet
#                 puntaje_crupier = 0
#                 puntaje_jugador = 0

#             else:
#                 #rondas siguientes
#                 desicion = 1
#                 while puntaje_jugador <= 21 or puntaje_crupier <= 17:
#                     if desicion != 1 or puntaje_jugador >21:
#                         if desicion !=1:
#                             print(name, " se planto")
#                         elif puntaje_jugador > 21:
#                             print(name," se paso")
#                     elif puntaje_jugador <= 21:
#                         #MENU PARA EL JUGADOR
#                         print()
#                         print("SEGUIR JUEGO")
#                         print("si desea sacar otra carta ingrese - 1\nsi desea plantarse ingrese - 0")
#                         print()
#                         desicion = int(input("ingrese la opcion deseada --> "))

#                         #CARTAS SIGUIENTES DEL JUGADOR
#                         carta_jugador = carta_random()
#                         #VARIABLE ACUMULADOR
#                         cartaJ = carta_jugador[0] + carta_jugador[1]
#                         valor_jugador = control_as(puntaje_jugador,carta_jugador[2])
#                         puntaje_jugador += valor_jugador
#                         print(name, " saco la carta--> ", carta_jugador[0] + carta_jugador[1], "\nel puntaje actual de ", name, " es--> ", puntaje_jugador)
#                         cartas_jugador += cartaJ
#                     if puntaje_crupier <= 17:
#                         #GENERACION DE CARTA DEL CRUPIER
#                         carta_crupier = carta_random()
#                         #VARIABLE PARA ACUMULAR
#                         cartaC = carta_crupier[0] + carta_crupier[1]
#                         valor_crupier = control_as(puntaje_crupier,carta_crupier[2])
#                         puntaje_crupier += valor_crupier
#                         cartas_crupier += cartaC
#                     elif puntaje_crupier >= 17 and puntaje_crupier <= 21:
#                         print("el crupier se planto")
#                     else:
#                         print("el crupier se paso")
#                 else:
#                     print()
#                     input("precione enter para ver los resultados...")
#                     print()
#                     resultado = control_resultado(name, puntaje_jugador, bet, puntaje_crupier)
#                     print(resultado[0])
#                     print("el saldo de ", name, " antes de esta mano era de:", saldo)
#                     print("la apuesta de ", name, " fue de:", bet)
#                     print("el saldo actual de ", name, " es de:", (saldo + resultado[1]))
#                     print("las cartas de ", name, " fueron:", cartas_jugador)
#                     print("las cartas del crupier fueron:", cartas_crupier)

#                     #PROCESOS
#                     if resultado[2] == 1:
#                         victory_player += 1
#                     elif resultado[2] == 2:
#                         victory_crupier += 1
#                     suma_saldo += resultado[1]
#                     act_saldo += 1
#                     if bet > apuesta_max:
#                         apuesta_max = bet
#                     puntaje_crupier = 0
#                     puntaje_jugador = 0

#     #OPCION DE SALIR
#     elif opcion == 3:
#         print("chau")
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

    # PEDIDO DE NOMBRE Y CANTIDAD DE DINERO
    player_name = str(input('Ingrese su nombre --> '))
    print('Bienvenido', player_name, '!, ahora ingrese su monto')
    amount_money_box = int(input("ingrese la cantidad de dinero que desea tener en su pozo \nel monto no debe ser menor a 0 ni mayor a 100000$ -->"))
    while amount_money_box > 100000 or amount_money_box <= 0:
        print("no se puede ingresar una cantidad superior a 100000$ ni menor o igual a 0")
        amount_money_box = int(input("ingrese la cantidad de dinero deseada --> "))
    acu_amount_money_box = amount_money_box
    if amount_money_box_max == None:
        amount_money_box_max = amount_money_box
    while option != 3:
        print("MENU")
        print(18*"-")
        print("1 - Apostar\n2 - Jugar una mano\n3 - Salir")
        option = int(input("elija la opcion deseada --> "))
        # hacer la despedida
        print('\n\n')

        #OPCION DE APUESTA
        if option == 1:
            amount_money_box_plus = 0
            while amount_money_box_plus <= 0 or amount_money_box_plus > 100000:
                print("no se puede ingresar una cantidad superior a 100000$ ni menor o igual a 0")
                amount_money_box_plus = int(input("ingrese la cantidad de dinero deseada --> "))
                if (amount_money_box_plus + amount_money_box) <= 100000:
                    amount_money_box += amount_money_box_plus
                    act_amount_money_box += 1
                    acu_amount_money_box += amount_money_box
                else:
                    print('El monto ingresado es menor o igual a 0 o... \nel total entre este monto y el primero supera la cantidad de 100000')
                    amount_money_box_plus = 0
        #OPCION DE JUGAR UNA MANO
        elif option == 2:
            if amount_money_box == 0 or amount_money_box < 5:
                print("\n No tiene sificiente dinero. Volviendo al menu principal\n")
                continue
            print("Su saldo disponible es :", amount_money_box)
            bet = int(input("ingresar un apuesta inferior o igual al saldo disponible --> "))
            while bet > amount_money_box or bet <= 0 or (bet % 5) != 0:
                if bet % 5 != 0:
                    print("La apuesta debe ser múltiplo de 5. Ingrese otra vez: ")
                elif bet > amount_money_box:
                    print("no cuentas con suficiente dinero para realizar esta apuesta")
                elif bet <= 0:
                    print("La apuesta debe ser mayor que 0. Ingrese otra vez: ")
                bet = int(input("ingresar un apuesta inferior o igual al saldo disponible --> "))
            if bet == None:
                print("debes apostar antes de jugar")
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

                print("las primeras dos cartas de ", player_name, " son: \n--> ", total_cards_player, "\nla carta del crupier es: \n--> ",total_cards_crupier)

                #CONTROL BLACK JACK NATURAL
                control = natural_control(player_score, crupier_score)
                winner = control[0]
                if winner == True:
                    cant_blackjack_nat += 1
                else:
                    #GENERACION DE CARTAS DEL JUGADOR
                    print()
                    print("SEGUIR JUEGO")
                    print("si desea sacar otra carta ingrese - 1\nsi desea plantarse ingrese - 0")
                    print()
                    desicion = int(input("ingrese la opcion deseada --> "))
                    while player_score < 21 and desicion == 1:
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
                            print("SEGUIR JUEGO")
                            print("si desea sacar otra carta ingrese - 1\nsi desea plantarse ingrese - 0")
                            print()
                            desicion = int(input("ingrese la opcion deseada --> "))
                    if desicion == 0:
                        print(player_name, " se planto")
                    if player_score > 21:
                        print(player_name," se paso")
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
                        print("el crupier se planto")
                    elif crupier_score > 21:
                        print("el crupier se paso")

                print("\n\n")
                result = check_result(player_name, player_score, bet, crupier_score,winner)

                print(result[0])
                print("\nel saldo de ", player_name, " antes de esta mano era de:", amount_money_box)
                print("la apuesta de ", player_name, " fue de:", bet)
                print("el saldo actual de ", player_name, " es de:", (amount_money_box + result[1]))
                print("las cartas de ", player_name, " fueron:", total_cards_player)
                print("las cartas del crupier fueron:",total_cards_crupier)

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

                if victory_crupier_flag == True:
                    racha_crupier = victory_crupier
                else:
                    victory_crupier = 0

                if result[2] == 1:
                    victory_player += 1

                cont_games += 1
                amount_money_box += result[1]
                #POZO
                if amount_money_box > amount_money_box_max:
                    amount_money_box_max = amount_money_box
                act_amount_money_box += 1
                acu_amount_money_box += amount_money_box

    if option == 3:
        if flag_finish_game == False:
            print("No se concreto ninguna partida")
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


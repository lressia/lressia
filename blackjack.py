#BLACKJACK 2.0

import random


def card_generator():
    value = (11,2,3,4,5,6,7,8,9,10,10,10,10)
    names = (" -AS"," -2"," -3"," -4"," -5"," -6"," -7"," -8"," -9"," -10"," -J"," -Q"," -K")
    pales = (" de picas"," de corazones"," de diamantes"," de treboles")
    index = random.randint(0,12)
    pale = str(random.choice(palos))
    return names[index],pale,value[index]


def control_natural(nombre,jugador,crupier):
    ganador = 0
    winer = False
    mensaje = "todavia no hay ganador"
    if jugador == 21:
        ganador = jugador
        mensaje = nombre," gano la partida por black ajck natural"
        winer = True
    if crupier == 21:
        ganador = crupier
        mensaje = "el crupier gano la partida por black jack natural"
        winer = True
    if jugador == 21 and crupier == 21:
        ganador = 0
        mensaje = "todavia no hay ganador"
        winer = False
    return winer,mensaje,ganador



def main_game():
    option = None
    amount_money_box = 0
    amount_money_box_plus = 0
    winer = False
    bet = None
    card_player_count = 0
    card_player_value = 0
    victory_player = 0
    victory_crupier = 0
    cant_blackjack_nat = 0



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
            while amount_money_box_plus <= 0:
                print("no se puede ingresar una cantidad superior a 100000$ ni menor o igual a 0")
                amount_money_box_plus = int(input("ingrese la cantidad de dinero deseada --> "))
                if (amount_money_box_plus % 5) == 0 and (amount_money_box_plus + amount_money_box) <= 100000:
                    amount_money_box += amount_money_box_plus
                else:
                    print('El monto ingresado no es multiplo de 5 o el total entre este monto y el primero supera la cantidad de cien mil pesos')

        #OPCION DE JUGAR UNA MANO
        elif option == 2:

            bet = int(input("ingresar un apuesta inferior o igual al saldo disponible --> "))
            while bet > amount_money_box or bet < 0 or bet%5 != 0:

                if bet % 5 != 0:
                    print("La apuesta debe ser múltiplo de 5. Ingrese otra vez: ")
                elif bet > saldo:
                    print("no cuentas con suficiente dinero para realizar esta apuesta")
                elif bet < 0:
                    print("La apuesta debe ser mayor que 0. Ingrese otra vez: ")
                bet = int(input("ingresar un apuesta inferior o igual al saldo disponible --> "))
            if bet == None:
                print("debes apostar antes de jugar")
            else:
                #return name,palo,value
                #GENERACION DE CARTAS DEL CRUPIER
                card1_crupier = card_generator()

                crupier_score = card1_crupier[2]

                card1 = card1_crupier[0] + card1_crupier[1]

                cards_crupier = card1

                #GENERACION DE CARTAS DEL JUGADOR
                card_player_1 = card_generator()
                card_player_2 = card_generator()

                player_score = card_player_1[2] + card_player_2[2]

                card1 = card_player_1[0] + card_player_1[1]
                card2 = card_player_2[0] + card_player_2[1]

                cards_player = card1 + card2

                print("las primeras dos cartas de ", player_name, " son: \n--> ", card_player_1[0] + card_player_1[1], "\n--> ", card_player_2[0] + card_player_2[1])
                print("\nla carta del crupier es: \n--> ",carta1_crupier[0]+carta1_crupier[1])

                #control black jack natural
                control = control_natural(player_name, player_score, crupier_score)
                winner = control[0]
                if winner == True:
                    result = control_resultado(player_name, player_score, bet, crupier_score)
                    print(control[1])
                    print("el saldo de ", player_name, " antes de esta mano era de:", amount_money_box)
                    print("la apuesta de ", player_name, " fue de:", bet)
                    print("el saldo actual de ", player_name, " es de:", (amount_money_box + result[1]))
                    print("las cartas de ", player_name, " fueron:", cards_player)
                    print("las cartas del crupier fueron:",cards_crupier)

                    #PROCESOS
                    if control[2] == player_score:
                        victory_player += 1
                    else:
                        victory_crupier += 1
                    cant_blackjack_nat += 1
                    suma_saldo += resultado[1]
                    act_saldo += 1
                    if bet > apuesta_max:
                        apuesta_max = bet
                    puntaje_crupier = 0
                    puntaje_jugador = 0
                
                while player_score < 21:
                    

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

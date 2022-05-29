import random


#funcion de generacion de carta random
def carta_random():
    valores = (11,2,3,4,5,6,7,8,9,10,10,10,10)
    nombres = ("AS","2","3","4","5","6","7","8","9","10","J","Q","K")
    palos = (" de picas"," de corazones"," de diamantes"," de treboles")
    indice = random.randint(0,12)
    palo = str(random.choice(palos))
    return nombres[indice],palo,valores[indice]


def control_as(puntaje,carta):
    valor = carta
    if puntaje >= 11 and carta == 11:
        valor = 1
    return valor


def control_resultado(nombre,punt_jugador,apuesta,punt_crupier):
    dinero = 0
    ganador = None
    if punt_jugador <= 21:
        if punt_crupier > 21:
            mensaje =("El crupier se paso de 21 y ", nombre, "gana con ", punt_jugador, "puntos")
            dinero = apuesta + apuesta
            ganador = 1
        elif punt_jugador > punt_crupier:
            mensaje = (nombre, "gana con ", punt_jugador, "puntos")
            dinero = apuesta + apuesta
            ganador = 1
        elif punt_jugador == punt_crupier:
            mensaje = (nombre, "y el crupier empatan con ", punt_crupier, "puntos")
            dinero = apuesta
            ganador = 0
        else:
            mensaje = ("El crupier gano con ", punt_crupier, "puntos")
            dinero -= apuesta
            ganador = 2
    elif punt_crupier > 21:
        mensaje = (nombre,"y el crupier se pasaron de 21, así que el crupier gana")
        dinero -= apuesta
        ganador = 0
    else:
        mensaje = (nombre,"se paso de 21 y el crupier gano con ", punt_crupier, "puntos")
        dinero -= apuesta
        ganador = 2
    return mensaje,dinero,ganador


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


# MENU DE OPCIONES
#inicializaciones del menu
saldo = None
bet = None
winner = False
opcion = None
name = str(input("ingresar el nombre del jugador --> "))
victory_player = 0
victory_crupier = 0
racha_jugador = 0
racha_crupier = 0
apuesta_max = 0
cant_blackjack_nat = 0
suma_saldo = 0
act_saldo = 0
perdida_max = 0
#inicializaciones
cartas_jugador = None
cartas_crupier = None
puntaje_jugador = 0
puntaje_crupier = 0

#ingreso de saldo
print("INGRESO DEL SALDO")
ingreso_saldo = int(input("ingrese la cantidad de dinero que desea tener en su pozo \nel monto no debe ser menor a 0 ni mayor a 100000$ -->"))
while ingreso_saldo > 100000 or ingreso_saldo <= 0:
    print("no se puede ingresar una cantidad superior a 100000$ ni menor o igual a 0")
    ingreso_saldo = int(input("ingrese la cantidad de dinero deseada -->"))
saldo = ingreso_saldo


#ciclo que controla el menu
while opcion != 3:
    print("MENU")
    print(18*"-")
    print("1 - Apostar")
    print("2 - Jugar una mano")
    print("3 - Salir")
    opcion = int(input("elija la opcion deseada --> "))
    print()
    print()

    #OPCION DE APUESTA
    if opcion == 1:
        print("ingreso de un monto para su pozo")
        ingreso_saldo = int(input("ingrese la cantidad de dinero que desea tener en su pozo \n el monto no debe ser menor a 0 ni mayor a 100000$"))
        while ingreso_saldo > 100000 or ingreso_saldo <= 0 or ingreso_saldo%5 != 0:
            print("no se puede ingresar una cantidad superior a 100000$")
            ingreso_saldo = int(input("ingrese la cantidad de dinero deseada -->"))
        saldo += ingreso_saldo

    #OPCION DE JUEGO

    elif opcion == 2:
        bet = int(input("ingresar un apuesta inferior o igual al saldo disponible --> "))
        while bet > saldo or bet < 0 or bet%5 != 0:

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
            #primera ronda
            carta1_jugador = carta_random()
            carta2_jugador = carta_random()

            #validacion si la carta es un as
            valor_jugador = control_as(carta1_jugador[2],carta2_jugador[2])

            carta1_crupier = carta_random()
            carta2_crupier = carta_random()

            valor_crupier = control_as(carta1_crupier[2],carta2_crupier[2])

            print("las primeras dos cartas de ", name, " son: \n--> ", carta1_jugador[0] + carta1_jugador[1], "\n--> ", carta2_jugador[0] + carta2_jugador[1])
            print("\nla carta del crupier es: \n--> ",carta1_crupier[0]+carta1_crupier[1])

            #cartas_jugador += (carta1_jugador[0]+carta1_jugador[1]) + (carta2_jugador[0]+carta2_jugador[1])

            #cartas_crupier += (carta1_crupier[0]+carta1_crupier[1]) + (carta2_crupier[0]+carta2_crupier[1])

            puntaje_jugador = carta1_jugador[2] + valor_jugador
            puntaje_crupier = carta1_crupier[2] + valor_crupier

            print("el puntaje actual de ", name, " es --> ", puntaje_jugador)
            print("el puntaje actual del crupier es--> ",puntaje_crupier)

            #control black jack natural
            control = control_natural(name, puntaje_jugador, puntaje_crupier)
            winner = control[0]
            if winner == True:
                resultado = control_resultado(name, puntaje_jugador, bet, puntaje_crupier)
                print(control[1])
                print("el saldo de ", name, " antes de esta mano era de:", saldo)
                print("la apuesta de ", name, " fue de:", bet)
                print("el saldo actual de ", name, " es de:", (saldo + resultado[1]))
                print("las cartas de ", name, " fueron:", cartas_jugador)
                print("las cartas del crupier fueron:",cartas_crupier)

                #PROCESOS
                if control[2] == puntaje_jugador:
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

            else:
                #rondas siguientes
                desicion = 1
                while puntaje_jugador <= 21 or puntaje_crupier <= 17:
                    if desicion != 1 or puntaje_jugador >21:
                        if desicion !=1:
                            print(name, " se planto")
                        elif puntaje_jugador > 21:
                            print(name," se paso")
                    elif puntaje_jugador <= 21:
                        print()
                        print("SEGUIR JUEGO")
                        print("si desea sacar otra carta ingrese - 1\nsi desea plantarse ingrese - 0")
                        print()
                        desicion = int(input("ingrese la opcion deseada --> "))
                        carta_jugador = carta_random()
                        valor_jugador = control_as(puntaje_jugador,carta_jugador[2])
                        puntaje_jugador += valor_jugador
                        print(name, " saco la carta--> ", carta_jugador[0] + carta_jugador[1], "\nel puntaje actual de ", name, " es--> ", puntaje_jugador)
                        #cartas_jugador += (carta_jugador[0]+carta_jugador[1])
                    if puntaje_crupier <= 17:
                        carta_crupier = carta_random()
                        valor_crupier = control_as(puntaje_crupier,carta_crupier[2])
                        puntaje_crupier += valor_crupier
                        #cartas_crupier += carta_crupier[0]+carta_crupier[1]
                    elif puntaje_crupier >= 17 and puntaje_crupier <= 21:
                        print("el crupier se planto")
                    else:
                        print("el crupier se paso")
                else:
                    print()
                    input("precione enter para ver los resultados...")
                    print()
                    resultado = control_resultado(name, puntaje_jugador, bet, puntaje_crupier)
                    print(resultado[0])
                    print("el saldo de ", name, " antes de esta mano era de:", saldo)
                    print("la apuesta de ", name, " fue de:", bet)
                    print("el saldo actual de ", name, " es de:", (saldo + resultado[1]))
                    print("las cartas de ", name, " fueron:", cartas_jugador)
                    print("las cartas del crupier fueron:", cartas_crupier)

                    #PROCESOS
                    if resultado[2] == 1:
                        victory_player += 1
                    elif resultado[2] == 2:
                        victory_crupier += 1
                    suma_saldo += resultado[1]
                    act_saldo += 1
                    if bet > apuesta_max:
                        apuesta_max = bet
                    puntaje_crupier = 0
                    puntaje_jugador = 0

    #OPCION DE SALIR
    elif opcion == 3:
        print("chau")

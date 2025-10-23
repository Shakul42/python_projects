import random


def startuj():
    choice = None
    gamecount = 0
    playerscore, pcscore = 0, 0
    print("VITAJTE v hre : Kameň, Papier, Nožnice, Jašter, Spock!!")
    print("Zvoľ si svoju zbraň: (1-Kameň, 2-Papier, 3-Nožnice, 4-Jašter, 5-Spock), ")
    while choice != "end":
        choice = input ("Napíš číslo 1-5, 'stav', 'help' pre vysvetlivky alebo 'end' pre koniec> ")
        if choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5':
            result = porovnaj (choice)
            # Pocitadlo hier a stavu
            gamecount += 1
            if result == 1:
                playerscore += 1
            elif result == 2:
                pcscore += 1
        elif choice == "help":
            print("1- Kameň, 2- Papier, 3- Nožnice, 4- Jašter, 5- Spock")
        elif choice == "stav":
            print("Aktuálny stav je -> Ty vs. PC: "+ str(playerscore)+ " vs. "+ str(pcscore)+ " Počet odohraných hier: "+ str(gamecount))
        else:
            print("Zvoľ si svoju zbraň (1-5): (1-Kameň, 2-Papier, 3-Nožnice, 4-Jašter, 5-Spock), ")
    else:
        print("Vďaka za hru.")


def porovnaj(choice):
    npc = random.randint(1,5)
    choice = int(choice)
    result = 0
    if choice == 1:   # KAMEN
        print("KAMEN:")
        if npc == 1:
            print("Je to ZHODA! Kameň Kameň.")
        elif npc == 2:
            print("Prehral si! Papier zabalí Kameň.")
            result = 2
        elif npc == 3:
            print("Vyhral si! Kameň otupí Nožnice.")
            result = 1
        elif npc == 4:
            print("Vyhral si! Kameň rozdrví Jaštera.")
            result = 1
        elif npc == 5:
            print("Prehral si! Spock vyparí Kameň.")
            result = 2

    elif choice == 2:   # PAPIER
        print("PAPIER:")
        if npc == 1:
            print("Vyhral si! Papier zabalí Kameň.")
            result = 1
        elif npc == 2:
            print("Je to ZHODA! Papier Papier.")
        elif npc == 3:
            print("Prehral si! Nožnice rozstrihnú Papier.")
            result = 2
        elif npc == 4:
            print("Prehral si! Jašter zje Papier.")
            result = 2
        elif npc == 5:
            print("Vyhral si! Papier usvedčí Spocka.")
            result = 1

    elif choice == 3:   # NOZNICE
        print("NOZNICE:")
        if npc == 1:
            print("Prehral si! Kameň otupí Nožnice.")
            result = 2
        elif npc == 2:
            print("Vyhral si! Nožnice prestrihnú Papier.")
            result = 1
        elif npc == 3:
            print("Je to ZHODA! Nožnice Nožnice.")
        elif npc == 4:
            print("Vyhral si! Nožnice prestrihnú Jaštera.")
            result = 1
        elif npc == 5:
            print("Prehral si! Spock poláme Nožnice.")
            result = 2

    elif choice == 4:   # JASTER
        print("JASTER:")
        if npc == 1:
            print("Prehral si! Jaštera rozdrví Kameň.")
            result = 2
        elif npc == 2:
            print("Vyhral si! Jašter zje Papier.")
            result = 1
        elif npc == 3:
            print("Prehral si! Nožnice rozstrihnú Papier.")
            result = 2
        elif npc == 4:
            print("Je to ZHODA! Jašter Jašter.")
        elif npc == 5:
            print("Vyhral si! Jašter otrávi Spocka.")
            result = 1

    elif choice == 5:   # SPOCK
        print("SPOCK:")
        if npc == 1:
            print("Vyhral si! Spock vyparí Kameň.")
            result = 1
        elif npc == 2:
            print("Prehral si! Papier usvedčí Spocka.")
            result = 2
        elif npc == 3:
            print("Vyhral si! Spock poláme Nožnice..")
            result = 1
        elif npc == 4:
            print("Prehral si! Jašter otrávi Spocka.")
            result = 2
        elif npc == 5:
            print("Je to ZHODA! Spock Spock.")
    return result
    

if __name__ == '__main__':
    startuj()
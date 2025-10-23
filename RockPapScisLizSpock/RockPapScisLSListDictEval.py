import random


def startuj():
    choice = None
    gamecount = 0
    playerscore, pcscore = 0, 0
    wpn = ["Kameň", "Papier", "Nožnice", "Jašter", "Spock"] # List
    print("VITAJTE v hre : "+ wpn[0] +", "+ wpn[1] +", "+ wpn[2] +", "+ wpn[3] +", "+ wpn[4]+"!")
    print("Zvoľ si svoju zbraň: (1-"+ wpn[0] +", 2-"+ wpn[1] +", 3-"+ wpn[2] +", 4-"+ wpn[3] +", 5-"+ wpn[4] +"). ")
    while choice != "end":
        choice = input ("Napíš číslo 1-5, 'stav', 'help' pre vysvetlivky alebo 'end' pre koniec> ")
        if choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5':
            result = porovnaj (choice, wpn)
            # Pocitadlo hier a stavu
            gamecount += 1
            if result == 1:
                playerscore += 1
            elif result == 2:
                pcscore += 1
        elif choice == "help":
            print("1-"+ wpn[0] +", 2-"+ wpn[1] +", 3-"+ wpn[2] +", 4-"+ wpn[3] +", 5-"+ wpn[4])
        elif choice == "stav":
            print("Aktuálny stav je -> Ty vs. PC: "+ str(playerscore)+ " vs. "+ str(pcscore)+ " Počet odohraných hier: "+ str(gamecount))
        else:
            print("Zvoľ si svoju zbraň (1-5): (1-"+ wpn[0] +", 2-"+ wpn[1] +", 3-"+ wpn[2] +", 4-"+ wpn[3] +", 5-"+ wpn[4] +")")
    else:
        print("Vďaka za hru.")


def porovnaj(choice, wpn):
    npc = random.randint(1,5)
    choice = int(choice)
    result = 0
    # KAMEN 1: lose 2,5 won 3,4 # PAPIER 2: lose 3,4 won 1,5 # NOZNICE 3: lose 1,5 won 2,4
    # JASTER 4: lose 1,3 won 2,5 # SPOCK 5: lose 2,4 won 1,3
    lose = {1: "npc == 2 or npc == 5", 2: "npc == 3 or npc == 4", 3: "npc == 1 or npc == 5", 4: "npc == 1 or npc == 3", 5: "npc == 2 or npc == 4"}
    won =  {1: "npc == 3 or npc == 4", 2: "npc == 1 or npc == 5", 3: "npc == 2 or npc == 4", 4: "npc == 2 or npc == 5", 5: "npc == 1 or npc == 3"}  # Dictionary key:value pair, ordered+indexed from Python 3.7
    print(wpn[choice-1] +":")
    if choice == npc:   # ZHODA
        print("Je to ZHODA! "+ wpn[choice-1] +" vs. "+ wpn[npc-1]+".")
    elif eval(won[choice]):    # VYHRA
        print("Je to VÝHRA! "+ wpn[choice-1] +" vs. "+ wpn[npc-1]+".")
        result = 1
    elif eval(lose[choice]): # PREHRA
        print("Je to PREHRA! "+ wpn[choice-1] +" vs. "+ wpn[npc-1]+".")
        result = 2
    return result

if __name__ == '__main__':
    startuj()

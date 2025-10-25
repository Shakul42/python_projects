from math import sqrt   #ak je import takto, tak funkcia sa dalej vola bez "math."sqrt


def startuj():
    line = None
    print("OVEROVAČ PRVOČÍSELNOSTI:")
    while line != "end":
        line = input("Napíš celé kladné číslo alebo 'end' pre koniec> ")
        if line != "end":
            try:
                calcPrime(line)
            except Exception as e:
                #print(e)
                print("Vstup musí byť celé kladné číslo alebo 'end' pre koniec!!")
                continue
        else:
            print("Ďakujeme za použitie overovača prvočíselnosti.")


# ciferný súčet pre overenie deliteľnosti 3
def sum_digits3(overCislo, pocetCislic):
    r = 0
    for i in range(pocetCislic):
        # zvyšok po delení 10, teda číslica na mieste jednotiek, sa pripočítava a potom delí 10 bez zvyšku
        r, overCislo = r + overCislo % 10, overCislo // 10  
    return r    


def calcPrime(line):
    pocetCislic = len(line)
    overCislo = int(line)
    m = sqrt(overCislo) #stačí overiť deliteľov nižších ako druhá odmocnina
    stN = int(line[-1])  # posledná číslica

    # Overovanie prvočíselnosti
    if stN == 5 and overCislo != 5:
        print("Číslo je deliteľné 5.")
    elif stN == 0 or stN == 4 or stN == 6 or stN == 8 or stN == 2 and overCislo != 2: #2 je prvočíslo, zahrnutá 0
        print("Číslo nieje prvočíslo, lebo je párne.")
    elif overCislo == 3:
        print("Číslo je prvočíslo 3.")
    elif sum_digits3(overCislo, pocetCislic) % 3 == 0:  # ciferný súčet je deliteľný 3
        print("Číslo nieje prvočíslo. Je deliteľné 3")
    else:
        n, y, tri = 0, 0, 3
        while n < m:
            y += 1  # počet loopov (pre nepárne čísla)
            x = 1+2*y #nepárne čísla
            n = x + 2   #next odd nr, pre porovnanie s odmocninou, lebo +2 je
                        #rýchlejšie než zbytočné delenie delenie(last loop s x, bez n) 
            five = str(x)
            if x == tri: #SKIP delenia nepárnymi násobkami 3
                tri = tri + 6 #každé (1+2x)*3 je nepárne a deliteľné 3
                continue
            elif int(five[-1]) == 5: #SKIP posledná číslica je 5
                continue
            elif overCislo % x == 0:  #deliteľnosť zvyšnými nepárnymi číslami
                print("Číslo nieje prvočíslo. Je deliteľné " + str(x))         
                break
        else:
            print("Číslo " + line + " je prvočíslo.")


if __name__ == '__main__':
    startuj()
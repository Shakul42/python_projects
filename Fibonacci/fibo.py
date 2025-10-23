#Volané potom v main
def fibostep(n):
    sn = fibo[n] + fibo[n - 1]
    fibo.append(sn)

fibo = [0,1]

def startuj():
    print("Koľko čísel Fibonaciho postupnosti si želáte vypísať?(kladné celé číslo >2)")
    line = input(">")
    for i in range(1, int(line)-1): #znížené o 2, lebo list už prvé 2 prvky má
        fibostep(i)
    print(fibo)


if __name__ == '__main__':
    startuj()
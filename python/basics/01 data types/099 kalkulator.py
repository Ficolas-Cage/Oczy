end = False
while end == False:
    Liczba = int(input('Podaj 1 liczbe: '))
    Liczba2 = int(input('Podaj 2 liczbe: '))
    print('Co chcesz zrobić z tymi liczbami ? 1 - dodawanie, 2 odejmowanie, 3 dzielenie, 4 mnozenie, 5 potęgowanie ')
    operacja = 0

    while operacja > 5 or operacja < 1:
        operacja = int(input())
        if operacja < 6 and operacja > 0:
            match operacja:
                case 1:
                    Wynik = Liczba + Liczba2
                case 2:
                    Wynik = Liczba - Liczba2
                case 3:
                    Wynik = Liczba / Liczba2
                case 4:
                    Wynik = Liczba * Liczba2
                case 5:
                    Wynik = Liczba ** Liczba2 


    
    for v in range(10):
        import time
        time.sleep(0.1)
        print(str(v * 10) + '%')
        import time
        time.sleep(0.1)
        import os
        clear = lambda: os.system('cls')
        clear()
        
    
    print('Wynik: ' + str(Wynik))
     
    Wynik2 =+ Wynik
    if Wynik >= 0:
            wynik2 = Wynik + Liczba2
    while operacja > 5 or operacja < 1:
        operacja = int(input())
        if operacja < 6 and operacja > 0:
            match operacja:
                case 1:
                    wynik2 = Wynik + Liczba2
                case 2:
                    Wynik2 = Wynik - Liczba2
                case 3:
                    Wynik2 = Wynik / Liczba2
                case 4:
                    Wynik2 = Wynik * Liczba2
                case 5:
                    Wynik2 = Wynik ** Liczba2
    print(' ')
    endStr = 'S'
    while endStr != 'T' and endStr != 'N' or Wynik2 != 'J':
        endStr = input('Liczymy jeszcze raz ? T - Tak , N - Nie ')
        if endStr == 'T' or endStr == 'N':
            if endStr == 'T':
                end = False
            else:
                end = True
        else:
            print('Zly znak wybierz go jeszcze raz')
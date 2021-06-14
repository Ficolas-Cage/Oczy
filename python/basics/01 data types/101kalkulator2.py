# data = PobranieZExcela()

from os import error

end = False
Wynik2 = 0
while end == False:
    if Wynik2 == 0:
        Liczba = int(input('Podaj 1 liczbe: '))
    else:
        Liczba = Wynik2

    Liczba2 = int(input('Podaj 2 liczbe: '))
    print('Co chcesz zrobić z tymi liczbami ? 1 - dodawanie, 2 odejmowanie, 3 dzielenie, 4 mnozenie, 5 potęgowanie: ')
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
   

        print('Zla operacja wybierz ja jeszcze raz')
        print('Co chcesz zrobić z tymi liczbami ? 1 - dodawanie, 2 odejmowanie, 3 dzielenie, 4 mnozenie, 5 potęgowanie ')

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
    print(' ')
    endStr = 'sstetadzsawrfac'
    wynikStr = 'sstetadzsawrfac'
    while endStr != 'T' and endStr != 'N':
        endStr = input('Liczymy jeszcze raz ? T - Tak , N - Nie: ')
        if endStr == 'T' or endStr == 'N':
            if endStr == 'T':
                end = False
                while wynikStr != 'T' and wynikStr != 'N':
                    wynikStr = input('Zachować wynik ? T - Tak , N - Nie: ')
                    if wynikStr == 'T' or wynikStr == 'N':
                        if wynikStr == 'T':
                            Wynik2 = Wynik
                        else:
                            Wynik2 = 0
                    else:
                        print('Zly znak wybierz go jeszcze raz')           
            else:
                end = True
        else:
            print('Zly znak wybierz go jeszcze raz')
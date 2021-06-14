
# wczytaj plik, wyświetl dane, usuń dane, modyfikuj dane

import os
end = False
while end == False:
    clear = lambda: os.system('cls')
    clear()
    print('1.wczytaj plik')
    print('2.wyświetl dane')
    print('3.usuń dane')
    print('4.modyfikuj dane')

    operacja = 0
    while operacja > 4 or operacja < 1:
        operacja = int(input())
        if operacja < 5 and operacja > 0:
            match operacja:
                case 1:
                    for v in range(10):
                        import time
                        time.sleep(0.1)
                        print(str(v * 10) + '%')
                        import time
                        time.sleep(0.1)
                        import os
                        clear = lambda: os.system('cls')
                        clear()
                                
                case 2:
                    print('wyświetlanie danych')
                case 3:
                    print('usuwanie dancyh')
                case 4:
                    print('modyfikowanie danych')
        else:
            clear()
            print('Zla operacja wybierz ja jeszcze raz')
            print('1.wczytaj plik')
            print('2.wyświetl dane')
            print('3.usuń dane')
            print('4.modyfikuj dane')

        endStr = 'sstetadzsawrfac'
        wynikStr = 'sstetadzsawrfac'
        while endStr != 'T' and endStr != 'N':
            endStr = input(' T - Powrót do Menu , N - Wyjście: ')
            if endStr == 'T' or endStr == 'N':
                if endStr == 'T':
                    end = False          
                else:
                    end = True
            else:
                print('Zly znak wybierz go jeszcze raz')
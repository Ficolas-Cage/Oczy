
import os
end = False

# D:\pPULPIT\PYTHON\DANE.txt

# Podglad jednego wiersza. Czyli podaje numer wiersza i wyświetla mi się tylko to. Dodać jako opcje 3 Wyświetl konkretne dane.

# Usuwanie pliku.

# Modifikowanie danych i zapisanie do pliku.


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
                    print('Wczytywanie danych')
                    for v in range(10):
                        import time
                        time.sleep(0.05)
                        print(str(v * 10) + '%')
                        import time
                        time.sleep(0.05)
                        import os
                        clear = lambda: os.system('cls')
                        clear()
                    with open(input('Podaj sciezke pliku: ')) as f:
                        lines = f.readlines()               
                case 2:
                    print('wyświetlanie danych:')
                    for a in lines:
                        print(a)
                case 3:
                    print('usuwanie dancyh')
                    import os
                    open(input(os.remove("D:\pPULPIT\PYTHON\DANE.txt")))
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
        while endStr != 't' and endStr != 'n':
            endStr = input(' t - Powrót do Menu , n - Wyjście: ')
            if endStr == 't' or endStr == 'n':
                if endStr == 't':
                    end = False
                else:
                    end = True
            else:
                print('Zly znak wybierz go jeszcze raz')
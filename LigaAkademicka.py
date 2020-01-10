PIERWSZY_KROK_SLOWNIK = {'A': ['G'],            # Deklaracja slownika z wszystkimi mozliwymi kombinacjami
                         'B': ['G', 'J', 'L'],  # dla pierwszego kroku.
                         'C': ['K', 'M', 'H', 'E'],
                         'D': ['L'],
                         'E': ['C', 'L', 'P'],
                         'F': ['Q', 'J', 'P'],
                         'G': ['B', 'K', 'N', 'R', 'A'],
                         'H': ['Q', 'C', 'L'],
                         'I': ['P'],
                         'J': ['F', 'S', 'B'],
                         'K': ['G', 'C', 'T', 'Q'],
                         'L': ['B', 'S', 'D', 'E', 'O', 'U', 'H', 'R'],
                         'M': ['C', 'T', 'P'],
                         'N': ['G', 'Q'],
                         'O': ['T', 'L'],
                         'P': ['F', 'V', 'E', 'U', 'M', 'I'],
                         'Q': ['F', 'V', 'K', 'S', 'N', 'H'],
                         'R': ['G', 'T', 'L'],
                         'S': ['Q', 'J', 'L'],
                         'T': ['K', 'M', 'O', 'R'],
                         'U': ['L', 'P'],
                         'V': ['Q', 'P']}

DRUGI_KROK_SLOWNIK = {'A': ['B', 'D'],       # Deklaracja slownika z wszystkimi mozliwymi kombinacjami
                      'B': ['F', 'E', 'A'],  # dla drugiego kroku.
                      'C': ['G'],
                      'D': ['F', 'H', 'A'],
                      'E': ['K', 'I', 'B'],
                      'F': ['K', 'M', 'B', 'D'],
                      'G': ['C', 'L'],
                      'H': ['M', 'N', 'D'],
                      'I': ['O', 'E'],
                      'J': ['P'],
                      'K': ['F', 'O', 'E'],
                      'L': ['Q', 'G', 'P'],
                      'M': ['F', 'R', 'H'],
                      'N': ['R', 'H'],
                      'O': ['K', 'S', 'I'],
                      'P': ['J', 'T', 'L'],
                      'Q': ['T', 'L'],
                      'R': ['M', 'U', 'N'],
                      'S': ['O', 'V'],
                      'T': ['Q', 'P'],
                      'U': ['R', 'V'],
                      'V': ['S', 'U']}


def nieparzyste_n(litera, n, dynamiczny_slownik):
    '''
    Funkcja zliczajaca ilosc unikalnych ciagow znakow dla nieparzystego n.

    :param litera:  Litera dla ktorej chcemy obliczyc ilosc mozliwych podciagow.
    :param n: Ilosc krokow.
    :param dynamiczny_slownik: Slownik zapamietujacy ilosc roznych podciagow dla kazdej litery.
    W celu zoptymalizowania algorytmu
    :return: Ilosc roznych podciagow dla podanej litery 'litera' oraz 'n' krokow.
    '''

    if n == 1:
        return len(PIERWSZY_KROK_SLOWNIK[litera])  # Zwracamy ilosc podciagow dla ostatniego n

    suma = 0  # Zmienna zliczajaca ilosc podciagow dla danej litery
    if n % 2 != 0:
        for i in PIERWSZY_KROK_SLOWNIK[litera]:
            if (i, n) in dynamiczny_slownik:
                suma += dynamiczny_slownik[(i, n)]  # Dodanie juz spamietanej ilosci dla danej litery oraz n
            else:
                liczba_dzieci = nieparzyste_n(i, n - 1,
                                              dynamiczny_slownik)  # Wywolanie rekurencyjne dla kazdej litery z pociagu
                dynamiczny_slownik[(i, n)] = liczba_dzieci  # Spamietywanie ilosci podciagow do slownika
                suma += liczba_dzieci  # Zliczanie ilosci podciagow
    else:
        for i in DRUGI_KROK_SLOWNIK[litera]:
            if (i, n) in dynamiczny_slownik:
                suma += dynamiczny_slownik[(i, n)]  # Dodanie juz spamietanej ilosci dla danej litery oraz n
            else:
                liczba_dzieci = nieparzyste_n(i, n - 1,
                                              dynamiczny_slownik)  # Wywolanie rekurencyjne dla kazdej litery z pociagu
                dynamiczny_slownik[(i, n)] = liczba_dzieci  # Spamietywanie ilosci podciagow do slownika
                suma += liczba_dzieci  # Zliczanie ilosci podciagow
    return suma


def parzyste_n(litera, n, dynamiczny_slownik):
    '''
    Funkcja zliczajaca ilosc unikalnych ciagow znakow dla parzystego n.

    :param litera: Litera dla ktorej chcemy obliczyc ilosc mozliwych podciagow.
    :param n: Ilosc krokow.
    :param dynamiczny_slownik: Slownik zapamietujacy ilosc roznych podciagow dla kazdej litery oraz n.
    W celu zoptymalizowania algorytmu
    :return: Ilosc roznych podciagow dla podanej litery 'litera' oraz 'n' krokow.
    '''

    if n == 1:
        return len(DRUGI_KROK_SLOWNIK[litera])  # Zwracamy ilosc podciagow dla ostatniego n

    suma = 0  # Zmienna zliczajaca ilosc podciagow dla danej litery
    if n % 2 == 0:
        for i in PIERWSZY_KROK_SLOWNIK[litera]:
            if (i, n) in dynamiczny_slownik:
                suma += dynamiczny_slownik[(i, n)]  # Dodanie juz spamietanej ilosci dla danej litery oraz n
            else:
                liczba_dzieci = parzyste_n(i, n - 1,
                                           dynamiczny_slownik)  # Wywolanie rekurencyjne dla kazdej litery z pociagu
                dynamiczny_slownik[(i, n)] = liczba_dzieci  # Spamietywanie ilosci podciagow do slownika
                suma += liczba_dzieci  # Zliczanie ilosci podciagow
    else:
        for i in DRUGI_KROK_SLOWNIK[litera]:
            if (i, n) in dynamiczny_slownik:
                suma += dynamiczny_slownik[(i, n)]  # Dodanie juz spamietanej ilosci dla danej litery oraz n
            else:
                liczba_dzieci = parzyste_n(i, n - 1,
                                           dynamiczny_slownik)  # Wywolanie rekurencyjne dla kazdej litery z pociagu
                dynamiczny_slownik[(i, n)] = liczba_dzieci  # Spamietywanie ilosci podciagow do slownika
                suma += liczba_dzieci  # Zliczanie ilosci podciagow
    return suma


def wykonaj(litera, n):
    '''
    Glowna funkcja wywolujaca 'nieparzyste_n' dla nieparzystego n
    oraz 'patzyste_n' dla parzystego n.
    :param litera: Litera dla ktorej chcemy obliczyc ilosc mozliwych podciagow
    :param n: Ilosc krokow.
    :return: Ilosc roznych podciagow dla podanej litery 'litera' oraz 'n' krokow.
    '''
    dynamiczny_slownik = {}
    if n % 2 != 0:
        return nieparzyste_n(litera, n, dynamiczny_slownik)
    return parzyste_n(litera, n, dynamiczny_slownik)


letter, n = input().split(",")
print(wykonaj(letter, int(n[:-1])))
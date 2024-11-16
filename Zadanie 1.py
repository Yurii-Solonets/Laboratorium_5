def oblicz_kwadrat(liczba):
    return liczba ** 2

liczba = float(input("Podaj liczbę: "))
wynik = oblicz_kwadrat(liczba)
print(f"Kwadrat liczby {liczba}, wynosi: {wynik}.")
def oblicz_średnia (lista_liczb):
    if len (lista_liczb) == 0:
        return "Lista jest pusta. Nie można obliczyć średniej."
    return sum(lista_liczb) / len(lista_liczb)

liczba1 = [10, 20, 30, 40, 50]
liczba2 = [5, 15, 25]
liczba3 = []

print(f"Średnia z listy {liczba1}, wynosi: {oblicz_średnia(liczba1)}")
print(f"Średnia z listy {liczba2}, wynosi: {oblicz_średnia(liczba2)}")
print(f"Średnia z pystej listy: {oblicz_średnia(liczba3)}")
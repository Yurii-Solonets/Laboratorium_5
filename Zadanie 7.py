def potęga(a, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / potęga(a, -n)
    else:
        return a * potęga(a, n - 1)

a = float(input("Podaj podstawę a: "))
n = int(input("POdaj wykładnik n: "))

wynik = potęga(a, n)
print(f"{a}, do potęgi {n}, wynosi: {wynik}.")
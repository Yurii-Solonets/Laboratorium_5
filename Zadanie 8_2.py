def znajdz_maksymalna(*args):
    for i, arg in enumerate(args, start = 1):
        print(f"Parametr {i}: {arg}")

    maksymalna_wartość = max(args) if args else None
    return maksymalna_wartość

wynik = znajdz_maksymalna(10, 20, -5, 50, 3.14)
print(f"Maksymalna wartość: {wynik}")
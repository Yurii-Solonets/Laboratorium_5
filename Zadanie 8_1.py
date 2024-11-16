def wyswietl_parametry(*args):
    for i, arg in enumerate(args, start = 1):
        print(f"Parametr {i}: {arg}")

wyswietl_parametry(5, "hello", 3.14, 12.7)